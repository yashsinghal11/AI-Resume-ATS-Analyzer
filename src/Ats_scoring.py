def calculate_ats_score(detected_skills, total_skills):
    # Handle divide-by-zero error
    if total_skills == 0:
        return 0
    
    score = (len(detected_skills) / total_skills) * 100
    return round(score, 2)
