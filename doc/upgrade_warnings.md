# PDFSolid Conversion SDK for Python 1.3.0 Upgrade Warnings

This document lists the considerations that developers should be aware of when upgrading from previous versions to PDFSolid Conversion SDK for Python 1.3.0. Some interfaces and default behaviors have changed, so changes to your code or deployment files may be necessary to make sure your project compiles and produces the expected results with the new version.

**Upgrading to version 1.3.0 from version 1.2.0**

If you are upgrading from version 1.2.0 to version 1.3.0, please note the following changes between 1.2.0 and 1.3.0.

**Important: Upgrade the Python module and keep the model files in step.** Upgrade to 1.3.0 with `python -m pip install --upgrade --no-index --find-links path/to/extracted-wheels pdfsolidconversion==1.3.0`. Point `--find-links` to the extracted directory that actually contains your platform’s wheels. Import `PDFSolidConversion` on Windows and macOS, or `PdfSolidConversion` on Linux. The new module ships with matching native libraries; do not mix dynamic libraries from an older version with the new module. Your Python code does not need to be recompiled and existing 1.2.0 calls keep working, but the behavior changes below affect the conversion results.

**Important: The default table recognition model profile has changed.** 1.2.0 used the high-accuracy model by default, while 1.3.0 uses the balanced model by default. After upgrading, even without any code change, table recognition results and resource usage will differ from 1.2.0. If you want to keep the same behavior as 1.2.0, explicitly select the high-accuracy profile and load the table extension package `table_legacy.model` (see the description of the `table_recognition_accuracy` option below).

**Important: Upgrade the model file together with the SDK.** The `documentai.model` of 1.2.0 and earlier does not contain the resources required by the balanced profile, while the 1.3.0 model file keeps the same name, so **continuing to use the old file causes model loading to fail. Overwrite the old file in your deployment directory with the `documentai.model` bundled in the 1.3.0 SDK package.** The SDK package bundles the base model `documentai.model` by default, so the default configuration needs no extra download; download the corresponding extension model packages only when you need extended capabilities such as high-accuracy tables, high-accuracy OCR, or orientation correction. For the contents and purposes of the model packages, see "Model Package Reference" in the "Set DocumentAI Model" chapter of the Developer Guide.

In the LibraryManager class:

1. `set_document_ai_model` now supports incremental loading of model packages. The base package `documentai.model` provides layout analysis, balanced-profile table recognition, and basic OCR; capabilities such as high-accuracy tables, high-accuracy OCR, and orientation correction are provided by extension packages. Each call loads only the capabilities contained in that file and merges them with the capabilities already loaded, without replacing them. Sample code:

   ```python
   LibraryManager.set_document_ai_model("path/documentai.model", -1)
   LibraryManager.set_document_ai_model("path/table_legacy.model", -1)
   ```

   If a package fails to load, the capabilities already loaded are kept and a specific error code is returned.

2. The timing of release and configuration has changed. If synchronous conversion tasks are still running when `LibraryManager.release` is called, the release is deferred until the last task returns, and new tasks are refused in the meantime; `release_document_ai_model` likewise waits for running tasks to return before cleaning up. While tasks are running or a release is still pending, reconfiguring the DocumentAI model is refused and `ErrorCode.CONVERTING_ERROR` is returned, and `LibraryManager.get_page_count` returns `-1` while library resources are being released or configured. Unload the SDK only after all conversion calls have returned, and load or reload models only after all conversion tasks have finished.

3. The new `LibraryManager.get_license_type` interface returns the type of the currently verified license: `LicenseType.UNKNOWN`, `LicenseType.TRIAL`, or `LicenseType.FORMAL`. It does not verify the license again and does not consume page quota. Sample code:

   ```python
   # Windows and macOS; on Linux import from PdfSolidConversion instead.
   from PDFSolidConversion import LibraryManager, LicenseType

   license_type = LibraryManager.get_license_type()
   if license_type == LicenseType.TRIAL:
       print("Trial license")
   ```

In the CPDFConversion class:

