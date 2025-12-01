import json

def extract_skills(text):
    # Load skill list from JSON
    with open("assets/skills.json", "r") as f:
        skills_data = json.load(f)

    skills_list = skills_data["skills"]

    detected = []
    
    # Check if each skill exists in the resume text
    for skill in skills_list:
        if skill in text:
            detected.append(skill)

    # Find missing ones
    missing = list(set(skills_list) - set(detected))

    return detected, missing
