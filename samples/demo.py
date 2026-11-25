#!/usr/bin/env python3

import argparse
import os
import sys
from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
if str(PACKAGE_ROOT) not in sys.path:
    sys.path.insert(0, str(PACKAGE_ROOT))

from PDFSolidConversion import (  # noqa: E402
    CPDFConversion,
    ConvertCallback,
    ConvertOptions,
    ErrorCode,
    ExcelWorksheetOption,
    HtmlOption,
    ImageColorMode,
    ImageType,
    LibraryManager,
    OCRLanguage,
    OCROption,
    PageLayoutMode,
)

SAMPLE_ROOT = Path(__file__).resolve().parent
DEFAULT_LICENSE_PATH = SAMPLE_ROOT / "license.xml"
DEFAULT_INPUT_DIR = SAMPLE_ROOT / "input_files"
DEFAULT_OUTPUT_DIR = SAMPLE_ROOT / "output_files"
DEFAULT_MODEL_PATH = PACKAGE_ROOT / "resource" / "models" / "documentai.model"


def license_file_path(value: str) -> bool:
    return value.lower().endswith(".xml") or Path(value).expanduser().exists()


def normalize_license(value: str) -> str:
    if not value:
        raise ValueError("License is required. Pass --license or set CONVERSION_LICENSE.")
    if license_file_path(value):
        path = Path(value).expanduser().resolve()
        if not path.is_file():
            raise FileNotFoundError(f"License file not found: {path}")
        return str(path)
    return value


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Conversion SDK Python sample")
    parser.add_argument("inputs", nargs="*", help="Input PDF files. Defaults to samples/input_files.")
    parser.add_argument("--license", default=os.environ.get("CONVERSION_LICENSE", str(DEFAULT_LICENSE_PATH)))
    parser.add_argument("--device-id", default=os.environ.get("CONVERSION_DEVICE_ID", ""))
    parser.add_argument("--app-id", default=os.environ.get("CONVERSION_APP_ID"))
    parser.add_argument("--resource", default=os.environ.get("CONVERSION_RESOURCE_PATH", ""))
    parser.add_argument("-o", "--output", default=str(DEFAULT_OUTPUT_DIR))
    parser.add_argument("-m", "--model", default=os.environ.get("CONVERSION_MODEL_PATH", str(DEFAULT_MODEL_PATH)))
    args = parser.parse_args()

    app_id_specified = args.app_id is not None
    args.license = normalize_license(args.license)
    if args.app_id is None:
        args.app_id = "" if license_file_path(args.license) else "conversion.demo"
    if not app_id_specified and license_file_path(args.license):
        args.app_id = ""
    return args


def ensure_input_pdf(path: Path) -> str:
    resolved = path.expanduser().resolve()
    if not resolved.is_file():
        raise FileNotFoundError(f"Input PDF not found: {resolved}")
    return str(resolved)


def default_options() -> ConvertOptions:
    options = ConvertOptions()
    options.enable_ai_layout = True
    options.enable_ai_table_recognition = True
    options.contain_image = True
    options.contain_page_background_image = True
    options.json_contain_table = True
    options.contain_annotation = True
    options.excel_all_content = False
    options.excel_csv_format = False
    options.enable_ocr = False
    options.transparent_text = True
    options.txt_table_format = True
    options.image_path_enhance = False
    options.formula_to_image = True
    options.auto_create_folder = True
    options.output_document_per_page = False
    options.image_scaling = 4.0
    options.page_layout_mode = PageLayoutMode.FLOW
    options.excel_worksheet_option = ExcelWorksheetOption.FOR_TABLE
    options.html_option = HtmlOption.SINGLE_PAGE
    options.ocr_option = OCROption.ALL
    options.image_color_mode = ImageColorMode.COLOR
    options.image_type = ImageType.JPG
    options.languages = [OCRLanguage.CHINESE]
    return options


def box_layout_options() -> ConvertOptions:
    options = default_options()
    options.page_layout_mode = PageLayoutMode.BOX
    return options


def conversion_callback(label: str) -> ConvertCallback:
    callback = ConvertCallback()
    callback.set_progress(lambda current, total: print(f"[{label}] progress: {current}/{total}"))
    callback.set_cancel(lambda: False)
    return callback


def run_conversion(label: str, method, input_pdf: str, output_path: Path, options: ConvertOptions) -> None:
    result = method(input_pdf, "", str(output_path), options, conversion_callback(label))
    print(f"{label}: result={result}, output={output_path}")
    if result != ErrorCode.SUCCESS:
        raise RuntimeError(f"{label} failed with result={result}")


