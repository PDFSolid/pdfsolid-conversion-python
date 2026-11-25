# PDFSolid Conversion SDK for Python

High-performance Python SDK for converting PDF to Word, Excel, PowerPoint, HTML, Image, TXT, RTF, CSV, JSON, Markdown, Searchable PDF, and OFD with AI-powered OCR, layout analysis, and table recognition. SDK v1.3.0 also converts Word documents (`.docx`) to PDF.

## Features

- **PDF to Word** (.docx) — Flow and Box layout modes
- **Word to PDF** (.docx → .pdf) — optional page ranges and PDF bookmarks
- **PDF to Excel** (.xlsx) — per-table, per-page, or per-document worksheet options
- **PDF to PowerPoint** (.pptx)
- **PDF to HTML** (.html) — single/multi-page with optional bookmark navigation
- **PDF to CSV** (.csv)
- **PDF to Image** (.png, .jpg, .jpeg, .jpeg2000, .bmp, .tiff, .tga, .gif, .webp) — color/grayscale/binary, configurable scaling
- **PDF to Plain Text** (.txt) — optional table format preservation
- **PDF to RTF** (.rtf)
- **PDF to Searchable PDF** (.pdf) — OCR with transparent text layer
- **PDF to OFD** (.ofd) — OCR, page background preservation, transparent text layer
- **PDF to JSON** (.json) — structured data with table extraction
- **PDF to Markdown** (.md)

### AI-Powered Document Tools

- **OCR** — Optical Character Recognition for scanned documents and images
- **Layout Analysis** — AI-based document structure parsing
- **Table Recognition** — AI-based table structure reconstruction
- **Custom AI Models** — plug in your own OCR, layout, or table engine via callbacks (SDK v1.1.0+)

## Requirements

| Platform | System Requirements | Development Environment |
| -------- | ------------------- | ----------------------- |
| Windows | Windows x64 (use a Windows version supported by your CPython build) | CPython 3.8–3.14 |
| Linux | Linux x64, GLIBC 2.31+ | CPython 3.10–3.14 |
| macOS | macOS 11.0+ (Intel x86_64, Apple Silicon arm64) | CPython 3.10–3.14 |

## Quick Start

Install the matching 1.3.0 `pdfsolidconversion` wheel from the SDK distribution; this repository does not contain wheels. The examples use `PDFSolidConversion` (Windows and macOS wheels). For the Linux x86_64 wheels, replace that import name with `PdfSolidConversion` (case-sensitive).

### 1. Get a License

Contact [sales@pdfsolid.com](mailto:sales@pdfsolid.com) for a 30-day free trial or commercial license.

### 2. Apply License and Initialize

```python
from PDFSolidConversion import LibraryManager

LibraryManager.license_verify("LICENSE_KEY", "device_id", "app_id")
LibraryManager.initialize("PDFSolid_Conversion_SDK/resource")
```

### 3. Convert

```python
from PDFSolidConversion import ConvertOptions, CPDFConversion

options = ConvertOptions()
CPDFConversion.start_pdf_to_word("input.pdf", "", "output.docx", options)
```

### Release Resources

```python
LibraryManager.release_document_ai_model()
LibraryManager.release()
```

## Conversion Examples

### Word (DOCX) to PDF

After applying the license and initializing the SDK, pass the input `.docx` path and a writable output `.pdf` path.

```python
# On Linux, import from PdfSolidConversion instead.
from PDFSolidConversion import CPDFConversion

status = CPDFConversion.start_word_to_pdf("input.docx", "output.pdf")
```

The default converts all pages without PDF bookmarks. On an optional `ConvertOptions` passed as the third argument, set `page_ranges` to select pages (for example, `1-2`) and `word_pdf_bookmark_mode` to generate bookmarks from headings or Word bookmarks. Check the returned status before using the PDF. `ErrorCode.UNSUPPORTED_FEATURE` means the input contains features that may affect fidelity; a PDF may still have been written.

### PDF to Excel

```python
from PDFSolidConversion import ConvertOptions, CPDFConversion, ExcelWorksheetOption

options = ConvertOptions()
options.excel_worksheet_option = ExcelWorksheetOption.FOR_TABLE
CPDFConversion.start_pdf_to_excel("input.pdf", "", "output.xlsx", options)
```

### PDF to Image

```python
from PDFSolidConversion import ConvertOptions, CPDFConversion, ImageType

options = ConvertOptions()
options.image_type = ImageType.PNG
options.image_scaling = 2.0
CPDFConversion.start_pdf_to_image("input.pdf", "", "output", options)
```

### PDF to Searchable PDF (OCR)

```python
from PDFSolidConversion import LibraryManager, ConvertOptions, CPDFConversion, OCRLanguage

LibraryManager.set_document_ai_model("path/model")

options = ConvertOptions()
options.enable_ocr = True
options.languages = [OCRLanguage.ENGLISH]
options.transparent_text = True
CPDFConversion.start_pdf_to_searchable_pdf("scan.pdf", "", "output.pdf", options)
```

### PDF to JSON with Table Extraction

```python
from PDFSolidConversion import ConvertOptions, CPDFConversion

options = ConvertOptions()
options.json_contain_table = True
CPDFConversion.start_pdf_to_json("input.pdf", "", "output.json", options)
```

### Custom AI Engine (SDK v1.1.0+)

```python
from PDFSolidConversion import ConvertOptions, CPDFConversion, ConvertCallback, OCRLanguage

def on_ocr(image_path: str) -> bool:
    return run_my_ocr_model(image_path)

def get_ocr_result() -> str:
    return ocr_json_result

callback = ConvertCallback()
callback.set_ocr(on_ocr)
callback.set_get_ocr_result(get_ocr_result)

options = ConvertOptions()
options.enable_ocr = True
options.languages = [OCRLanguage.ENGLISH]
CPDFConversion.start_pdf_to_word("input.pdf", "", "output.docx", options, callback)
```

## Documentation

- [Developer Guide](doc/developer_guide_python.md)
- [API Reference](doc/api_reference_python.html)

## Contact

- Website: [https://www.pdfsolid.com](https://www.pdfsolid.com/)
- Sales: [sales@pdfsolid.com](mailto:sales@pdfsolid.com)
- Support: [support@pdfsolid.com](mailto:support@pdfsolid.com)
