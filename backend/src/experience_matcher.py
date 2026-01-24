import re

def extract_years(text: str) -> int:
    matches = re.findall(r'(\d+)\+?\s*years?', text.lower())
    return max(map(int, matches)) if matches else 0

def experience_score(resume_text, jd_text):
    resume_years = extract_years(resume_text)
    jd_years = extract_years(jd_text)

    if jd_years == 0:
        return 100
    if resume_years >= jd_years:
        return 100
    return round((resume_years / jd_years) * 100, 2)
