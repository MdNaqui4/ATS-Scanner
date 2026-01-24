import re
from src.skill_normalizer import normalize_skill

# -----------------------
# Skill Definitions
# -----------------------

CORE_SKILLS = {
    "frontend": {"html", "css", "javascript", "react"},
    "backend": {"python", "node", "api", "database"},
}

SECONDARY_SKILLS = {
    "frontend": {"typescript", "webpack", "babel", "accessibility"},
    "backend": {"docker", "aws", "redis"},
}

# -----------------------
# Skill Extraction
# -----------------------

def extract_skills(text: str, skills_db=None):
    text = text.lower()
    found = set()

    for word in re.findall(r"[a-zA-Z\.]+", text):
        normalized = normalize_skill(word)
        if normalized:
            found.add(normalized)

    return found


def find_missing_skills(resume_skills, jd_skills):
    resume_set = set(resume_skills or [])
    jd_set = set(jd_skills or [])

    return list(jd_set - resume_set)


# -----------------------
# Skill Match Scoring
# -----------------------

def skill_match_score(resume_skills, job_skills, role="frontend"):
    core = CORE_SKILLS.get(role, set())
    secondary = SECONDARY_SKILLS.get(role, set())

    job_skills = set(job_skills)
    resume_skills = set(resume_skills)

    core_required = core & job_skills
    secondary_required = secondary & job_skills

    core_match = len(core_required & resume_skills) / max(len(core_required), 1)
    secondary_match = len(secondary_required & resume_skills) / max(len(secondary_required), 1)

    return round((0.7 * core_match + 0.3 * secondary_match) * 100, 2)
