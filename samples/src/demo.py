import sys
import os
from pathlib import Path

from PDFSolidConversion import LibraryManager, ErrorCode, ConvertOptions, CPDFConversion, OCRLanguage, ConvertCallback


license_path = Path(__file__).resolve().parent.parent / "license.xml"
error_code = LibraryManager.license_verify(
    str(license_path),
    "",
    ""
)

def progress_callback(current: int, total: int):
    print(f"Progress: {current} / {total}")

if error_code == ErrorCode.SUCCESS:
    print("License verify success")

    base_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    pdf_path = os.path.join(base_path, "pdf")
    excel_test_file_path = os.path.join(pdf_path, "excel.pdf")
    ppt_test_file_path = os.path.join(pdf_path, "powerpoint.pdf")
    word_test_file_path = os.path.join(pdf_path, "word.pdf")
    word_with_ocr_test_file_path = os.path.join(pdf_path, "word.pdf")

    resource_path = os.path.join(os.path.dirname(base_path), "resource")
    model_path = os.path.join(resource_path, "models", "documentai.model")
    output_path = os.path.join(base_path, "output")

    LibraryManager.initialize(str(resource_path))

    LibraryManager.set_logger(False, False)
    LibraryManager.set_document_ai_model(str(model_path))


    convert_options = ConvertOptions()
    callback = ConvertCallback()
    callback.set_progress(progress_callback)
    callback.set_cancel(lambda: False)
    # Convert PDF to Word
    CPDFConversion.start_pdf_to_word(str(word_test_file_path), "", str(output_path), convert_options, callback)

    # Convert PDF to Excel
    CPDFConversion.start_pdf_to_excel(str(excel_test_file_path), "", str(output_path), convert_options, callback)

    # Convert PDF to ppt
    CPDFConversion.start_pdf_to_ppt(str(ppt_test_file_path), "", str(output_path), convert_options, callback)

    # Convert PDF to csv
    excel_opt = ConvertOptions()
    excel_opt.excel_csv_format = True
    CPDFConversion.start_pdf_to_excel(str(excel_test_file_path), "", str(output_path), excel_opt, callback)

    # Convert PDF to HTML
    CPDFConversion.start_pdf_to_html(str(word_test_file_path), "", str(output_path), convert_options, callback)

    # Convert PDF to RTF
    CPDFConversion.start_pdf_to_rtf(str(word_test_file_path), "", str(output_path), convert_options, callback)

    # Convert PDF to Image
    CPDFConversion.start_pdf_to_image(str(word_test_file_path), "", str(output_path), convert_options, callback)

    # Convert PDF to Text
    CPDFConversion.start_pdf_to_txt(str(word_test_file_path), "", str(output_path), convert_options, callback)

    # Convert PDF to JSON
    CPDFConversion.start_pdf_to_json(str(word_test_file_path), "", str(output_path), convert_options, callback)

    # Convert PDF to Markdown
    CPDFConversion.start_pdf_to_markdown(str(word_test_file_path), "", str(output_path), convert_options, callback)

    # Convert PDF to Searchable PDF
    convert_options.enable_ocr = True
    languages = [OCRLanguage.ENGLISH]
    convert_options.languages = languages
    convert_options.transparent_text = True
    CPDFConversion.start_pdf_to_searchable_pdf(str(word_with_ocr_test_file_path), "", str(output_path), convert_options, callback)

    # Convert PDF to ofd
    CPDFConversion.start_pdf_to_ofd(str(word_test_file_path), "", str(output_path), convert_options, callback)


    LibraryManager.release()