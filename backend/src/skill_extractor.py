import re
from src.skill_normalizer import normalize_skill

def extract_skills(text: str, skills_db=None):
    text = text.lower()
    found = set()

    for word in re.findall(r"[a-zA-Z\.]+", text):
        normalized = normalize_skill(word)
        if normalized:
            found.add(normalized)

    return found


def find_missing_skills(resume_skills, jd_skills):
    return jd_skills - resume_skills
