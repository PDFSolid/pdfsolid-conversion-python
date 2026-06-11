# PDFSolid Conversion SDK for Python

High-performance Python SDK for converting PDF to Word, Excel, PowerPoint, HTML, Image, TXT, RTF, CSV, JSON, Markdown, Searchable PDF, and OFD with AI-powered OCR, layout analysis, and table recognition.

## Features

- **PDF to Word** (.docx) - Flow and Box layout modes
- **PDF to Excel** (.xlsx) - Table-per-sheet, page-per-sheet, or document-per-sheet
- **PDF to PowerPoint** (.pptx)
- **PDF to HTML** (.html) - Single/multi-page with optional bookmarks
- **PDF to CSV** (.csv)
- **PDF to Image** (.png, .jpg, .jpeg, .jpeg2000, .bmp, .tiff, .tga, .gif, .webp)
- **PDF to Plain Text** (.txt)
- **PDF to RTF** (.rtf)
- **PDF to Searchable PDF** (.pdf)
- **PDF to OFD** (.ofd)
- **PDF to JSON** (.json) - Structured data extraction
- **PDF to Markdown** (.md)

### AI-Powered Document Tools

- **OCR** (Optical Character Recognition) - 16+ language scripts
- **Layout Analysis** - AI-based document structure detection
- **Table Recognition** - Reconstructs table structure including merged cells
- **Custom AI Models** - Plug in your own OCR/Layout/Table engine via callbacks (SDK v4.1.0+)

## Requirements

| Platform | System Requirements | Python Version |
| -------- | ------------------- | -------------- |
| Windows | Windows 7, 8, 10, 11 (32/64-bit) | Python 3.10+ |
| Linux | Linux x64, GLIBC 2.31+ | Python 3.10+ |
| macOS | macOS 10.14+ (Intel, Apple Silicon) | Python 3.10+ |

## Installation

```shell
pip install PDFSolidConversion
```

## Quick Start

```python
from PDFSolidConversion import LibraryManager, ConvertOptions, CPDFConversion

# 1. Verify license
LibraryManager.license_verify("LICENSE_KEY", "device_id", "app_id")

# 2. Initialize SDK resources
LibraryManager.initialize("PDFSolid_Conversion_SDK/resource")

# 3. Convert PDF to Word
options = ConvertOptions()
CPDFConversion.start_pdf_to_word("input.pdf", "", "output.docx", options)

# 4. Release resources
LibraryManager.release()
```

## Usage Examples

### Convert PDF to Word with Layout Modes

```python
from PDFSolidConversion import LibraryManager, ConvertOptions, CPDFConversion, PageLayoutMode

options = ConvertOptions()

# Flow layout - flexible, editable output
options.page_layout_mode = PageLayoutMode.FLOW
CPDFConversion.start_pdf_to_word("input.pdf", "", "output_flow.docx", options)

# Box layout - high-precision reproduction
options.page_layout_mode = PageLayoutMode.BOX
CPDFConversion.start_pdf_to_word("input.pdf", "", "output_box.docx", options)
```

### Convert PDF to Excel

```python
from PDFSolidConversion import ConvertOptions, CPDFConversion, ExcelWorksheetOption

options = ConvertOptions()
options.excel_worksheet_option = ExcelWorksheetOption.FOR_TABLE
CPDFConversion.start_pdf_to_excel("input.pdf", "", "output.xlsx", options)
```

### Convert PDF to Image

```python
from PDFSolidConversion import ConvertOptions, CPDFConversion, ImageType

options = ConvertOptions()
options.image_type = ImageType.PNG
options.image_scaling = 2.0
CPDFConversion.start_pdf_to_image("input.pdf", "", "output", options)
```

### OCR with Multiple Languages

```python
from PDFSolidConversion import LibraryManager, ConvertOptions, CPDFConversion, OCRLanguage

LibraryManager.set_document_ai_model("path/documentai.model", -1)

options = ConvertOptions()
options.enable_ocr = True
options.languages = [OCRLanguage.ENGLISH, OCRLanguage.CHINESE]
CPDFConversion.start_pdf_to_word("scanned.pdf", "", "output.docx", options)
```

### Conversion Progress and Cancellation

```python
from PDFSolidConversion import ConvertOptions, CPDFConversion, ConvertCallback

def progress_callback(current: int, total: int):
    print(f"Progress: {current} / {total}")

callback = ConvertCallback()
callback.set_progress(progress_callback)
callback.set_cancel(lambda: False)

options = ConvertOptions()
CPDFConversion.start_pdf_to_word("input.pdf", "", "output.docx", options, callback)
```

### Custom AI Models via Callbacks (SDK v1.1.0+)