1. A new `start_word_to_pdf` interface converts Word documents (.docx) to PDF (the 1.2.0 Python module has no such entry point). Sample code:

   ```python
   error = CPDFConversion.start_word_to_pdf("input.docx", "output.pdf")
   ```

   When the document contains features that may affect fidelity, `ErrorCode.UNSUPPORTED_FEATURE` (95) is returned. The PDF is usually still produced in this case, so **do not assume that no output file exists just because 95 is returned**; check the output file. If the conversion itself fails, the real error code is returned and takes precedence over 95. The C / C++ interfaces also provide an optional diagnostics buffer that reports the feature identifiers and the output status; the Python interface does not provide this parameter.

2. Word to PDF shares `ConvertOptions` with PDF conversion; only the bookmark mode and the page range take effect: `word_pdf_bookmark_mode` is `WordPdfBookmarkMode.NONE` (default, no bookmarks), `WordPdfBookmarkMode.HEADINGS` (one bookmark per heading), or `WordPdfBookmarkMode.WORD_BOOKMARKS` (one bookmark per Word bookmark); `page_ranges` specifies the pages to output, e.g. `"1-3,5,7-9"`, and an empty value outputs every page. Sample code:

   ```python
   options = ConvertOptions()
   options.word_pdf_bookmark_mode = WordPdfBookmarkMode.HEADINGS
   options.page_ranges = "1-3,5,7-9"
   error = CPDFConversion.start_word_to_pdf("input.docx", "output.pdf", options, callback)
   ```

3. The conversion behavior for image input has changed:
   - When an image is converted to TXT or CSV-format Excel and OCR is not enabled, `ErrorCode.UNSUPPORTED_FEATURE` (95) is now returned; enable `enable_ocr`.
   - With OCR off (the default), an image converted to a format that can carry images produces an output document that contains the complete source image and no recognized text.
   - `CPDFConversion.start_pdf_to_image` accepts both PDF and supported image input. Image-to-image conversion does not run OCR or layout analysis and does not depend on any model; multi-page TIFF is converted frame by frame, each selected frame produces one image, and `page_ranges` selects the frames.

In the conversion options class ConvertOptions:

1. New option `table_recognition_accuracy` selects the table recognition accuracy. **The default is `TableRecognitionAccuracy.BALANCED`, which differs from 1.2.0, where the high-accuracy profile was the default.** Selecting `TableRecognitionAccuracy.HIGH_ACCURACY` requires `table_legacy.model` to be loaded; if it is not loaded, the conversion still succeeds, but tables are recognized with the rule-based method instead, so the result differs from the high-accuracy result. To keep the same behavior as 1.2.0, change the original:

   ```python
   options = ConvertOptions()
   CPDFConversion.start_pdf_to_word("input_file", "password", "output_path.docx", options)
   ```

   to:

   ```python
   LibraryManager.set_document_ai_model("/path/documentai.model", -1)
   LibraryManager.set_document_ai_model("/path/table_legacy.model", -1)

   options = ConvertOptions()
   options.table_recognition_accuracy = TableRecognitionAccuracy.HIGH_ACCURACY
   CPDFConversion.start_pdf_to_word("input_file", "password", "output_path.docx", options)
   ```

2. New option `enable_auto_page_size`: when enabled, the output page size of image conversion is matched to the nearest standard paper size based on the image resolution; when disabled, one image pixel becomes one page point. It only takes effect for image input; the default is `False`.

3. New options `custom_page_width` and `custom_page_height`, in points (1 point = 1/72 inch). When both are set, they specify the output page size directly and take precedence over `enable_auto_page_size`; the image is scaled proportionally to fit inside the page without cropping. They only take effect for image input; the default is `0`. Sample code:

   ```python
   options = ConvertOptions()
   options.enable_auto_page_size = True
   CPDFConversion.start_pdf_to_word("input.png", "", "path/output.docx", options)

   options = ConvertOptions()
   options.custom_page_width = 595.28
   options.custom_page_height = 841.89
   CPDFConversion.start_pdf_to_word("input.png", "", "path/output_a4.docx", options)
   ```
