import sys
from Resume_parser import extract_from_pdf, extract_from_docx

def run():
    if len(sys.argv) < 2:
        print("Usage: python app.py <file_path>")
        return 
    
    path = sys.argv[1]

    # Check file format
    if path.endswith(".pdf"):
        text = extract_from_pdf(path)
    elif path.endswith(".docx"):
        text = extract_from_docx(path)
    else:
        print("Unsupported file format. Only .pdf and .docx allowed.")
        return

    # Print extracted text
    print("\n------ Extracted Text ------\n")
    print(text)


if __name__ == "__main__":
    run()