```python
from PDFSolidConversion import LibraryManager, ConvertOptions, CPDFConversion, ConvertCallback, OCRLanguage

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

## Conversion Options

| Option | Type | Description |
| ------ | ---- | ----------- |
| `enable_ai_layout` | bool | Enable AI layout analysis |
| `enable_ai_table_recognition` | bool | Enable AI table recognition |
| `enable_ocr` | bool | Enable OCR |
| `contain_image` | bool | Include images in output |
| `contain_annotation` | bool | Include annotations in output |
| `page_layout_mode` | PageLayoutMode | `FLOW` or `BOX` |
| `image_type` | ImageType | Output image format |
| `image_scaling` | float | Image scaling factor (default 1.0) |
| `image_color_mode` | ImageColorMode | `COLOR`, `GRAY`, or `BINARY` |
| `page_ranges` | str | Page ranges, e.g. `"1-3,5,7-9"` |
| `output_document_per_page` | bool | Output one file per page |
| `font_name` | str | Preferred output font name |
| `transparent_text` | bool | Transparent text layer (Searchable PDF/OFD) |
| `formula_to_image` | bool | Convert formulas to images |
| `languages` | list | OCR languages (`[OCRLanguage.ENGLISH]`) |

## OCR Languages

| Enum | Language |
| ---- | -------- |
| `OCRLanguage.CHINESE` | Chinese Simplified |
| `OCRLanguage.CHINESE_TRA` | Chinese Traditional |
| `OCRLanguage.ENGLISH` | English |
| `OCRLanguage.KOREAN` | Korean |
| `OCRLanguage.JAPANESE` | Japanese |
| `OCRLanguage.LATIN` | Latin script languages |
| `OCRLanguage.DEVANAGARI` | Devanagari |
| `OCRLanguage.CYRILLIC` | Cyrillic |
| `OCRLanguage.ARABIC` | Arabic |
| `OCRLanguage.TAMIL` | Tamil |
| `OCRLanguage.TELUGU` | Telugu |
| `OCRLanguage.KANNADA` | Kannada |
| `OCRLanguage.THAI` | Thai |
| `OCRLanguage.GREEK` | Greek |
| `OCRLanguage.ESLAV` | Eslav |
| `OCRLanguage.AUTO` | Auto-detect |

## API Reference

### LibraryManager

| Method | Description |
| ------ | ----------- |
| `license_verify(license, device_id, app_id)` | Verify license key |
| `initialize(resource_path)` | Initialize SDK resources |
| `release()` | Release all SDK resources |
| `release_document_ai_model()` | Release AI model resources only |
| `set_document_ai_model(file_path, gpu_id=-1)` | Set DocumentAI model path |
| `set_document_ai_model_count(layout_count, table_count)` | Set AI model instance counts |
| `set_logger(enable_info, enable_warning)` | Configure logging |
| `get_version()` | Get SDK version string |
| `get_page_count(file_path, password)` | Get page count of a document |

### CPDFConversion

| Method | Description |
| ------ | ----------- |
| `start_pdf_to_word(file_path, password, output_path, options, callback=None)` | Convert PDF to Word |
| `start_pdf_to_excel(file_path, password, output_path, options, callback=None)` | Convert PDF to Excel |
| `start_pdf_to_ppt(file_path, password, output_path, options, callback=None)` | Convert PDF to PowerPoint |
| `start_pdf_to_html(file_path, password, output_path, options, callback=None)` | Convert PDF to HTML |
| `start_pdf_to_image(file_path, password, output_path, options, callback=None)` | Convert PDF to Image |
| `start_pdf_to_rtf(file_path, password, output_path, options, callback=None)` | Convert PDF to RTF |
| `start_pdf_to_txt(file_path, password, output_path, options, callback=None)` | Convert PDF to TXT |
| `start_pdf_to_json(file_path, password, output_path, options, callback=None)` | Extract PDF to JSON |
| `start_pdf_to_markdown(file_path, password, output_path, options, callback=None)` | Extract PDF to Markdown |
| `start_pdf_to_searchable_pdf(file_path, password, output_path, options, callback=None)` | Convert PDF to Searchable PDF |
| `start_pdf_to_ofd(file_path, password, output_path, options, callback=None)` | Convert PDF to OFD |

### ConvertCallback

| Method | Description |
| ------ | ----------- |
| `set_progress(callback)` | Set progress callback `(current, total)` |
| `set_cancel(callback)` | Set cancel callback, return `True` to cancel |
| `set_ocr(callback)` | Set custom OCR trigger `(image_path) -> bool` |
| `set_get_ocr_result(callback)` | Set OCR result getter `() -> str` (JSON) |
| `set_layout(callback)` | Set custom layout trigger `(image_path) -> bool` |
| `set_get_layout_result(callback)` | Set layout result getter `() -> str` (JSON) |
| `set_table(callback)` | Set custom table trigger `(image_path) -> bool` |
| `set_get_table_result(callback)` | Set table result getter `() -> str` (JSON) |

## License

PDFSolid Conversion SDK is a commercial SDK. Contact [sales@pdfsolid.com](mailto:sales@pdfsolid.com) for license and trial information.

## Support

- Website: [https://www.pdfsolid.com](https://www.pdfsolid.com/)
- Email: [support@pdfsolid.com](mailto:support@pdfsolid.com)
