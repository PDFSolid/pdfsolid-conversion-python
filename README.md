# PDFSolid Conversion SDK for Python

High-performance Python SDK for converting PDF to Word, Excel, PowerPoint, HTML, Image, TXT, RTF, CSV, JSON, Markdown, Searchable PDF, and OFD with AI-powered OCR, layout analysis, and table recognition.

## Features

- **PDF to Word** (.docx) — Flow and Box layout modes
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
| Windows | Windows 7, 8, 10, 11 (64-bit) | Python 3.10+ |
| Linux | Linux x64, GLIBC 2.31+ | Python 3.10+ |
| macOS | macOS 10.14+ (Intel, Apple Silicon) | Python 3.10+ |

## Quick Start

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
