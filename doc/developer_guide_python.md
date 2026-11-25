# 1. Overview

PDFSolid Conversion SDK is a high-performance library designed for extracting and transforming the data within your PDF files, such as text, images, tables, links, and annotations, into various file formats. Our Conversion SDK retains the original document layout and the properties of the file data, ensuring a seamless document conversion experience.

Effortlessly integrate the PDFSolid Conversion SDK into your projects in just a few steps, and enable the following file format conversions:

- Convert PDF to Word (.docx)
- Convert PDF to Excel (.xlsx)
- Convert PDF to PowerPoint (.pptx)
- Convert PDF to HTML (.html)
- Convert PDF to CSV (.csv)
- Convert PDF to Image (.png, .jpg, .jpeg, .jpeg2000, .bmp, .tiff, .tga, .gif, .webp)
- Convert PDF to Plain Text (.txt)
- Convert PDF to Rich Text Format (.rtf)

- Convert PDF to Searchable PDF (.pdf)


- Convert PDF to OFD (.ofd)

- Convert PDF to Structured Data (.json)
- Convert PDF to Markdown (.md)
- Convert Word to PDF (.docx to .pdf)


Harness the power of PDFSolid Conversion SDK and take your document processing to the next level with intelligent tools designed for accuracy and efficiency. To enhance your format conversion results, PDFSolid offers AI-powered document tools with the following capabilities:


- Optical Character Recognition (OCR)


- Layout Analysis


- Table Recognition



## 1.1 Why PDFSolid Conversion SDK

- Mature Technology

  With years of technology accumulation, we have established a complete mechanism of product iteration to offer a continuous guarantee for product competitiveness.

- Complete PDF and Format Conversion Functionalities

  Our comprehensive features can meet diverse needs and are easy for our customers to use without training costs.

- High-quality Service

  professional service and technical support to quickly respond to users' feedback through onsite service or remote support like telephone, email, etc.

- Independent Intellectual Property Rights

  Our technology is independent and compliant with ISO, helping enterprises conduct international business without considering copyright risks.

## 1.2 PDFSolid Conversion SDK

The PDFSolid Conversion SDK is designed to facilitate the effortless conversion of PDF files into various other formats, all while preserving the original layout and formatting of the documents. In this guide, we will explore the PDFSolid Conversion SDK and demonstrate how to utilize it within your Python projects.

## 1.3 License & Trial

