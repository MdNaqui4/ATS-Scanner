def match_skills(resume_skills: set, jd_skills: set):
    matched = resume_skills.intersection(jd_skills)
    missing = jd_skills - resume_skills
    score = (len(matched) / len(jd_skills)) * 100 if jd_skills else 0

    return {
        "match_score": round(score, 2),
        "matched_skills": list(matched),
        "missing_skills": list(missing),
    }
