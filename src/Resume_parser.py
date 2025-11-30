import pdfplumber
from docx import Document
import os

def extract_from_pdf(path):
    """Extract text from a PDF file using pdfplumber."""
    if not os.path.exists(path):
        return f"Error: File not found -> {path}"

    text = ""
    try:
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                txt = page.extract_text()
                if txt:
                    text += txt + "\n"
    except Exception as e:
        return f"Error reading PDF: {e}"

    return text.strip()


def extract_from_docx(path):
    """Extract text from a DOCX file."""
    if not os.path.exists(path):
        return f"Error: File not found -> {path}"

    try:
        doc = Document(path)
        paragraphs = [p.text.strip() for p in doc.paragraphs if p.text.strip()]
        return "\n".join(paragraphs)
    except Exception as e:
        return f"Error reading DOCX: {e}"


if __name__ == "__main__":
    file = "Yash_Singhal_Resume_.pdf"   # sample
    print(extract_from_pdf(file))