The PDFSolid Conversion SDK is a commercial SDK that requires a license to grant developers the right to develop and distribute their applications. In development mode, each license is only valid for one device ID. PDFSolid provides flexible licensing models, please contact [our sale's team](mailto:support@pdfsolid.com) for more information. However, even if you have a license, it is prohibited to distribute any documents, sample code, or source code of the PDFSolid Conversion SDK to any third parties.

If you do not have a License, please feel free to contact the PDFSolid Team (support@pdfsolid.com) to obtain a License to try the PDFSolid Conversion SDK.
# 2. Getting Started

## 2.1 Requirements
Before starting, please make sure that you have already met the following prerequisites.

### 2.1.1 Get PDFSolid License Key

PDFSolid provides two types of license key: 30-day free trial license, and commercial license.

#### How to Get Free Trial License

Contact our sales team (support@pdfsolid.com) and we'll send you a 30-day free trial license for PDFSolid Conversion SDK.

#### How to Get Commercial License

PDFSolid Conversion SDK is a commercial SDK that requires a license for application release. Any documents, sample code, or source code distribution from the released package of PDFSolid to any third party is prohibited.

**Contact Sales**

To get commercial license for PDFSolid Conversion SDK, feel free to contact our sales team (support@pdfsolid.com) .

For Python Conversion SDK, the commercial license must be bound to your developer device ID (How to find the developer device ID), and each license is only valid for one device ID in development mode.


### 2.1.2 Download Conversion SDK

Contact us (support@pdfsolid.com) to obtain the PDFSolid Python Conversion SDK.


### 2.1.3 System Requirements

| Platform | System Requirements | Development Environment | Python import |
| :------ | :------ | :------ | :------ |
| Windows | Windows x64 supported by your CPython build | CPython 3.8–3.14 | `PDFSolidConversion` |
| macOS | macOS 11.0+ (Intel x86_64 or Apple Silicon arm64) | CPython 3.10–3.14 | `PDFSolidConversion` |
| Linux | Linux x86_64, glibc 2.31+ | CPython 3.10–3.14 | `PdfSolidConversion` |

## 2.2 SDK Package Structure

The PDFSolid Conversion SDK for Python should contain at least the following:


- ***"doc"*** - API reference and developer guide.
- ***"samples"*** - Python sample projects or scripts.
- ***"resource"*** - OCR models, DocumentAI models, and other resource files.
- Python installation package or module distribution files.
- ***"release_notes.txt"*** - Release notes.
- ***"legal.txt"*** - Legal and copyright information.

**About model files:** The SDK package ships with the base model `documentai.model` by default (in the `resource/models` directory), so the default configuration requires no additional model download. Extension model packages need to be downloaded only when you need a higher-accuracy variant or extended features. See [Model Package Description](#model-package-description) in 3.2.

![package](image/package.png)
### 2.2.1 Apply the License Key
If you don't have a license key, please check out [how to obtain a license key](#211-get-pdfsolid-license-key).

PDFSolid Conversion SDK currently supports offline authentication to verify license keys.

*Learn about:*

What is the authentication mechanism of PDFSolid's license?

#### Copy the License Key

Accurately obtaining the license key is crucial for the application of the license.

1. In the email you received, locate the XML file containing the license key.
2. Open the XML file, and determine the license type based on the `<type>` field. If `<type>online</type>` is present, it indicates an online license. If `<type>offline</type>` is present or if the field is absent, it indicates an offline license.

**Online License**:

```xml
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<license version="1">
    <platform>windows</platform>
    <starttime>xxxxxxxx</starttime>
    <endtime>xxxxxxxx</endtime>
    <type>online</type>
    <key>LICENSE_KEY</key>
</license>

```

**Offline License**:

```xml
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<license version="1">
    <platform>windows</platform>
    <starttime>xxxxxxxx</starttime>
    <endtime>xxxxxxxx</endtime>
    <key>LICENSE_KEY</key>
</license>

```

3. Copy the value located at the LICENSE_KEY position within the `<key>LICENSE_KEY</key>` field. This is your license key.

#### Apply the License Key
You can perform offline authentication using the following method:

Before using the classes and methods of the PDFSolid Conversion SDK in your project, you need to initialize the SDK with a valid license key. If you don’t have a license key, feel free to contact the PDFSolid team (support@pdfsolid.com) to obtain one.

```python
# Windows and macOS; on Linux import from PdfSolidConversion instead.
from PDFSolidConversion import *

error_code = LibraryManager.license_verify("", "", "")
```
## 2.3 How to Run a Demo

The generic documentation and samples do not include wheels. Obtain the matching SDK wheel bundle for your platform: Windows x64 wheels are at the root of the Windows wheel ZIP; macOS wheels are in `lib/` of the macOS package; Linux wheels are in `wheelhouse/` of the Linux package. Use the Linux package’s sample and README on Linux; the generic `samples/demo.py` uses the Windows/macOS import spelling.

From the extracted SDK root, install the wheel for your interpreter and architecture (replace `path/to/extracted-wheels` with the directory containing the wheels):

```sh
python -m pip install --no-index --find-links path/to/extracted-wheels pdfsolidconversion==1.3.0
```

On Windows or macOS, run the included sample from the extracted SDK root:

```sh
python samples/demo.py
```

# 3. Conversion Guides

PDFSolid Conversion SDK allows developers to use a simple API to convert PDF to commonly used file
formats such as Word, Excel, PowerPoint, HTML, CSV, PNG, JPEG, RTF, TXT, Searchable PDF, OFD, JSON, and Markdown. It provides a wide range of customized conversion
options, such as whether to include images or annotations in PDF documents, whether to enable OCR, whether to enable layout analysis, and more.
## 3.1 Initialize Library Resources

#### **Overview**

Initialize the necessary file and memory resources required by the PDFSolid Conversion SDK.

#### **Notes**

- You must initialize SDK resources before calling any conversion interface.

- When using OCR, Layout Analysis, Table Recognition, PDF to Searchable PDF, or PDF to OFD, make sure the DocumentAI model resources in the `resource` directory are available.


#### **Example**

```python
LibraryManager.initialize("PDFSolid_Conversion_SDK/resource")
```
## 3.2 Set DocumentAI Model

#### **Overview**

Before using OCR, Layout Analysis, Table Recognition you need to set the DocumentAI model path first.

`set_document_ai_model` supports an optional `gpu_id` parameter used to specify the GPU device index for the AI model. When `gpu_id` is `-1`, GPU acceleration is disabled. The interface returns an `ErrorCode`.

The SDK package ships with the base model `documentai.model`, which is all the default configuration needs. Load extension packages only when you need a higher-accuracy variant or extended features (see [Model Package Description](#model-package-description)).

#### **Incremental Loading of Model Packages**

- Each call loads only the capabilities contained in that file and **merges** them with the capabilities already loaded; nothing is replaced. The loading order is not restricted.
- If a package fails to load, the capabilities loaded earlier are kept and a specific error code is returned. The SDK does not silently degrade.
- `release_document_ai_model()` releases all loaded models; reload them before using AI features again.
- While a conversion task is running, or while a release has not yet completed, loading a model again is rejected and `ErrorCode.CONVERTING_ERROR` is returned.

#### **Set AI Model Instance Count**

If you need to control the number of Layout Analysis and Table Recognition model instances, call the corresponding interface to set the model instance counts.


#### **Use Your Own AI Engine (SDK v1.1.0+)**

This option is available only in SDK v1.1.0 or later. You can skip `set_document_ai_model` and plug in your own OCR, Layout Analysis, or Table Recognition engine through the callbacks on `ConvertCallback`. See [3.12 Use Custom AI Models via Callbacks](#312-use-custom-ai-models-via-callbacks) for details.


#### **Sample**

```python
model_path = "***"
LibraryManager.set_document_ai_model_count(1, 1)
LibraryManager.set_document_ai_model(model_path)
```

Loading the base package followed by extension packages:

```python
# Windows and macOS; on Linux import from PdfSolidConversion instead.
from PDFSolidConversion import LibraryManager, ErrorCode

# Load the base package first
result = LibraryManager.set_document_ai_model("/path/documentai.model", -1)
if result != ErrorCode.SUCCESS:
    raise RuntimeError(f"load documentai.model failed: {result}")

# Load extension packages when needed; capabilities already loaded are kept
LibraryManager.set_document_ai_model("/path/table_legacy.model", -1)
LibraryManager.set_document_ai_model("/path/document_process.model", -1)
```

#### **Model Package Description**

##### **What the model packages are and where to get them**

The AI capabilities of PDFSolid Conversion SDK (layout analysis, table recognition, OCR, orientation correction, etc.) depend on model files. **The SDK package ships with the base model `documentai.model` by default; the default configuration requires no additional download.** Download an extension package only when you need a higher-accuracy variant or extended features, place it in a directory of your choice, and specify its path with `LibraryManager.set_document_ai_model`.

The model packages consist of one base package and several extension packages:

| File | Size | Purpose | How to obtain / when needed |
| --- | --- | --- | --- |
| `documentai.model` | about 230 MB | Base package: layout analysis, table recognition (balanced profile), and all basic OCR languages | **Shipped with the SDK package by default**; required for any AI feature (layout analysis, OCR, table recognition) |
| `table_legacy.model` | about 270 MB | Table extension package: resources such as bordered / borderless table detection required by the high-accuracy profile | Download separately; needed only when using the `TableRecognitionAccuracy.HIGH_ACCURACY` profile, not for the default balanced profile |
| `ocr_server.model` | about 139 MB | High-accuracy OCR enhancement package, covering Chinese, English, Japanese, and other languages | Download separately; needed when higher OCR accuracy is required |
| `document_process.model` | about 37 MB | Document orientation classification and skew correction | Download separately; needed when using `enable_document_orientation_classification` (orientation detection) or `enable_document_dewarp` (dewarping) |

The four files total about 676 MB. **If you do not need the extra features, you do not have to download any extension package**: the default configuration uses only the `documentai.model` shipped with the SDK package.

##### **Loading**

All model packages are loaded through the same interface, `LibraryManager.set_document_ai_model`. See "Incremental Loading of Model Packages" above for the rules.

##### **Version compatibility**

- A model package must match the SDK version. The `documentai.model` shipped with the SDK package is the version that matches 1.3.0; **please also download the 1.3.0 version of any extension package.**
- The `documentai.model` of 1.2.0 and earlier **does not contain** the resources required by the balanced profile, while 1.3.0 keeps the same file name. **If you copied an old `documentai.model` into your own deployment directory or project, overwrite it with the new file from the 1.3.0 SDK package when upgrading; do not keep using the old file of the same name.** Loading an old model returns an error and does not fall back to the high-accuracy profile automatically.
- Do not replace only the Python module or only the model files; they must be updated together.

##### **FAQ**

| Symptom | Possible cause |
| --- | --- |
| `set_document_ai_model` returns an error | Wrong path; the model file does not match the SDK version; the file is incomplete (interrupted download) |
| Tables look different from (or worse than) expected with `HIGH_ACCURACY` | `table_legacy.model` has not been loaded (tables fell back to rule-based recognition) |
| A conversion returns `ErrorCode.LICENSE_OCR_PERMISSION_DENY` (29) | The license does not include the OCR permission; unrelated to the models |

## 3.3 OpenVINO Acceleration Package

### **Overview**

If your device uses an Intel processor, you can deploy the optional OpenVINO acceleration package to speed up AI recognition such as OCR. Once the package is deployed, the SDK automatically uses the OpenVINO backend when it loads the DocumentAI model, **with no code changes and no extra settings**.

### **Applicability**

- Operating system: Windows x64.
- Processor: Intel CPU.
- The package only affects the speed of AI inference (such as OCR recognition). It does not change any conversion API or conversion option.

### **Get the Package**

Download the OpenVINO acceleration package that matches your SDK version. The package must match the SDK version; do not mix files from different versions.

### **Deployment**

1. Extract the downloaded package.
2. Copy **all files** in the package to the directory that contains the SDK dynamic libraries, that is, the same directory as the `onnxruntime` runtime library.
3. Load the model with `LibraryManager.set_document_ai_model` and run conversions as usual. The SDK uses the OpenVINO backend automatically.

### **Notice**

- If the package is missing, incomplete, or does not match the SDK version, the SDK automatically uses the default CPU backend. Conversion continues normally and no error is reported for this reason.
- Deploy the whole package. Do not copy or replace only some of its files.
- Deploy the package before the model is loaded. A model that is already loaded does not switch backends, so restart the program or reload the model after deployment.
- The OpenVINO backend uses more memory. The actual speed-up depends on the processor model, document content, and thread settings, and not every scenario becomes faster.
- To stop using acceleration, delete these files. The SDK then returns to the default CPU backend.

## 3.4 Get Conversion Progress

PDFSolid Conversion SDK obtains the conversion progress through callback functions. The following example demonstrates how to get the conversion progress while performing a PDF to Word task.


```python
def progress_callback(current: int, total: int):
  print(f"Progress: {current} / {total}")

callback = ConvertCallback()
callback.set_progress(progress_callback)
```
## 3.5 Cancel Conversion Task

PDFSolid Conversion SDK supports interrupting your ongoing conversion task at any time. The following example demonstrates how to interrupt your ongoing conversion task.


```python
def cancel_callback():
  return False

callback = ConvertCallback()
callback.set_cancel(cancel_callback)
```
## 3.6 Select Page Range for Conversion

PDFSolid Conversion SDK supports converting a specified page range. When an empty string is passed, all pages will be converted. If the page range exceeds one page, you can also choose to enable the `output_document_per_page` option to output each PDF page as a separate file. The following example demonstrates how to specify a page range when performing a conversion task:

```python
options = ConvertOptions()
options.output_document_per_page = False
options.page_ranges = "1-3,5,7-9"
```
## 3.7 Conversion Options: Contain Image & Annotation

#### **Overview**

In the process of converting PDF documents into various formats, PDFSolid Conversion SDK offers two additional options for users: one option to determine whether images are included in the generated document, and another to decide if annotations from the PDF file are to be retained.

- With the "Include Images" option enabled, PDFSolid Conversion SDK will extract the images from the PDF document and embed them in the corresponding pages and positions in the output file. For areas with overlapping images, PDFSolid Conversion SDK merges these images into one and embeds it into the exact location on the corresponding page of the output file.

- When the "Include Annotations" option is selected, most annotations are converted into raster images and embedded at the respective positions within your document. However, certain types of annotations, such as highlights, underlines, strikeouts, and squiggly, are converted into their respective formatting equivalents in the converted Word, PPT, and HTML documents, and are marked over the corresponding text. It is important to note that the conversion won't be 100% accurate in every instance.

In the PDFSolid Conversion SDK, the options for including images and annotations are commonly used in the following format conversions:

- PDF to Word
- PDF to Excel
- PDF to PowerPoint
- PDF to HTML
- PDF to RTF
- Extract PDF to JSON
- Extract PDF to Markdown

#### **About Text Markup Annotation**

- **Highlight:** When converting PDF to Word format keeping the highlight markups, it is important to note that Microsoft Word only supports 15 highlighter colors. To approximate the original document's appearance as closely as possible, text in the Word document will be marked with a text background color that matches the color of the original document's highlight annotation. For conversions to Microsoft PPT format, the native highlighting feature within the format is used to mark the text. In the case of converting to HTML format, a unique `<span>` tag is created for the marked text, and the background style is set to match the color of the corresponding annotation in the original document.

- **Underlines & Squiggly:** When converting PDF to Word or PPT formats keeping the underline and squiggly markups, the marked text will be marked with the same style in Microsoft Office. When converted to HTML format, the marked text will be styled to display the same effect. However, if a paragraph of text in the original document is marked by both underline and squiggly, then the text will only be marked with one type (Because squiggly is actually a type of underline in Word, PPT, and HTML formats).
  
- **Strikeout:** When converting strikeout markups to Word and PowerPoint formats, the marked text will be added with a strikeout natively supported by Microsoft Office. However, in these two file formats, the color of the strikeout itself cannot be the same as that in the original PDF document because the strikeout color in Word and PPT will only change according to the color of the marked text font itself. When converted to HTML format, the same strikeout color as the original document will be displayed.
  

#### **Sample**

This Sample demonstrates how to use the PDFSolid Conversion SDK to convert a PDF document to a Word document with the selected options: Include images and annotations.

```python
input_file_path = "***"
password = "***"
output_file_name = "***"

word_options = ConvertOptions()
word_options.contain_image = True
word_options.contain_annotation = True
word_options.enable_ai_layout = True
word_options.enable_ocr = False

error = CPDFConversion.start_pdf_to_word(input_file_path, password, output_file_name, word_options)
```
## 3.8 Page Layout Mode

In certain formats, the page layout mode plays a key role in the quality of the converted document. PDFSolid Conversion SDK supports two layout modes: Flow Layout and Box Layout.

- **Flow Layout:** This layout uses paragraph indentations, columns, and tab positions to adjust the content. Its main advantage is flexibility; content can flow automatically as the document is edited, and it adapts to various screen sizes on different devices. This layout also supports structured maintenance and can implement consistent global formatting through style templates (e.g., titles, body text). Common use cases include documents that are frequently modified, such as reports, manuals, and dynamic tables.
- **Box Layout:** Based on the PDF's "digital paper" model, this layout accurately positions every element (text, images, tables) on the page using a coordinate system (e.g., text is positioned 5 cm from the top and 3 cm from the left). The main advantage is high-precision rendering, which ensures consistency across different platforms. This layout is particularly useful for documents requiring precise reproduction, such as contracts, design drafts, and academic papers.

In the PDFSolid Conversion SDK, page layout modes are commonly used in the following format conversions:

- PDF to Word
- PDF to HTML

#### **Sample**

This example demonstrates how to convert a PDF document to Word with Flow Layout and Box Layout:

```python
input_file_path = "***"
password = "***"
output_file_name = "***"

word_options = ConvertOptions()
word_options.page_layout_mode = PageLayoutMode.FLOW
error = CPDFConversion.start_pdf_to_word(input_file_path, password, output_file_name, word_options)

word_options.page_layout_mode = PageLayoutMode.BOX
error = CPDFConversion.start_pdf_to_word(input_file_path, password, output_file_name, word_options)
```
## 3.9 OCR

#### **Overview**

OCR (Optical Character Recognition) is the process of converting images of typed, handwritten, or printed text into machine-encoded text.

OCR is commonly used for text recognition and extraction from the following types of documents:

- Non-editable scanned PDF files
- Photographs of documents.
- Scene photos such as advertising layouts, signboards, etc.
- Identification cards, passports, vehicle license plates, and other official plates.
- Invoices, bills, receipts, and other financial documents.

The following features support OCR:

- PDF to Word
- PDF to Excel
- PDF to PowerPoint (PPT)
- PDF to HTML
- PDF to Rich Text Format (RTF)
- PDF to Text (TXT)
- PDF to CSV
- PDF to Searchable PDF
- PDF to OFD
- Extract PDF to JSON
- Extract PDF to Markdown


OCR Language Support of PDFSolid Conversion SDK:

| Script / Notes | Language (Native)                           | Language (In English)       |
| -------------- | ------------------------------ | ---------------------- |
| Latn; American | English                        | English               |
| Latn; Canadian | Français canadien              | French                |
| Hans/Hant      | 中文简体                       | Chinese (Simplified)  |
| Hans/Hant      | 中文繁体                       | Chinese (Traditional) |
| Jpan           | 日本語                         | Japanese              |
| Kore           | 한국어                         | Korean                |
| Latn           | Deutsch                        | German              |
| Latn           | Српски (латиница)              | Serbian (latin)       |
| Latn           | Occitan, lenga d'òc, provençal | Occitan               |
| Latn           | Dansk                          | Danish                |
| Latn           | Italiano                       | Italian               |
| Latn; European | Español                        | Spanish               |
| Latn; European | Português (Portugal)           | Portuguese            |
| Latn           | Te reo Māori                   | Maori                 |
| Latn           | Bahasa Melayu                  | Malay                 |
| Latn           | Malti                          | Maltese               |
| Latn           | Nederlands                     | Dutch                 |
| Latn; Bokmål   | Norsk                          | Norwegian             |
| Latn           | Polski                         | Polish                |
| Latn           | Română                         | Romanian              |
| Latn           | Slovenčina                     | Slovak                |
| Latn           | Slovenščina                    | Slovenian             |
| Latn           | shqip                          | Albanian              |
| Latn           | Svenska                        | Swedish               |
| Latn           | Swahili                        | Swahili               |
| Latn           | Wikang Tagalog                 | Tagalog               |
| Latn           | Türkçe                         | Turkish               |
| Latn           | oʻzbekcha                      | Uzbek                 |
| Latn           | Tiếng Việt                     | Vietnamese            |
| Latn           | Afrikaans                      | Afrikaans             |
| Latn           | Azərbaycan                     | Azerbaijani           |
| Latn           | Bosanski                       | Bosnian               |
| Latn           | Čeština                        | Czech                 |
| Latn           | Cymraeg                        | Welsh                 |
| Latn           | Eesti keel                     | Estonian              |
| Latn           | Gaeilge                        | Irish                 |
| Latn           | Hrvatski                       | Croatian              |
| Latn           | Magyar                         | Hungarian             |
| Latn           | Bahasa Indonesia               | Indonesian            |
| Latn           | Íslenska                       | Icelandic             |
| Latn           | Kurdî                          | Kurdish               |
| Latn           | Lietuvių                       | Lithuanian            |
| Latn           | Latviešu                       | Latvian               |

#### **Set OCR Language**

In the current mainline version, OCR languages should be passed through the `languages` for each conversion task, rather than through a separate global interface.

```python
input_file_path = "***"
password = "***"
output_file_name = "***"

word_options = ConvertOptions()
word_options.enable_ocr = True
word_options.languages = [OCRLanguage.ENGLISH]
error = CPDFConversion.start_pdf_to_word(input_file_path, password, output_file_name, word_options)
```

#### **OCR Options**
Different OCR options can be selected according to actual needs. Below are the currently supported OCR options.

- **INVALID_CHARACTER:** Recognizes invalid or garbled characters in the PDF document through OCR, while normal characters are not processed by OCR.
- **SCAN_PAGE:** Recognizes scanned pages in the PDF document through OCR, while editable pages are not processed by OCR.
- **INVALID_CHARACTER_AND_SCAN_PAGE:** Recognizes both invalid characters and scanned pages in the PDF document through OCR.
- **ALL:** Recognizes all pages and characters in the PDF document through OCR.

#### **Preserve Page Background**
When OCR is enabled, you can choose whether to enable the `contain_page_background_image` option. If this option is enabled, the original page background image of the PDF will be preserved. If it is disabled, the image result detected during page layout analysis will be retained.

#### **Notice**

- The quality of the OCR result depends on the quality of the input image. If the input image has a low resolution, the OCR result quality will be affected. A good rule of thumb is that the more pixels in the character shapes, the better. If the character bounding box is smaller than 20x20 pixels, OCR quality will drop exponentially. The ideal image is a grayscale image with a resolution around 300 DPI.
- When performing OCR, make sure the OCR language setting matches the language in the PDF document to achieve the best OCR conversion quality.
- OCR functionality is currently not supported on operating systems lower than Windows 10.


#### **Convert Images to Other Document Formats**

The OCR function also supports converting input images into Word, Excel, PPT, HTML, CSV, RTF, TXT, JSON, and other formats. This sample demonstrates how to use the PDFSolid OCR function to convert image files to a DOCX file.

```python
input_file_path = "***"
password = "***"
output_file_name = "***"

word_options = ConvertOptions()
word_options.enable_ocr = True
word_options.languages = [OCRLanguage.ENGLISH]
error = CPDFConversion.start_pdf_to_word(input_file_path, password, output_file_name, word_options)
```

For the output page size of image input, keeping the original image when OCR is disabled, and similar behavior, see "Image Input" in [3.19 Convert PDF to Image](#319-convert-pdf-to-image).

#### **Sample**

This Sample demonstrates how to use the PDFSolid OCR function to convert a PDF to DOCX file.

```python
input_file_path = "***"
password = "***"
output_file_name = "***"

word_options = ConvertOptions()
word_options.enable_ocr = True
word_options.languages = [OCRLanguage.ENGLISH]
error = CPDFConversion.start_pdf_to_word(input_file_path, password, output_file_name, word_options)
```
## 3.10 Layout Analysis

#### **Overview**

Layout analysis is the process of leveraging Artificial Intelligence (AI) technology to parse and understand the structure of a document's layout. Its primary goal is to extract text, images, tables, layers, and other data from the input documents.

Layout analysis has several common use cases, including:

- **Intelligent recognition of tables within PDF documents**: This feature is particularly useful for analyzing company financial statements, invoices, bank statements, experimental data, medical test reports, and more.
- **Smart extraction of text, images, or tables from PDF documents through layout analysis**: This functionality greatly aids in the analysis and extraction of information from identification cards, receipts, licenses, documents, ancient books, and other various types of files.

Features that support Layout Analysis:

- PDF to Word
- PDF to Excel
- PDF to PowerPoint (PPT)
- PDF to HTML
- PDF to RTF
- PDF to TXT
- PDF to CSV
- Extract PDF to JSON
- Extract PDF to Markdown

#### **Notice**

- You need to load the DocumentAI model (see [3.2 Set DocumentAI Model](#32-set-documentai-model)) before using layout analysis, **or** plug in your own layout model through the callbacks described in [3.12 Use Custom AI Models via Callbacks](#312-use-custom-ai-models-via-callbacks).
- When OCR is enabled, layout analysis is automatically enabled.
- AI table recognition is a separate stage controlled by `enable_ai_table_recognition`. See [3.11 Table Recognition](#311-table-recognition).

#### **Sample**

This Sample demonstrates how to use the PDFSolid OCR function to convert PDF to DOCX file.

```python
input_file_path = "***"
password = "***"
output_file_name = "***"

word_options = ConvertOptions()
word_options.enable_ai_layout = True
error = CPDFConversion.start_pdf_to_word(input_file_path, password, output_file_name, word_options)
```
## 3.11 Table Recognition

#### **Overview**

Table Recognition reconstructs the internal structure of tables detected during layout analysis, including rows, columns, merged cells, and cell boundaries, so that the converted document preserves the original tabular semantics instead of producing a flat grid of text fragments.

It is controlled by the independent option `enable_ai_table_recognition`, which is **enabled by default**. The table model is only invoked for table regions reported by layout analysis whose detection confidence is below the trusted threshold; high-confidence native PDF tables bypass the model to save inference time.

Typical scenarios that benefit from Table Recognition:

- **Borderless or partially bordered tables**, where ruling lines alone cannot describe the structure.
- **Tables with merged header cells, multi-row headers, or spanning cells**, such as financial statements, lab reports, and invoices.
- **Scanned tables processed by OCR**, where geometric reconstruction is required before cell-level data extraction.

Features that support Table Recognition:

- PDF to Word
- PDF to Excel
- PDF to PowerPoint (PPT)
- PDF to HTML
- PDF to RTF
- PDF to CSV
- Extract PDF to JSON
- Extract PDF to Markdown

#### **Notice**

- Table Recognition runs only when layout analysis is active (i.e. `enable_ai_layout` is enabled, or implicitly when `enable_ocr` is enabled).
- You need to load the DocumentAI model before using Table Recognition, **or** plug in your own table model via the callbacks described in [3.12 Use Custom AI Models via Callbacks](#312-use-custom-ai-models-via-callbacks).
- Disabling `enable_ai_table_recognition` turns the table model off entirely; detected table regions then fall back to geometric reconstruction from the underlying page objects.

#### **Sample**

This sample demonstrates how to convert a PDF to a Word document with Table Recognition enabled.

```python
LibraryManager.set_document_ai_model("path/documentai.model", -1)

word_options = ConvertOptions()
word_options.enable_ai_layout = True
word_options.enable_ai_table_recognition = True  # enabled by default in 4.1
CPDFConversion.start_pdf_to_word("input.pdf", "password", "path/output.docx", word_options)
```

#### **Table Recognition Model Profile**

`ConvertOptions.table_recognition_accuracy` selects the table recognition model profile for each conversion task:

| Value | Meaning |
| --- | --- |
| `TableRecognitionAccuracy.HIGH_ACCURACY` | Prioritizes recognition accuracy and may use more resources. **The default behavior of 1.2.0.** |
| `TableRecognitionAccuracy.BALANCED` | Balances recognition accuracy, resource usage, and throughput. **The default since 1.3.0.** |

- **Since 1.3.0 the default profile changes from high accuracy to balanced.** Without any code change, the table recognition results and resource usage differ from 1.2.0. To keep the 1.2.0 behavior, explicitly select `HIGH_ACCURACY`.
- The resources required by the balanced profile are included in `documentai.model`, which ships with the SDK package; no additional download is needed. The high-accuracy profile also requires the table extension package `table_legacy.model` to be loaded (see [Model Package Description](#model-package-description)).
- Models of both profiles can be loaded at the same time; each conversion task uses the one given by its `table_recognition_accuracy`.
- If the requested profile has no corresponding model (for example, the high-accuracy profile without `table_legacy.model`), the conversion still succeeds, but tables are recognized with the rule-based method instead, so the result differs from that profile.
- The profile names do not guarantee better results for every document.

```python
# Windows and macOS; on Linux import from PdfSolidConversion instead.
from PDFSolidConversion import *

LibraryManager.set_document_ai_model("path/documentai.model", -1)
LibraryManager.set_document_ai_model("path/table_legacy.model", -1)

word_options = ConvertOptions()
word_options.enable_ai_layout = True
word_options.table_recognition_accuracy = TableRecognitionAccuracy.HIGH_ACCURACY
CPDFConversion.start_pdf_to_word("input.pdf", "password", "path/output.docx", word_options)
```
## 3.12 Use Custom AI Models via Callbacks

#### **Overview**

Starting with **SDK v1.1.0**, PDFSolid Conversion SDK exposes a callback-based extension point that lets you plug in your own AI inference engine for OCR, Layout Analysis, and Table Recognition. Instead of relying on the built-in DocumentAI model loaded by `set_document_ai_model`, you can:

- Run inference with any model or runtime you choose (e.g. your in-house engine, PaddleOCR, a cloud OCR API).
- Return the result to the SDK as a JSON string with a well-defined schema.

When the relevant callback pair is registered on `ConvertCallback`, the SDK skips its built-in model invocation for that capability and consumes your JSON output instead. If a pair is left unset, the SDK falls back to the built-in DocumentAI model (when available).

#### **Callback Pairs**

Each AI capability uses **two callbacks**: a *trigger* (invoked by the SDK with the path to a page image saved as PNG in a temp directory) and a *result getter* (invoked by the SDK immediately afterwards to retrieve the JSON string).

| Capability         | Trigger field / setter             | Result getter field / setter                | Triggered when                                                                              |
| ------------------ | ---------------------------------- | ------------------------------------------- | ------------------------------------------------------------------------------------------- |
| OCR                | `ocr`                              | `get_ocr_result`                            | OCR is enabled                                                                              |
| Layout Analysis    | `layout`                           | `get_layout_result`                         | layout analysis is enabled (or implicitly when OCR is enabled)                              |
| Table Recognition  | `table`                            | `get_table_result`                          | table recognition is enabled **and** a table region is detected by layout analysis          |

Rules:

- The trigger receives a UTF-8 path to a PNG file. Return `true` if your inference succeeded, `false` to make the SDK ignore the result for that page.
- The getter must return a UTF-8 JSON string. The SDK copies the string into an internal buffer before consuming it.
- Both callbacks for a capability must be set together. If only one is provided, the SDK falls back to the built-in path.
- Coordinates in your JSON must be in the **pixel space of the image the trigger received** (top-left origin, X right, Y down).
- Confidence filtering: OCR spans with `confidence < 0.1` and layout objects with `confidence < 0.45` are discarded by the SDK.
- When all three capabilities you need are covered by your own callbacks, `set_document_ai_model` does not have to be called.

#### **Sample**

```python
def on_ocr(image_path: str) -> bool:
    # Run your OCR engine on `image_path`, cache the JSON result.
    return True

def get_ocr_result() -> str:
    return ""  # return UTF-8 JSON

def on_layout(image_path: str) -> bool:
    # Run your layout engine on `image_path`.
    return True

def get_layout_result() -> str:
    return ""  # return UTF-8 JSON

def on_table(image_path: str) -> bool:
    # Run your table engine on `image_path`.
    return True

def get_table_result() -> str:
    return ""  # return UTF-8 JSON

callback = ConvertCallback()
callback.set_ocr(on_ocr)
callback.set_get_ocr_result(get_ocr_result)
callback.set_layout(on_layout)
callback.set_get_layout_result(get_layout_result)
callback.set_table(on_table)
callback.set_get_table_result(get_table_result)

word_options = ConvertOptions()
word_options.enable_ocr = True
word_options.enable_ai_layout = True
word_options.enable_ai_table_recognition = True
CPDFConversion.start_pdf_to_word("input.pdf", "password", "path/output.docx", word_options, callback)
```

#### **JSON Schemas**

##### **OCR Result JSON Schema**

Returned by `get_ocr_result`. The SDK populates each `text_spans[].chars[]` either from `words[]` if provided, or by uniformly splitting the span rect.

```json
{
  "text_spans": [
    {
      "text": "Hello World",
      "confidence": 0.98,
      "rotation": 0.0,
      "rect": { "left": 120, "top": 80, "right": 320, "bottom": 110 },
      "style": {
        "font_size": 18.0,
        "font_color": { "r": 0, "g": 0, "b": 0 }
      },
      "words": [
        { "text": "Hello", "rect": { "left": 120, "top": 80, "right": 200, "bottom": 110 } },
        { "text": "World", "rect": { "left": 210, "top": 80, "right": 320, "bottom": 110 } }
      ]
    }
  ]
}
```

| Field | Type | Required | Description |
| ----- | ---- | -------- | ----------- |
| `text_spans` | array | Yes | Recognized text spans on the page. |
| `text` | string | Yes | UTF-8 text content of the span. |
| `confidence` | number | No | 0.0 – 1.0. Spans below 0.1 are discarded. |
| `rotation` | number | No | Text rotation in degrees. Default 0. |
| `rect` | object | Yes | Bounding box in image pixels (`left`/`top`/`right`/`bottom`). |
| `style.font_size` | number | No | Estimated font size in pixels. |
| `style.font_color` | object | No | `{ r, g, b }` 0 – 255. |
| `words` | array | No | Per-word boxes. If omitted, the SDK splits the span rect evenly. Strongly recommended for CJK + Latin mixed lines for correct glyph spacing. |

##### **Layout Analysis Result JSON Schema**

Returned by `get_layout_result`. Objects with `confidence < 0.45` are discarded.

```json
{
  "objects": [
    { "type": "title", "confidence": 0.95, "rect": { "left": 60, "top": 50, "right": 540, "bottom": 90 } },
    { "type": "paragraph", "confidence": 0.97, "rect": { "left": 60, "top": 100, "right": 540, "bottom": 220 } },
    { "type": "figure", "confidence": 0.92, "rect": { "left": 80, "top": 240, "right": 520, "bottom": 460 } },
    { "type": "table", "confidence": 0.93, "rect": { "left": 60, "top": 480, "right": 540, "bottom": 700 } }
  ]
}
```

Supported `type` values:

| Value | Meaning |
| ----- | ------- |
| `paragraph` | Body text paragraph |
| `title` | Heading |
| `figure` | Image or figure |
| `figure_title` | Figure caption header |
| `figure_caption` | Figure caption text |
| `table` | Table region. Whether the table is bordered or borderless is determined by the table recognition stage, not by the layout label. |
| `table_title` | Table caption header |
| `table_caption` | Table caption text |
| `ordered_list` | Ordered list |
| `unordered_list` | Unordered list |
| `catalogue` | Table of contents |
| `formula` | Math formula |
| `code` | Code block |
| `algorithm` | Algorithm block |
| `header` | Page header |
| `footer` | Page footer |
| `page_number` | Page number |
| `reference` | Reference or citation |

Objects with a `type` value that is not listed above are ignored. Use the values in this table as the canonical layout labels in your custom output.

##### **Table Recognition Result JSON Schema**

Returned by `get_table_result` once per detected table region. Polygons use 8 integers `[x0, y0, x1, y1, x2, y2, x3, y3]` in the order top-left, top-right, bottom-right, bottom-left.

```json
{
  "type": "table_with_line",
  "position": [60, 480, 540, 480, 540, 700, 60, 700],
  "rows": 3,
  "cols": 2,
  "angle": 0.0,
  "height_of_rows": [40, 60, 60],
  "width_of_cols": [200, 280],
  "table_cells": [
    {
      "start_row": 0,
      "end_row": 0,
      "start_col": 0,
      "end_col": 0,
      "cell_background_color_r": 240,
      "cell_background_color_g": 240,
      "cell_background_color_b": 240,
      "position": [60, 480, 260, 480, 260, 520, 60, 520]
    }
  ]
}
```

| Field | Type | Description |
| ----- | ---- | ----------- |
| `type` | string | `table_with_line` for bordered tables; any other value is treated as a non-standard (borderless) table. |
| `position` | int[8] | Table polygon in image pixels. |
| `rows` / `cols` | int | Row / column counts. |
| `angle` | number | Skew angle in degrees. |
| `height_of_rows` | int[] | Per-row pixel heights (length = `rows`). |
| `width_of_cols` | int[] | Per-column pixel widths (length = `cols`). |
| `table_cells[]` | array | One entry per merged cell. |
| `start_row` / `end_row` | int | Inclusive row span of the cell. |
| `start_col` / `end_col` | int | Inclusive column span of the cell. |
| `cell_background_color_*` | int | Cell background color components (0 – 255). |
| `position` | int[8] | Cell polygon in image pixels. |

##### **Tip: Validate Your JSON**

If you need a reference output to compare against, run a conversion once with the built-in DocumentAI model. The SDK uses the same JSON shape internally, so your custom output should follow the same structure.

## 3.13 Output Font Option

#### **Overview**

In some output formats, you can set the preferred font name to unify the default font style in the output document.

#### **Supported Formats**

The `font_name` option currently applies to the following formats:

- PDF to Word
- PDF to Excel
- PDF to PowerPoint
- PDF to Searchable PDF
- PDF to OFD

#### **Example**

The following example demonstrates how to set the preferred font name for the output document.

```python
input_file_path = "***"
password = "***"
output_file_name = "***"

word_options = ConvertOptions()
word_options.font_name = "Arial"
error = CPDFConversion.start_pdf_to_word(input_file_path, password, output_file_name, word_options)
```
## 3.14 Convert PDF to Word

#### **Overview**

Converting PDF to Word is an operation that converts a PDF file into an editable Word file. By converting PDF to Word, you can easily edit, modify, insert, or delete text and images, and adjust layout and properties.

#### **Conversion Options**

This format uses only the following options of `ConvertOptions`; the other options have no effect:

| Option | Default | Meaning |
| --- | --- | --- |
| `enable_ai_layout` | `True` | Uses AI layout analysis to recognize paragraphs, tables, images, headers and footers, and formulas; when off, rule-based layout analysis is used. Ignored if the license does not include AI layout analysis. |
| `enable_ai_table_recognition` | `True` | Recognizes the structure of tables with the table model; when off, the table structure is rebuilt from the ruling lines. Only applies to tables found by AI layout analysis (`enable_ai_layout` on). |
| `table_recognition_accuracy` | `TableRecognitionAccuracy.BALANCED` | Table model: `TableRecognitionAccuracy.BALANCED` uses the base documentai.model, `TableRecognitionAccuracy.HIGH_ACCURACY` uses the table_legacy.model package. Only takes effect when AI table recognition runs with the built-in table model. If the model of the requested accuracy is not loaded, the conversion still succeeds and tables fall back to rule-based recognition. |
| `contain_image` | `True` | Keeps the images and vector graphics (output as pictures) of the source; when off, they are not output. |
| `contain_page_background_image` | `True` | On pages recognized by OCR, places the page image with the recognized text erased as a background behind the text, instead of separate image crops. Only takes effect when `enable_ocr` and `contain_image` are on. |
| `contain_annotation` | `True` | Outputs the appearance of annotations as images. Only for PDF pages that are not recognized by OCR. |
| `enable_ocr` | `False` | Recognizes text with OCR on the pages chosen by `ocr_option`. Ignored if the license does not include OCR. |
| `ocr_option` | `OCROption.ALL` | Which content OCR handles: `OCROption.ALL` every page; `OCROption.SCAN_PAGE` only image (scanned) pages; `OCROption.INVALID_CHARACTER` re-recognizes unreadable characters on the other pages; `OCROption.INVALID_CHARACTER_AND_SCAN_PAGE` both. Only takes effect when `enable_ocr` is on. |
| `languages` | `[]` | OCR recognition languages; the first language is also the language of the Word document. When no language is given, English is used. Only takes effect when `enable_ocr` is on. |
| `enable_document_orientation_classification` | `False` | Detects the page rotation and turns the page image upright before OCR. Only takes effect when `enable_ocr` is on. |
| `enable_document_dewarp` | `False` | Flattens curved or warped page photos before OCR. Only takes effect when `enable_ocr` is on. |
| `formula_to_image` | `True` | Outputs formulas as pictures; when off, as editable text. Only applies to formulas found by AI layout analysis (`enable_ai_layout` on). |
| `font_name` | Empty | Uses the given font for all text, e.g. "Arial"; empty selects fonts automatically. Silently ignored if the font is neither embedded in the PDF nor installed on the system. |
| `page_layout_mode` | `PageLayoutMode.FLOW` | `PageLayoutMode.FLOW`: content is laid out as flowing paragraphs; `PageLayoutMode.BOX`: each region is placed in its own positioned frame. |
| `output_document_per_page` | `False` | Writes one file per page instead of one document. |
| `page_ranges` | Empty | Pages to convert, e.g. "1-3,5,7-9"; empty converts every page. For multi-frame image input it selects the frames. |
| `enable_auto_page_size` | `False` | Image input only: sizes the page from the image resolution, matched to the nearest standard paper size; when off, one image pixel becomes one point. |
| `custom_page_width` / `custom_page_height` | `0` | Image input only: exact page width and height in points (1 pt = 1/72 inch); both must be greater than 0. Takes precedence over `enable_auto_page_size`. |

Example:

```python
options = ConvertOptions()
options.enable_ocr = True
options.ocr_option = OCROption.SCAN_PAGE
options.languages = [OCRLanguage.ENGLISH]
options.page_layout_mode = PageLayoutMode.BOX
error = CPDFConversion.start_pdf_to_word("input.pdf", "password", "path/output.docx", options)
```

#### **Layout differences**

- **Flow Layout:** Ideal for editing, with content dynamically adapting to different positions as you edit. However, a Word file may display differently because of incompatibilities across software or application versions. This makes it unsuitable for highly precise documents such as certificates or formal electronic records.
  
- **Fixed Layout:** Ensures a stable, uniform appearance and print quality across all devices. The content and formatting are locked upon creation, making alterations difficult without affecting the overall layout. It's preferred for formal documentation such as business reports and official electronic records.

#### **Sample**

This sample demonstrates how to convert from a PDF to DOCX file.

```python
input_file_path = "***"
password = "***"
output_file_name = "***"

word_options = ConvertOptions()
error = CPDFConversion.start_pdf_to_word(input_file_path, password, output_file_name, word_options)
```

#### **Convert Formulas to Images**

When a document contains complex formulas and you want to preserve visual consistency in the output document, you can enable the `formula_to_image` option.

```python
input_file_path = "***"
password = "***"
output_file_name = "***"

word_options = ConvertOptions()
  word_options.formula_to_image = True
error = CPDFConversion.start_pdf_to_word(input_file_path, password, output_file_name, word_options)
```
## 3.15 Convert PDF to Excel

#### **Overview**

PDFSolid Conversion SDK supports converting PDF documents to Microsoft Excel format (.xlsx). By extracting, parsing, and importing data from PDF into Excel, users can further edit, analyze, or share Excel files. This feature helps increase productivity, reduce manual entry errors, and simplify complex document processing tasks.

#### **Conversion Options**

This format uses only the following options of `ConvertOptions`; the other options have no effect:

| Option | Default | Meaning |
| --- | --- | --- |
| `excel_csv_format` | `False` | Must be off to output an .xlsx workbook; when on, CSV is output instead (see "PDF to CSV"). |
| `excel_worksheet_option` | `ExcelWorksheetOption.FOR_TABLE` | `ExcelWorksheetOption.FOR_TABLE`: one worksheet per table, tables only; `ExcelWorksheetOption.FOR_PAGE`: one worksheet per page; `ExcelWorksheetOption.FOR_DOCUMENT`: all content on one worksheet. Image input without OCR always uses `ExcelWorksheetOption.FOR_PAGE`. |
| `excel_all_content` | `False` | Also writes the content outside tables (text, images, headers and footers); when off, only tables are kept. Ignored with `ExcelWorksheetOption.FOR_TABLE`. |
| `enable_ai_layout` | `True` | Uses AI layout analysis to recognize paragraphs, tables, images, headers and footers, and formulas; when off, rule-based layout analysis is used. Ignored if the license does not include AI layout analysis. |
| `enable_ai_table_recognition` | `True` | Recognizes the structure of tables with the table model; when off, the table structure is rebuilt from the ruling lines. Only applies to tables found by AI layout analysis (`enable_ai_layout` on). |
| `table_recognition_accuracy` | `TableRecognitionAccuracy.BALANCED` | Table model: `TableRecognitionAccuracy.BALANCED` uses the base documentai.model, `TableRecognitionAccuracy.HIGH_ACCURACY` uses the table_legacy.model package. Only takes effect when AI table recognition runs with the built-in table model. If the model of the requested accuracy is not loaded, the conversion still succeeds and tables fall back to rule-based recognition. |
| `contain_image` | `True` | Keeps the images and vector graphics of the source. Only visible when content outside tables is written (`excel_all_content` on with `ExcelWorksheetOption.FOR_PAGE` or `ExcelWorksheetOption.FOR_DOCUMENT`); tables-only output never contains images. |
| `contain_annotation` | `True` | Outputs the appearance of annotations as images. Only for PDF pages that are not recognized by OCR, and only visible when content outside tables is written. |
| `enable_ocr` | `False` | Recognizes text with OCR on the pages chosen by `ocr_option`. Ignored if the license does not include OCR. |
| `ocr_option` | `OCROption.ALL` | Which content OCR handles: `OCROption.ALL` every page; `OCROption.SCAN_PAGE` only image (scanned) pages; `OCROption.INVALID_CHARACTER` re-recognizes unreadable characters on the other pages; `OCROption.INVALID_CHARACTER_AND_SCAN_PAGE` both. Only takes effect when `enable_ocr` is on. |
| `languages` | `[]` | OCR recognition languages; when no language is given, English is used. Only takes effect when `enable_ocr` is on. |
| `enable_document_orientation_classification` | `False` | Detects the page rotation and turns the page image upright before OCR. Only takes effect when `enable_ocr` is on. |
| `enable_document_dewarp` | `False` | Flattens curved or warped page photos before OCR. Only takes effect when `enable_ocr` is on. |
| `formula_to_image` | `True` | Outputs formulas as pictures; when off, as text. Only applies to formulas found by AI layout analysis, and only visible when content outside tables is written. |
| `font_name` | Empty | Uses the given font for all text, e.g. "Arial"; empty selects fonts automatically. Silently ignored if the font is neither embedded in the PDF nor installed on the system. |
| `output_document_per_page` | `False` | Writes one workbook per page instead of one workbook. |
| `page_ranges` | Empty | Pages to convert, e.g. "1-3,5,7-9"; empty converts every page. For multi-frame image input it selects the frames. |
| `enable_auto_page_size` | `False` | Image input only: sizes the page from the image resolution, matched to the nearest standard paper size; when off, one image pixel becomes one point. |
| `custom_page_width` / `custom_page_height` | `0` | Image input only: exact page width and height in points (1 pt = 1/72 inch); both must be greater than 0. Takes precedence over `enable_auto_page_size`. |

Example:

```python
options = ConvertOptions()
options.excel_worksheet_option = ExcelWorksheetOption.FOR_PAGE
options.excel_all_content = True
options.page_ranges = "1-3"
error = CPDFConversion.start_pdf_to_excel("input.pdf", "password", "path/output.xlsx", options)
```

#### **Set the content options for Excel**

When converting PDF files to Excel files, you need to pay attention to the settings of the following options, which will directly affect the content written to the Excel file.

- Content options:

  If you set the `all_content` option, the converted XLSX file will contain all content in the PDF.

- Worksheet options:

| Option | Description |
| --- | --- |
| `FOR_TABLE` | Create one sheet per table. |
| `FOR_PAGE` | Create one sheet per page. |
| `FOR_DOCUMENT` | Create one sheet for the entire document. |


#### **Sample**

This sample demonstrates how to convert from a PDF to XLSX file.

```python
input_file_path = "***"
password = "***"
output_file_name = "***"

excel_options = ConvertOptions()
error = CPDFConversion.start_pdf_to_excel(input_file_path, password, output_file_name, excel_options)
```
## 3.16 Convert PDF to PowerPoint

#### **Overview**

PDFSolid Conversion SDK provides the function of converting PDF files to PowerPoint files and restoring the layout and format of the original document, which can meet the needs of users for the presentation and editing of document content in Microsoft PowerPoint.

#### **Conversion Options**

This format uses only the following options of `ConvertOptions`; the other options have no effect:

| Option | Default | Meaning |
| --- | --- | --- |
| `enable_ai_layout` | `True` | Uses AI layout analysis to recognize paragraphs, tables, images, headers and footers, and formulas; when off, rule-based layout analysis is used. Ignored if the license does not include AI layout analysis. |
| `enable_ai_table_recognition` | `True` | Recognizes the structure of tables with the table model; when off, the table structure is rebuilt from the ruling lines. Only applies to tables found by AI layout analysis (`enable_ai_layout` on). |
| `table_recognition_accuracy` | `TableRecognitionAccuracy.BALANCED` | Table model: `TableRecognitionAccuracy.BALANCED` uses the base documentai.model, `TableRecognitionAccuracy.HIGH_ACCURACY` uses the table_legacy.model package. Only takes effect when AI table recognition runs with the built-in table model. If the model of the requested accuracy is not loaded, the conversion still succeeds and tables fall back to rule-based recognition. |
| `contain_image` | `True` | Keeps the images and vector graphics (output as pictures) of the source; when off, they are not output. |
| `contain_page_background_image` | `True` | On pages recognized by OCR, outputs the page image with the recognized text erased as a page-sized background, instead of separate image crops; headers and footers found by AI layout analysis are not output separately. Only takes effect when `enable_ocr` and `contain_image` are on. |
| `contain_annotation` | `True` | Outputs the appearance of annotations as images. Only for PDF pages that are not recognized by OCR. |
| `enable_ocr` | `False` | Recognizes text with OCR on the pages chosen by `ocr_option`. Ignored if the license does not include OCR. |
| `ocr_option` | `OCROption.ALL` | Which content OCR handles: `OCROption.ALL` every page; `OCROption.SCAN_PAGE` only image (scanned) pages; `OCROption.INVALID_CHARACTER` re-recognizes unreadable characters on the other pages; `OCROption.INVALID_CHARACTER_AND_SCAN_PAGE` both. Only takes effect when `enable_ocr` is on. |
| `languages` | `[]` | OCR recognition languages; when no language is given, English is used. Only takes effect when `enable_ocr` is on. |
| `enable_document_orientation_classification` | `False` | Detects the page rotation and turns the page image upright before OCR. Only takes effect when `enable_ocr` is on. |
| `enable_document_dewarp` | `False` | Flattens curved or warped page photos before OCR. Only takes effect when `enable_ocr` is on. |
| `formula_to_image` | `True` | Outputs formulas as pictures; when off, as editable text. Only applies to formulas found by AI layout analysis (`enable_ai_layout` on). |
| `font_name` | Empty | Uses the given font for all text, e.g. "Arial"; empty selects fonts automatically. Silently ignored if the font is neither embedded in the PDF nor installed on the system. |
| `output_document_per_page` | `False` | Writes one file per page instead of one document. |
| `page_ranges` | Empty | Pages to convert, e.g. "1-3,5,7-9"; empty converts every page. For multi-frame image input it selects the frames. |
| `enable_auto_page_size` | `False` | Image input only: sizes the slide from the image resolution, matched to the nearest standard paper size; when off, one image pixel becomes one point. |
| `custom_page_width` / `custom_page_height` | `0` | Image input only: exact page width and height in points (1 pt = 1/72 inch); both must be greater than 0. Takes precedence over `enable_auto_page_size`. |

Example:

```python
options = ConvertOptions()
options.contain_annotation = False
options.font_name = "Arial"
options.output_document_per_page = True
error = CPDFConversion.start_pdf_to_ppt("input.pdf", "password", "path/output.pptx", options)
```

#### **Sample**

This sample demonstrates how to convert from a PDF to PPTX file.

```python
input_file_path = "***"
password = "***"
output_file_name = "***"

ppt_options = ConvertOptions()
error = CPDFConversion.start_pdf_to_ppt(input_file_path, password, output_file_name, ppt_options)
```
## 3.17 Convert PDF to HTML

#### **Overview**

PDFSolid Conversion SDK provides the PDF to HTML function, which can convert PDF files to HTML files while maintaining the layout and format of the original document, allowing users to browse and view the document on Web.

#### **Conversion Options**

This format uses only the following options of `ConvertOptions`; the other options have no effect:

| Option | Default | Meaning |
| --- | --- | --- |
| `html_option` | `HtmlOption.SINGLE_PAGE` | `HtmlOption.SINGLE_PAGE`: one HTML file; `HtmlOption.SINGLE_PAGE_WITH_BOOKMARK`: one HTML file with an outline navigation; `HtmlOption.MULTIPLE_PAGE`: one HTML file per page; `HtmlOption.MULTIPLE_PAGE_WITH_BOOKMARK`: one HTML file per page with an outline navigation and previous/next links. The navigation is only generated when the PDF has an outline. |
| `page_layout_mode` | `PageLayoutMode.FLOW` | `PageLayoutMode.FLOW`: flowing HTML; `PageLayoutMode.BOX`: absolutely positioned blocks. |
| `enable_ai_layout` | `True` | Uses AI layout analysis to recognize paragraphs, tables, images, headers and footers, and formulas; when off, rule-based layout analysis is used. Ignored if the license does not include AI layout analysis. |
| `enable_ai_table_recognition` | `True` | Recognizes the structure of tables with the table model; when off, the table structure is rebuilt from the ruling lines. Only applies to tables found by AI layout analysis (`enable_ai_layout` on). |
| `table_recognition_accuracy` | `TableRecognitionAccuracy.BALANCED` | Table model: `TableRecognitionAccuracy.BALANCED` uses the base documentai.model, `TableRecognitionAccuracy.HIGH_ACCURACY` uses the table_legacy.model package. Only takes effect when AI table recognition runs with the built-in table model. If the model of the requested accuracy is not loaded, the conversion still succeeds and tables fall back to rule-based recognition. |
| `contain_image` | `True` | Keeps the images and vector graphics of the source (written to the resource folder next to the HTML file); when off, they are not output. |
| `contain_page_background_image` | `True` | On pages recognized by OCR, outputs the page image with the recognized text erased as a page-sized background, instead of separate image crops; headers and footers found by AI layout analysis are not output separately. Only takes effect when `enable_ocr` and `contain_image` are on. |
| `contain_annotation` | `True` | Outputs the appearance of annotations as images. Only for PDF pages that are not recognized by OCR. |
| `enable_ocr` | `False` | Recognizes text with OCR on the pages chosen by `ocr_option`. Ignored if the license does not include OCR. |
| `ocr_option` | `OCROption.ALL` | Which content OCR handles: `OCROption.ALL` every page; `OCROption.SCAN_PAGE` only image (scanned) pages; `OCROption.INVALID_CHARACTER` re-recognizes unreadable characters on the other pages; `OCROption.INVALID_CHARACTER_AND_SCAN_PAGE` both. Only takes effect when `enable_ocr` is on. |
| `languages` | `[]` | OCR recognition languages; when no language is given, English is used. Only takes effect when `enable_ocr` is on. |
| `enable_document_orientation_classification` | `False` | Detects the page rotation and turns the page image upright before OCR. Only takes effect when `enable_ocr` is on. |
| `enable_document_dewarp` | `False` | Flattens curved or warped page photos before OCR. Only takes effect when `enable_ocr` is on. |
| `formula_to_image` | `True` | Outputs formulas as pictures; when off, as editable text. Only applies to formulas found by AI layout analysis (`enable_ai_layout` on). |
| `output_document_per_page` | `False` | Runs a separate HTML conversion for each page. |
| `page_ranges` | Empty | Pages to convert, e.g. "1-3,5,7-9"; empty converts every page. For multi-frame image input it selects the frames. |
| `enable_auto_page_size` | `False` | Image input only: sizes the page from the image resolution, matched to the nearest standard paper size; when off, one image pixel becomes one point. |
| `custom_page_width` / `custom_page_height` | `0` | Image input only: exact page width and height in points (1 pt = 1/72 inch); both must be greater than 0. Takes precedence over `enable_auto_page_size`. |

Example:

```python
options = ConvertOptions()
options.html_option = HtmlOption.MULTIPLE_PAGE_WITH_BOOKMARK
options.page_layout_mode = PageLayoutMode.BOX
error = CPDFConversion.start_pdf_to_html("input.pdf", "password", "path/output.html", options)
```

#### **Notice**

When converting PDF to HTML format, PDFSolid Conversion SDK provides the following four options to create HTML files:

| Option | Description |
| --- | --- |
| `SINGLE_PAGE` | Convert the entire PDF file into a single HTML file, where all PDF pages are connected in sequence by page number, displayed on the same HTML page. |
| `SINGLE_PAGE_WITH_BOOKMARK` | Convert the PDF file into a single HTML file with all PDF page content on the same page in sequential order. This option also adds a bookmark navigation bar to the HTML page for quick navigation to a specific page. |
| `MULTIPLE_PAGE` | Convert the PDF file into multiple HTML files. Each HTML file corresponds to a PDF page, and users can navigate to the next page via a link at the bottom of the page. |
| `MULTIPLE_PAGE_WITH_BOOKMARK` | Convert the PDF file into multiple HTML files, each corresponding to a PDF page. An outline HTML page is provided for navigation, allowing users to jump to the corresponding HTML page by clicking the outline. |


#### **Sample**

This sample demonstrates how to convert from a PDF to HTML file.

```python
input_file_path = "***"
password = "***"
output_file_name = "***"

html_options = ConvertOptions()
error = CPDFConversion.start_pdf_to_html(input_file_path, password, output_file_name, html_options)
```
## 3.18 Convert PDF to CSV

#### **Overview**

PDFSolid Conversion SDK supports converting PDF documents to CSV (Comma-Separated Values). Converting PDF to CSV is a common need, usually used to extract tabular or structured data from PDF documents and convert it into CSV files.

#### **Conversion Options**

This format uses only the following options of `ConvertOptions`; the other options have no effect:

| Option | Default | Meaning |
| --- | --- | --- |
| `excel_csv_format` | `False` | Must be on to output CSV. Only tables are exported. |
| `excel_worksheet_option` | `ExcelWorksheetOption.FOR_TABLE` | `ExcelWorksheetOption.FOR_TABLE`: one CSV file per table; `ExcelWorksheetOption.FOR_PAGE`: one CSV file per page; `ExcelWorksheetOption.FOR_DOCUMENT`: one CSV file with all tables, written to the output path. |
| `auto_create_folder` | `True` | With `ExcelWorksheetOption.FOR_TABLE` or `ExcelWorksheetOption.FOR_PAGE`, when the output path is an existing folder, the CSV files are put in a new subfolder named after the input file; when off, they are written directly into that folder. If the output path is not an existing folder, a folder is created at that path. |
| `enable_ai_layout` | `True` | Finds tables (including tables without borders) with AI layout analysis; when off, only tables with ruling lines are found. Ignored if the license does not include AI layout analysis. |
| `enable_ai_table_recognition` | `True` | Recognizes the structure of tables with the table model; when off, the table structure is rebuilt from the ruling lines. Only applies to tables found by AI layout analysis (`enable_ai_layout` on). |
| `table_recognition_accuracy` | `TableRecognitionAccuracy.BALANCED` | Table model: `TableRecognitionAccuracy.BALANCED` uses the base documentai.model, `TableRecognitionAccuracy.HIGH_ACCURACY` uses the table_legacy.model package. Only takes effect when AI table recognition runs with the built-in table model. If the model of the requested accuracy is not loaded, the conversion still succeeds and tables fall back to rule-based recognition. |
| `enable_ocr` | `False` | Recognizes text with OCR on the pages chosen by `ocr_option`. Required for image input; without it the conversion returns `ErrorCode.UNSUPPORTED_FEATURE`. Ignored if the license does not include OCR. |
| `ocr_option` | `OCROption.ALL` | Which content OCR handles: `OCROption.ALL` every page; `OCROption.SCAN_PAGE` only image (scanned) pages; `OCROption.INVALID_CHARACTER` re-recognizes unreadable characters on the other pages; `OCROption.INVALID_CHARACTER_AND_SCAN_PAGE` both. Only takes effect when `enable_ocr` is on. |
| `languages` | `[]` | OCR recognition languages; when no language is given, English is used. Only takes effect when `enable_ocr` is on. |
| `enable_document_orientation_classification` | `False` | Detects the page rotation and turns the page image upright before OCR. Only takes effect when `enable_ocr` is on. |
| `enable_document_dewarp` | `False` | Flattens curved or warped page photos before OCR. Only takes effect when `enable_ocr` is on. |
| `output_document_per_page` | `False` | Runs a separate CSV export for each page; each export still follows `excel_worksheet_option`. |
| `page_ranges` | Empty | Pages to convert, e.g. "1-3,5,7-9"; empty converts every page. For multi-frame image input it selects the frames. |

Example:

```python
options = ConvertOptions()
options.excel_csv_format = True
options.excel_worksheet_option = ExcelWorksheetOption.FOR_TABLE
options.auto_create_folder = False
error = CPDFConversion.start_pdf_to_excel("input.pdf", "password", "path/output_folder", options)
```

#### **Set Whether to Automatically Create Folders**
When multiple CSV files may be output, you can control whether to automatically create folders to store the CSV files by setting the `auto_create_folder` option. When this option is enabled, a folder with the same name as the output file will be automatically created in the output path to store the CSV files.

#### **Sample**

This sample demonstrates how to convert from a PDF to CSV file.

```python
input_file_path = "***"
password = "***"
output_file_name = "***"

excel_options = ConvertOptions()
excel_options.csvFormat = True
error = CPDFConversion.start_pdf_to_excel(input_file_path, password, output_file_name, excel_options)
```
## 3.19 Convert PDF to Image

#### **Overview**

PDFSolid Conversion SDK provides an API for converting PDFs to images. Integrate PDFSolid Conversion SDK to your apps to convert PDF into images easily. 

#### **Conversion Options**

This format uses only the following options of `ConvertOptions`; the other options have no effect:

| Option | Default | Meaning |
| --- | --- | --- |
| `image_type` | `ImageType.JPG` | Output image format and file extension. For image input, transparency is kept only for PNG, TIFF, WEBP (and JPEG 2000 where supported) and 16-bit depth only for PNG, TIFF and JPEG 2000; other formats are flattened onto white and converted to 8-bit. |
| `image_color_mode` | `ImageColorMode.COLOR` | `ImageColorMode.COLOR` keeps the color; `ImageColorMode.GRAY` converts to grayscale; `ImageColorMode.BINARY` converts to black and white. |
| `image_scaling` | `4.0` | Pixel size = page size in points × scaling for PDF input, and source pixel size × scaling for image input (a value above 1 enlarges input images). Must be greater than 0. The long side is limited to an internal maximum. |
| `image_path_enhance` | `False` | Darkens and strengthens vector lines and strokes. PDF input only. |
| `page_ranges` | Empty | Pages (or image frames) to export; empty exports every page. When one page is selected, the output path is used as the file name if it ends with the extension of the image format; when several pages are selected, the output path is used as a folder and numbered files are written into it. |

Example:

```python
options = ConvertOptions()
options.image_type = ImageType.PNG
options.image_color_mode = ImageColorMode.GRAY
options.image_scaling = 2.0
options.page_ranges = "1-3"
error = CPDFConversion.start_pdf_to_image("input.pdf", "password", "path/output", options)
```

#### **Setting Image Formats**

In PDFSolid Conversion SDK, supported image formats include:

- JPG
- JPEG
- JPEG2000
- PNG
- BMP
- TIFF
- TGA
- GIF
- WEBP

#### **Setting Image Color Modes**

Supported image color modes in PDFSolid Conversion SDK include:

- **Color:** Color mode, where the image effect is consistent with the original PDF page.
- **Gray:** Grayscale mode.
- **Binary:** Black and white mode, which applies binarization to the original effect.

#### **Setting Image Scaling**

The SDK supports setting image scaling. The default scaling is 1.0, which maintains the original PDF page size. If you want to double the image size, you can set `image_scaling` to 2.0; similarly, to reduce the image size by half, set `image_scaling` to 0.5.

#### **Enhancing Image Path Display**

The SDK supports an option called `image_path_enhance` for enhancing the display of image paths. This option can be enabled when you want to enhance the display effect of paths within the PDF page.

- Do not enable the `image_path_enhance` option (original PDF rendering effect):

  ![image-20250603162605558](image/image-20250603162605558.png)

- Enable the `image_path_enhance` option:

  ![image-20250603162651769](image/image-20250603162651769.png)

#### **Notice**

- A higher `image_scaling` value results in images with higher resolution, but it also increases memory usage and slows down the conversion.
- A higher `image_scaling` value does not necessarily equate to higher clarity; the clarity also depends on the original image resolution in the document.

#### **Sample**

This sample demonstrates how to convert from a PDF to Image file.

```python
input_file_path = "***"
password = "***"
output_file_name = "***"

image_options = ConvertOptions()
error = CPDFConversion.start_pdf_to_image(input_file_path, password, output_file_name, image_options)
```

#### **Image Input**

The image conversion interface `start_pdf_to_image` accepts both PDF files and supported image files as input, so it can also convert between image formats. Converting between images does not run OCR or layout analysis and does not depend on any AI model.

- **Multi-page TIFF:** Each selected frame produces one image, and `page_ranges` selects the frames. The frames are not merged into a multi-page TIFF.
- **Keep the original image when OCR is disabled:** When an image input is converted to a document format that can hold images, the default settings (`enable_ocr = False`, `contain_image = True`) output the complete source image as the document content, and no recognized text is generated.
- **Converting to TXT / Excel CSV:** These formats cannot hold images. If OCR is not enabled for an image input, `ErrorCode.UNSUPPORTED_FEATURE` (95) is returned; please enable OCR.

#### **Output Page Size for Image Input**

When an image input is converted to a document, the following options control the size of the output page (they take effect only for image input, not for PDF input):

| Option | Default | Meaning |
| --- | --- | --- |
| `enable_auto_page_size` | `False` | When enabled, the page size is derived from the image's own resolution and matched to the nearest standard paper size; when disabled, one image pixel corresponds to one page point |
| `custom_page_width` | `0` | Output page width in points (1 point = 1/72 inch); `0` means not specified |
| `custom_page_height` | `0` | Output page height in points |

- When `custom_page_width` and `custom_page_height` are both set, they specify the page size directly and **take precedence over `enable_auto_page_size`**. The size is used exactly as given (orientation included), and the image is scaled proportionally to fit inside the page without cropping.
- Examples: A4 is 595.28 x 841.89; JIS B5 is 515.91 x 728.50.

```python
# Size the page from the image's own resolution
options = ConvertOptions()
options.enable_auto_page_size = True
error = CPDFConversion.start_pdf_to_word("scan.jpg", "", "auto.docx", options)

# Specify the page size explicitly (A4, in points)
options = ConvertOptions()
options.custom_page_width = 595.28
options.custom_page_height = 841.89
error = CPDFConversion.start_pdf_to_word("scan.jpg", "", "a4.docx", options)
```
## 3.20 Convert PDF to RTF

#### **Overview**

RTF is a popular text format that can retain the format and style data of the text, and it is convenient for most text readers to read and write. Integrate PDFSolid Conversion SDK to convert PDFs to RTF files now.

#### **Conversion Options**

This format uses only the following options of `ConvertOptions`; the other options have no effect:

| Option | Default | Meaning |
| --- | --- | --- |
| `enable_ai_layout` | `True` | Uses AI layout analysis to recognize paragraphs, tables, images, headers and footers, and formulas; when off, rule-based layout analysis is used. Ignored if the license does not include AI layout analysis. |
| `enable_ai_table_recognition` | `True` | Recognizes the structure of tables with the table model; when off, the table structure is rebuilt from the ruling lines. Only applies to tables found by AI layout analysis (`enable_ai_layout` on). |
| `table_recognition_accuracy` | `TableRecognitionAccuracy.BALANCED` | Table model: `TableRecognitionAccuracy.BALANCED` uses the base documentai.model, `TableRecognitionAccuracy.HIGH_ACCURACY` uses the table_legacy.model package. Only takes effect when AI table recognition runs with the built-in table model. If the model of the requested accuracy is not loaded, the conversion still succeeds and tables fall back to rule-based recognition. |
| `contain_image` | `True` | Keeps the images and vector graphics (output as pictures) of the source; when off, they are not output. |
| `contain_page_background_image` | `True` | On pages recognized by OCR, outputs the page image with the recognized text erased as a page-sized background, instead of separate image crops; headers and footers found by AI layout analysis are not output separately. Only takes effect when `enable_ocr` and `contain_image` are on. |
| `contain_annotation` | `True` | Outputs the appearance of annotations as images. Only for PDF pages that are not recognized by OCR. |
| `enable_ocr` | `False` | Recognizes text with OCR on the pages chosen by `ocr_option`. Ignored if the license does not include OCR. |
| `ocr_option` | `OCROption.ALL` | Which content OCR handles: `OCROption.ALL` every page; `OCROption.SCAN_PAGE` only image (scanned) pages; `OCROption.INVALID_CHARACTER` re-recognizes unreadable characters on the other pages; `OCROption.INVALID_CHARACTER_AND_SCAN_PAGE` both. Only takes effect when `enable_ocr` is on. |
| `languages` | `[]` | OCR recognition languages; when no language is given, English is used. Only takes effect when `enable_ocr` is on. |
| `enable_document_orientation_classification` | `False` | Detects the page rotation and turns the page image upright before OCR. Only takes effect when `enable_ocr` is on. |
| `enable_document_dewarp` | `False` | Flattens curved or warped page photos before OCR. Only takes effect when `enable_ocr` is on. |
| `formula_to_image` | `True` | Outputs formulas as pictures; when off, as editable text. Only applies to formulas found by AI layout analysis (`enable_ai_layout` on). |
| `output_document_per_page` | `False` | Writes one file per page instead of one document. |
| `page_ranges` | Empty | Pages to convert, e.g. "1-3,5,7-9"; empty converts every page. For multi-frame image input it selects the frames. |
| `enable_auto_page_size` | `False` | Image input only: sizes the page from the image resolution, matched to the nearest standard paper size; when off, one image pixel becomes one point. |
| `custom_page_width` / `custom_page_height` | `0` | Image input only: exact page width and height in points (1 pt = 1/72 inch); both must be greater than 0. Takes precedence over `enable_auto_page_size`. |

Example:

```python
options = ConvertOptions()
options.contain_annotation = False
options.page_ranges = "1-3,5"
error = CPDFConversion.start_pdf_to_rtf("input.pdf", "password", "path/output.rtf", options)
```

#### **Sample**

This sample demonstrates how to convert from a PDF to RTF file.

```python
input_file_path = "***"
password = "***"
output_file_name = "***"

rtf_options = ConvertOptions()
error = CPDFConversion.start_pdf_to_rtf(input_file_path, password, output_file_name, rtf_options)
```
## 3.21 Convert PDF to TXT

#### **Overview**

When you need to extract the text content in the PDF file, in order for data analysis, text mining, information retrieval, etc. Using PDFSolid Conversion SDK, you can easily extract the text in the PDF into the TXT file.

#### **Conversion Options**

This format uses only the following options of `ConvertOptions`; the other options have no effect:

| Option | Default | Meaning |
| --- | --- | --- |
| `txt_table_format` | `True` | On: the cells of a table row are written on one line, separated by two spaces; off: each cell is written on its own line. Only matters when the document has tables. |
| `enable_ai_layout` | `True` | Uses AI layout analysis for reading order, paragraphs, lists, headers and footers, and table detection; when off, rule-based paragraphs and ruling-line tables are used. Ignored if the license does not include AI layout analysis. |
| `enable_ai_table_recognition` | `True` | Recognizes the cell structure of tables with the table model, which decides how table text is split and ordered. Only applies to tables found by AI layout analysis (`enable_ai_layout` on). |
| `table_recognition_accuracy` | `TableRecognitionAccuracy.BALANCED` | Table model: `TableRecognitionAccuracy.BALANCED` uses the base documentai.model, `TableRecognitionAccuracy.HIGH_ACCURACY` uses the table_legacy.model package. Only takes effect when AI table recognition runs with the built-in table model. If the model of the requested accuracy is not loaded, the conversion still succeeds and tables fall back to rule-based recognition. |
| `enable_ocr` | `False` | Recognizes text with OCR on the pages chosen by `ocr_option`. Required for image input; without it the conversion returns `ErrorCode.UNSUPPORTED_FEATURE`. Ignored if the license does not include OCR. |
| `ocr_option` | `OCROption.ALL` | Which content OCR handles: `OCROption.ALL` every page; `OCROption.SCAN_PAGE` only image (scanned) pages; `OCROption.INVALID_CHARACTER` re-recognizes unreadable characters on the other pages; `OCROption.INVALID_CHARACTER_AND_SCAN_PAGE` both. Only takes effect when `enable_ocr` is on. |
| `languages` | `[]` | OCR recognition languages; when no language is given, English is used. Only takes effect when `enable_ocr` is on. |
| `enable_document_orientation_classification` | `False` | Detects the page rotation and turns the page image upright before OCR. Only takes effect when `enable_ocr` is on. |
| `enable_document_dewarp` | `False` | Flattens curved or warped page photos before OCR. Only takes effect when `enable_ocr` is on. |
| `contain_image` | `True` | TXT never contains images. With `enable_ocr` and `enable_ai_layout` on, OCR text inside image regions found by AI layout analysis is dropped while this is on; turn it off to keep that text. |
| `formula_to_image` | `True` | When on, formulas found by AI layout analysis are left out of the TXT; turn it off to keep the formula text. Only applies with `enable_ai_layout` on. |
| `output_document_per_page` | `False` | Writes one file per page instead of one document. The files are named after the input file plus the page number and are written to the folder of the output path; the file name in the output path is not used. |
| `page_ranges` | Empty | Pages to convert, e.g. "1-3,5,7-9"; empty converts every page. For multi-frame image input it selects the frames. |

Example:

```python
options = ConvertOptions()
options.txt_table_format = False
options.formula_to_image = False
error = CPDFConversion.start_pdf_to_txt("input.pdf", "password", "path/output.txt", options)
```

#### **Preserving Table Format**

The SDK supports an option called `txt_table_format` that preserves the table format when writing the TXT file, meaning that the original table structure is maintained. It is generally recommended to enable this option, especially for data extraction scenarios.

#### **Sample**

This sample demonstrates how to convert from a PDF to TXT file.

```python
input_file_path = "***"
password = "***"
output_file_name = "***"

txt_options = ConvertOptions()
error = CPDFConversion.start_pdf_to_txt(input_file_path, password, output_file_name, txt_options)
```
## 3.22 Convert PDF to Searchable PDF

#### **Overview**

To make a searchable PDF by adding invisible text to an image based PDF such as a scanned document using OCR.

#### **Conversion Options**

This format uses only the following options of `ConvertOptions`; the other options have no effect:

| Option | Default | Meaning |
| --- | --- | --- |
| `transparent_text` | `True` | PDF input: on keeps the original pages and adds an invisible OCR text layer; off rebuilds the pages with visible text, and vector graphics are not kept in the rebuilt pages. Image input: the recognized text is invisible (on) or visible (off). |
| `enable_ocr` | `False` | Adds the OCR text layer on the pages chosen by `ocr_option`. With `transparent_text` on and OCR off, the output is just the selected source pages. Ignored if the license does not include OCR. |
| `ocr_option` | `OCROption.ALL` | Which content OCR handles: `OCROption.ALL` every page; `OCROption.SCAN_PAGE` only image (scanned) pages; `OCROption.INVALID_CHARACTER` re-recognizes unreadable characters on the other pages (visible only when `transparent_text` is off); `OCROption.INVALID_CHARACTER_AND_SCAN_PAGE` both. Only takes effect when `enable_ocr` is on. |
| `languages` | `[]` | OCR recognition languages; the first language also selects the fallback font of the text layer. When no language is given, English is used. |
| `enable_document_orientation_classification` | `False` | Detects the page rotation and turns the page image upright before OCR; the page size follows the rotation. Only takes effect when `enable_ocr` is on and the page is rebuilt (`transparent_text` off, or image input). |
| `enable_document_dewarp` | `False` | Flattens curved or warped page photos before OCR. Only takes effect when `enable_ocr` is on and the page is rebuilt (`transparent_text` off, or image input). |
| `page_ranges` | Empty | Pages to convert, e.g. "1-3,5,7-9"; empty converts every page. For multi-frame image input it selects the frames. |
| `contain_image` | `True` | Only when the page is rebuilt (`transparent_text` off, or image input): keeps the source images on pages not recognized by OCR, and is required for `contain_page_background_image`. For image input without OCR, the image itself is drawn only when this is on. |
| `contain_page_background_image` | `True` | Only when the page is rebuilt and `contain_image` is on. On OCR pages with `transparent_text` off, draws the page image with the recognized text erased beneath the visible text (off: text only). For image input with `transparent_text` on, keeps the source image beneath the invisible text (off: invisible text only). |
| `contain_annotation` | `True` | Draws the appearance of annotations as images on pages that are rebuilt (`transparent_text` off) and not recognized by OCR. With `transparent_text` on, the original pages keep their annotations unchanged. |
| `font_name` | Empty | Font of the OCR text layer; with `transparent_text` off it is also the visible font of the rebuilt pages. If the font cannot be found, the OCR or system font is used. |
| `output_document_per_page` | `False` | Writes one file per page instead of one document. The files are named after the input file plus the page number and are written to the folder of the output path; the file name in the output path is not used. |
| `enable_auto_page_size` | `False` | Image input only: sizes the page from the image resolution, matched to the nearest standard paper size; when off, one image pixel becomes one point. |
| `custom_page_width` / `custom_page_height` | `0` | Image input only: exact page width and height in points (1 pt = 1/72 inch); both must be greater than 0. The image is fitted inside with white padding. Takes precedence over `enable_auto_page_size`. |

Example:

```python
options = ConvertOptions()
options.enable_ocr = True
options.ocr_option = OCROption.SCAN_PAGE
options.languages = [OCRLanguage.ENGLISH]
options.transparent_text = True
error = CPDFConversion.start_pdf_to_searchable_pdf("input.pdf", "password", "path/output.pdf", options)
```

#### **Set Transparent Text Layer**

When outputting a searchable PDF, you can use the following option to control the hidden text layer:

- `transparent_text`: Whether to output a transparent text layer.

#### **Sample**

Full code sample which shows how to use the PDFSolid OCR module on scanned documents in multiple languages.

```python
input_file_path = "***"
password = "***"
output_file_name = "***"

pdf_options = ConvertOptions()
pdf_options.enable_ocr = True
error = CPDFConversion.start_pdf_to_searchable_pdf(input_file_path, password, output_file_name, pdf_options)
```
## 3.23 Convert PDF to OFD

#### **Overview**

PDFSolid Conversion SDK supports converting PDF documents to OFD documents. Similar to searchable PDF, OFD conversion also supports OCR, page background preservation, and transparent text layers.

#### **Conversion Options**

This format uses only the following options of `ConvertOptions`; the other options have no effect:

| Option | Default | Meaning |
| --- | --- | --- |
| `enable_ocr` | `False` | The text layer comes from OCR on the pages chosen by `ocr_option`; when off, it comes from the text of the PDF. Image input without OCR has no text layer. Ignored if the license does not include OCR. |
| `ocr_option` | `OCROption.ALL` | Which content OCR handles: `OCROption.ALL` every page; `OCROption.SCAN_PAGE` only image (scanned) pages; `OCROption.INVALID_CHARACTER` re-recognizes unreadable characters of the text layer on the other pages; `OCROption.INVALID_CHARACTER_AND_SCAN_PAGE` both. Only takes effect when `enable_ocr` is on. |
| `languages` | `[]` | OCR recognition languages; when no language is given, English is used. Only takes effect when `enable_ocr` is on. |
| `enable_document_orientation_classification` | `False` | Turns the page image upright before OCR; the page size follows the rotation. Only takes effect when `enable_ocr` is on. |
| `enable_document_dewarp` | `False` | Flattens curved or warped page photos before OCR. Only takes effect when `enable_ocr` is on. |
| `page_ranges` | Empty | Pages to convert, e.g. "1-3,5,7-9"; empty converts every page. For multi-frame image input it selects the frames. |
| `enable_ai_layout` | `True` | Only changes how the invisible text of pages not recognized by OCR is grouped, and the header and footer detection; the visible page image is not affected. |
| `formula_to_image` | `True` | When on, the text of formulas found by AI layout analysis is removed from the invisible text layer (it can no longer be copied or searched); turn it off to keep it. The page image is unchanged. Only for pages not recognized by OCR, with `enable_ai_layout` on. |
| `output_document_per_page` | `False` | Writes one file per page instead of one document. The files are named after the input file plus the page number and are written to the folder of the output path; the file name in the output path is not used. |
| `enable_auto_page_size` | `False` | Image input only: sizes the page from the image resolution, matched to the nearest standard paper size; when off, one image pixel becomes one point. |
| `custom_page_width` / `custom_page_height` | `0` | Image input only: exact page width and height in points (1 pt = 1/72 inch); both must be greater than 0. The image is fitted inside with white padding. Takes precedence over `enable_auto_page_size`. |

Example:

```python
options = ConvertOptions()
options.enable_ocr = True
options.enable_document_orientation_classification = True
options.output_document_per_page = True
error = CPDFConversion.start_pdf_to_ofd("input.pdf", "password", "path/output.ofd", options)
```

#### **Sample**

```python
input_file_path = "***"
password = "***"
output_file_name = "***"

pdf_options = ConvertOptions()
pdf_options.enable_ocr = True
word_options.languages = [OCRLanguage.ENGLISH]
error = CPDFConversion.start_pdf_to_ofd(input_file_path, password, output_file_name, pdf_options)
```
## 3.24 Convert Word to PDF

#### **Overview**

PDFSolid Conversion SDK supports converting Word documents (.docx) to PDF. The input must be in DOCX format; the legacy binary `.doc` format is not supported. Word to PDF does not depend on any AI model.

#### **Basic Usage**

```python
# Windows and macOS; on Linux import from PdfSolidConversion instead.
from PDFSolidConversion import *

error = CPDFConversion.start_word_to_pdf("input.docx", "output.pdf")
if error != ErrorCode.SUCCESS:
    print("Word to PDF failed:", error)
```

`start_word_to_pdf` has two call forms, both returning an `ErrorCode`:

| Call form | Description |
| --- | --- |
| `start_word_to_pdf(file_path, output_path, callback=None)` | Uses the default options: no bookmarks, all pages output |
| `start_word_to_pdf(file_path, output_path, options, callback=None)` | Specifies the bookmarks and the page range through `ConvertOptions` (Word to PDF uses only these two) |

`callback` is an optional `ConvertCallback`. It works the same way as for PDF conversions and can be used to obtain progress and to cancel the conversion.

#### **Bookmarks and Page Range**

Word to PDF uses only the following properties of `ConvertOptions`; the others are ignored:

| Property | Default | Meaning |
| --- | --- | --- |
| `word_pdf_bookmark_mode` | `WordPdfBookmarkMode.NONE` | How the PDF bookmarks (the outline shown in a reader's navigation panel) are generated |
| `page_ranges` | empty string | The pages to output, e.g. `"1-3,5,7-9"`; empty outputs every page |

Values of `WordPdfBookmarkMode`:

| Value | Meaning |
| --- | --- |
| `NONE` | Do not generate bookmarks |
| `HEADINGS` | One bookmark per heading (a paragraph with an outline level), nested by level |
| `WORD_BOOKMARKS` | One bookmark per Word bookmark, named after it |

The document properties (title, author, subject, keywords) are always written to the PDF as filled in the Word document.

```python
options = ConvertOptions()
options.word_pdf_bookmark_mode = WordPdfBookmarkMode.HEADINGS   # or WORD_BOOKMARKS
options.page_ranges = "1-3,5,7-9"

callback = ConvertCallback()
callback.set_progress(lambda current, total: print(f"Progress: {current}/{total}"))

error = CPDFConversion.start_word_to_pdf("input.docx", "output.pdf", options, callback)
```

#### **Return Values and Unsupported-Feature Reports**

- A successful conversion returns `ErrorCode.SUCCESS`. Canceling through the callback returns `ErrorCode.CANCEL` and no output file is produced.
- If a specified page number exceeds the page count of the document, `ErrorCode.PDF_PAGE_ERROR` is returned and no output file is produced.
- When the document contains a feature that may affect fidelity, `ErrorCode.UNSUPPORTED_FEATURE` (95) is returned. The PDF is usually still generated in this case; check that the output file exists and verify its content. If the conversion itself fails, the real error code is returned and takes precedence over 95.
- The C / C++ interfaces additionally provide an optional diagnostics buffer that reports the specific feature identifiers and the output status. **The Python interface does not currently expose this parameter**; use the C or C++ interface if you need the diagnostic text.

#### **Availability**

Word to PDF is provided by the SDK's native library. Python modules of 1.2.0 and earlier do not contain this entry point. To keep the same code compatible with different module versions, check for it first:

```python
if hasattr(CPDFConversion, "start_word_to_pdf"):
    error = CPDFConversion.start_word_to_pdf("input.docx", "output.pdf")
```

When building the Python package from source, `setup.py` checks at build time whether the native library in use provides Word to PDF. If the native library uses an older interface, the build fails and asks you to use the native library, binding sources, and headers from the same revision.
## 3.25 Release library resources

**Overview**

Release the files and memory resources occupied by PDFSolid Conversion SDK.

**Notice**

- After calling this interface to release library resources, the PDFSolid Conversion SDK will no longer function properly and must be reloaded.

- When you only want to release the resources occupied by the AI model rather than all resources used by the PDFSolid Conversion SDK, you can achieve this by calling the `release_document_ai_model` interface.

- If synchronous conversion tasks are still running when `release` is called, the cleanup is deferred until the last task returns; new tasks are rejected during that period.

- While conversion tasks are running or a cleanup has not yet completed, reconfiguring the DocumentAI model (`set_document_ai_model`, etc.) is rejected and `ErrorCode.CONVERTING_ERROR` is returned.

- Unload the SDK only after all conversion interfaces have returned.


**Sample**

```python
LibraryManager.release_document_ai_model()
LibraryManager.release()
```

# 4. Data Extraction Guides

Unleash the Power of Data with PDFSolid Conversion SDK's Data Extraction to detect, recognize, analyze, and
extract the PDF text, image, table, etc.
## 4.1 Extract PDF to JSON

#### **Overview**

Extract text, tables, and images from PDF documents to a JSON file.

#### **Conversion Options**

This format uses only the following options of `ConvertOptions`; the other options have no effect:

| Option | Default | Meaning |
| --- | --- | --- |
| `json_contain_table` | `True` | On: each table is output once as an HTML table with the row, column, span and text of every cell; off: the text of each cell is output as a separate text item of the page content. |
| `contain_image` | `True` | On: the output is a .zip that holds the JSON, the page renderings and the image items; off: a plain .json without image items. With `enable_ocr` and `enable_ai_layout` on, it also drops the OCR text inside image regions found by AI layout analysis. |
| `enable_ai_layout` | `True` | Gives the object types (title, list, table, header, footer, ...), the grouping, the reading order and the table detection. Ignored if the license does not include AI layout analysis. |
| `enable_ai_table_recognition` | `True` | Recognizes the structure of tables with the table model; when off, the table structure is rebuilt from the ruling lines. Only applies to tables found by AI layout analysis (`enable_ai_layout` on). |
| `table_recognition_accuracy` | `TableRecognitionAccuracy.BALANCED` | Table model: `TableRecognitionAccuracy.BALANCED` uses the base documentai.model, `TableRecognitionAccuracy.HIGH_ACCURACY` uses the table_legacy.model package. Only takes effect when AI table recognition runs with the built-in table model. If the model of the requested accuracy is not loaded, the conversion still succeeds and tables fall back to rule-based recognition. |
| `enable_ocr` | `False` | Recognizes text with OCR on the pages chosen by `ocr_option`. Without OCR, image input gives only an image item (if `contain_image` is on) and no text. Ignored if the license does not include OCR. |
| `ocr_option` | `OCROption.ALL` | Which content OCR handles: `OCROption.ALL` every page; `OCROption.SCAN_PAGE` only image (scanned) pages; `OCROption.INVALID_CHARACTER` re-recognizes unreadable characters on the other pages; `OCROption.INVALID_CHARACTER_AND_SCAN_PAGE` both. Only takes effect when `enable_ocr` is on. |
| `languages` | `[]` | OCR recognition languages; when no language is given, English is used. Only takes effect when `enable_ocr` is on. |
| `enable_document_orientation_classification` | `False` | Turns the page image upright before OCR; the page width, height and coordinates follow the rotation. Only takes effect when `enable_ocr` is on. |
| `enable_document_dewarp` | `False` | Flattens curved or warped page photos before OCR. Only takes effect when `enable_ocr` is on. |
| `page_ranges` | Empty | Pages to convert, e.g. "1-3,5,7-9"; empty converts every page. For multi-frame image input it selects the frames. |
| `contain_annotation` | `True` | Outputs the appearance of annotations as image items. Only for PDF pages not recognized by OCR, and only when `contain_image` is on. |
| `formula_to_image` | `True` | When on, formulas found by AI layout analysis become text items with empty text; turn it off to keep the formula text. Only applies with `enable_ai_layout` on. |
| `output_document_per_page` | `False` | Writes one file per page instead of one document. The files are named after the input file plus the page number and are written to the folder of the output path; the file name in the output path is not used. |
| `enable_auto_page_size` | `False` | Image input only: the page width, height and all positions use the page size from the image resolution, matched to the nearest standard paper size. |
| `custom_page_width` / `custom_page_height` | `0` | Image input only: the page width, height and all positions use this exact page size in points; both must be greater than 0. Takes precedence over `enable_auto_page_size`. |

Example:

```python
options = ConvertOptions()
options.json_contain_table = False
options.contain_image = False
error = CPDFConversion.start_pdf_to_json("input.pdf", "password", "path/output.json", options)
```

#### **Standard table and non-standard table**

Commonly, tables can be divided into two categories: standard tables and non-standard tables. The specific definitions are as follows:

- Standard table: The table border and the inner lines of the table are complete and clear. There is no need to manually add table lines to divide the table content.

![image-20231116145224545](image/image-20231116145224545.png)

- **Non-Standard Tables:** Tables lacking borders or clear inner lines, requiring manual additions of table lines to separate contents.

![image-20231116145517818](image/image-20231116145517818.png)

#### **Table Extraction Option**

PDFSolid Conversion SDK supports the option `json_contain_table`. When enabled, table content is extracted from PDFs together with table structure; otherwise, table content is treated as regular text.

#### **Notice**

- Without enabling AI layout analysis or OCR options, tables in the original PDF cannot be extracted. It is recommended to enable AI layout analysis or OCR for high-precision table recognition.

#### **Sample**

Full sample code which illustrates the text extraction capabilities.

```python
input_file_path = "***"
password = "***"
output_file_name = "***"

json_options = ConvertOptions()
error = CPDFConversion.start_pdf_to_json(input_file_path, password, output_file_name, json_options)
```
## 4.2 Extract PDF to Markdown

#### **Overview**

Extract text, tables and images from PDF documents to Markdown file.

#### **Conversion Options**

This format uses only the following options of `ConvertOptions`; the other options have no effect:

| Option | Default | Meaning |
| --- | --- | --- |
| `enable_ai_layout` | `True` | Gives the titles, lists, captions, tables, images and the reading order. Headers and footers are always output as body text in Markdown. Ignored if the license does not include AI layout analysis. |
| `enable_ai_table_recognition` | `True` | Recognizes the cell structure of tables with the table model; the tables are written as HTML tables. Only applies to tables found by AI layout analysis (`enable_ai_layout` on). |
| `table_recognition_accuracy` | `TableRecognitionAccuracy.BALANCED` | Table model: `TableRecognitionAccuracy.BALANCED` uses the base documentai.model, `TableRecognitionAccuracy.HIGH_ACCURACY` uses the table_legacy.model package. Only takes effect when AI table recognition runs with the built-in table model. If the model of the requested accuracy is not loaded, the conversion still succeeds and tables fall back to rule-based recognition. |
| `enable_ocr` | `False` | Recognizes text with OCR on the pages chosen by `ocr_option`. Without OCR, image input gives only the page image (if `contain_image` is on). Ignored if the license does not include OCR. |
| `ocr_option` | `OCROption.ALL` | Which content OCR handles: `OCROption.ALL` every page; `OCROption.SCAN_PAGE` only image (scanned) pages; `OCROption.INVALID_CHARACTER` re-recognizes unreadable characters on the other pages; `OCROption.INVALID_CHARACTER_AND_SCAN_PAGE` both. Only takes effect when `enable_ocr` is on. |
| `languages` | `[]` | OCR recognition languages; when no language is given, English is used. Only takes effect when `enable_ocr` is on. |
| `enable_document_orientation_classification` | `False` | Detects the page rotation and turns the page image upright before OCR. Only takes effect when `enable_ocr` is on. |
| `enable_document_dewarp` | `False` | Flattens curved or warped page photos before OCR. Only takes effect when `enable_ocr` is on. |
| `page_ranges` | Empty | Pages to convert, e.g. "1-3,5,7-9"; empty converts every page. For multi-frame image input it selects the frames. |
| `contain_image` | `True` | Writes the source images and vector graphics (as pictures) into the Markdown; when off, they are not output. With `enable_ocr` and `enable_ai_layout` on, image regions are cropped as pictures and the OCR text inside them is dropped. |
| `contain_annotation` | `True` | Writes the appearance of annotations as images, independently of `contain_image`. Only for PDF pages not recognized by OCR. |
| `formula_to_image` | `True` | When on, formulas found by AI layout analysis are output as empty paragraphs, so the formula is lost; turn it off to keep the formula text. Only applies with `enable_ai_layout` on. |
| `output_document_per_page` | `False` | Writes one file per page instead of one document. The files are named after the input file plus the page number and are written to the folder of the output path; the file name in the output path is not used. |
| `enable_auto_page_size` | `False` | Image input only: the image width and height attributes (in points) follow the page size from the image resolution, matched to the nearest standard paper size. |
| `custom_page_width` / `custom_page_height` | `0` | Image input only: the image width and height attributes follow this exact page size in points; both must be greater than 0. Takes precedence over `enable_auto_page_size`. |

Example:

```python
options = ConvertOptions()
options.formula_to_image = False
options.contain_annotation = False
error = CPDFConversion.start_pdf_to_markdown("input.pdf", "password", "path/output.md", options)
```

#### **Sample**

Full code sample which shows how to convert from a PDF to Markdown file.

```python
input_file_path = "***"
password = "***"
output_file_name = "***"

markdown_options = ConvertOptions()
error = CPDFConversion.start_pdf_to_markdown(input_file_path, password, output_file_name, markdown_options)
```
# 5. Support
## 5.1 FAQ


- Does OCR work on x86 architecture?

  Currently, OCR only works on x64 architecture.
## 5.2 Contact Us

Thanks for your interest in PDFSolid Conversion SDK, an easy-to-use and powerful development solution. If you encounter technical questions or bug issues when using PDFSolid Conversion SDK, please submit a problem report to the [PDFSolid team](mailto:support@pdfsolid.com). The following information will help us solve your problem more efficiently:

- PDFSolid Conversion SDK product and version.
- Your operating system and IDE version.
- Detailed descriptions of the problem.
- Any other related information, such as an error screenshot.

#### **Contact Information**

- Home link: [https://www.pdfsolid.com](https://www.pdfsolid.com/)

- Email: [support@pdfsolid.com](mailto:support@pdfsolid.com)

Thanks,
The PDFSolid Team