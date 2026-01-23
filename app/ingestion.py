from PyPDF2 import PdfReader


def upload_pdf(file_path: str) -> dict:
    """
    Uploads a PDF file and extracts its text content.

    Args:
        file_path (str): The path to the PDF file.

    Returns:
        dict: A dictionary containing the file name and extracted text.
    """

    reader = PdfReader(file_path)
    extracted_text = []

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text and page_text.strip():
            extracted_text.append(page_text.strip())

    return {"file_name": file_path, "extracted_text": "\n".join(extracted_text)}