def verify_and_initialize(args: argparse.Namespace) -> None:
    license_code = LibraryManager.license_verify(args.license, args.device_id, args.app_id)
    print(f"license_verify => {license_code}")
    if license_code != ErrorCode.SUCCESS:
        raise RuntimeError(f"license verify failed with result={license_code}")

    LibraryManager.initialize(args.resource)
    LibraryManager.set_logger(False, True)
    print(f"version => {LibraryManager.get_version()}")

    model_path = Path(args.model).expanduser().resolve() if args.model else None
    if model_path and model_path.is_file():
        model_code = LibraryManager.set_document_ai_model(str(model_path), -1)
        print(f"set_document_ai_model => {model_code}")
        if model_code != ErrorCode.SUCCESS:
            raise RuntimeError(f"set document ai model failed with result={model_code}")


def sample_input(name: str) -> str:
    return ensure_input_pdf(DEFAULT_INPUT_DIR / name)


def run_default_suite(args: argparse.Namespace) -> None:
    output_dir = Path(args.output).expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    word_pdf = sample_input("word.pdf")
    excel_pdf = sample_input("excel.pdf")
    powerpoint_pdf = sample_input("powerpoint.pdf")

    verify_and_initialize(args)

    try:
        run_conversion("pdf to word", CPDFConversion.start_pdf_to_word, word_pdf, output_dir / "word.docx", default_options())
        run_conversion("pdf to excel", CPDFConversion.start_pdf_to_excel, excel_pdf, output_dir / "excel.xlsx", default_options())
        run_conversion("pdf to ppt", CPDFConversion.start_pdf_to_ppt, powerpoint_pdf, output_dir / "powerpoint.pptx", default_options())

        csv_options = default_options()
        csv_options.excel_csv_format = True
        run_conversion("pdf to csv", CPDFConversion.start_pdf_to_excel, excel_pdf, output_dir, csv_options)

        layout_options = box_layout_options()
        run_conversion("pdf to html", CPDFConversion.start_pdf_to_html, word_pdf, output_dir / "html.html", layout_options)
        run_conversion("pdf to rtf", CPDFConversion.start_pdf_to_rtf, word_pdf, output_dir / "rtf.rtf", layout_options)
        run_conversion("pdf to image", CPDFConversion.start_pdf_to_image, word_pdf, output_dir, layout_options)
        run_conversion("pdf to txt", CPDFConversion.start_pdf_to_txt, word_pdf, output_dir / "txt.txt", layout_options)
        run_conversion("pdf to json", CPDFConversion.start_pdf_to_json, word_pdf, output_dir / "json.json", layout_options)
        run_conversion("pdf to markdown", CPDFConversion.start_pdf_to_markdown, word_pdf, output_dir / "markdown.md", layout_options)

        searchable_options = box_layout_options()
        searchable_options.enable_ocr = True
        searchable_options.transparent_text = True
        searchable_options.languages = [OCRLanguage.ENGLISH]
        run_conversion(
            "pdf to searchable pdf",
            CPDFConversion.start_pdf_to_searchable_pdf,
            excel_pdf,
            output_dir / "pdf.pdf",
            searchable_options,
        )

        ofd_options = box_layout_options()
        ofd_options.enable_ocr = True
        ofd_options.transparent_text = True
        ofd_options.languages = [OCRLanguage.ENGLISH]
        run_conversion("pdf to ofd", CPDFConversion.start_pdf_to_ofd, word_pdf, output_dir / "pdf.ofd", ofd_options)

        print("all conversion tasks finished")
    finally:
        LibraryManager.release_document_ai_model()
        LibraryManager.release()


def run_custom_inputs(args: argparse.Namespace) -> None:
    output_dir = Path(args.output).expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    verify_and_initialize(args)

    try:
        for input_arg in args.inputs:
            input_pdf = ensure_input_pdf(Path(input_arg))
            output_path = output_dir / f"{Path(input_pdf).stem}.docx"
            run_conversion("pdf to word", CPDFConversion.start_pdf_to_word, input_pdf, output_path, default_options())
    finally:
        LibraryManager.release_document_ai_model()
        LibraryManager.release()


def main() -> int:
    args = parse_args()
    if args.inputs:
        run_custom_inputs(args)
    else:
        run_default_suite(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
