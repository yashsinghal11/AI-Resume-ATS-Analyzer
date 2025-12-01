import sys
from src.Resume_parser import extract_from_pdf, extract_from_docx, extract_text
from src.cleaner import clean_text
from src.skill_extractor import extract_skills
from src.Ats_scoring import calculate_ats_score

def main():
    if len(sys.argv) < 2:
        print("Usage: python app.py <resume_file>")
        return

    resume_path = sys.argv[1]

    # ----------------------
    # 1. Extract Text
    # ----------------------
    print("\n📄 Extracting text from resume...\n")

    if resume_path.endswith(".pdf"):
        raw_text = extract_from_pdf(resume_path)
    elif resume_path.endswith(".docx"):
        raw_text = extract_from_docx(resume_path)
    else:
        print("❌ Unsupported file format. Only .pdf and .docx allowed.")
        return

    print("\n------ Extracted Text ------\n")
    print(raw_text)

    # ----------------------
    # 2. Clean Text
    # ----------------------
    print("\n🧹 Cleaning text...\n")
    cleaned_text = clean_text(raw_text)

    # ----------------------
    # 3. Extract Skills
    # ----------------------
    print("\n🔍 Extracting skills...\n")
    detected, missing = extract_skills(cleaned_text)

    # ----------------------
    # 4. ATS Score
    # ----------------------
    print("\n📊 Calculating ATS Score...\n")
    total_skills = len(detected) + len(missing)
    score = calculate_ats_score(detected, total_skills)

    # ----------------------
    # 5. Final Output
    # ----------------------
    print("====== RESULT ======")
    print("Detected Skills:", detected)
    print("Missing Skills:", missing)
    print("ATS Score:", score, "%")


if __name__ == "__main__":
    main()
