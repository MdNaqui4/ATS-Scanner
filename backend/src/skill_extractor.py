import re
import csv
from typing import Set, Optional

_SKILLS_CACHE: Optional[Set[str]] = None


def load_skills(csv_path: str) -> Set[str]:
    global _SKILLS_CACHE

    if _SKILLS_CACHE is not None:
        return _SKILLS_CACHE

    skills = set()
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                skills.add(row[0].strip().lower())

    _SKILLS_CACHE = skills
    return skills


def extract_skills(text: str, skills_db: Optional[Set[str]] = None) -> Set[str]:
    """
    Backward-safe:
    - If skills_db is not passed, return empty set instead of crashing
    - Prevents 500 errors
    """
    if not text:
        return set()

    if skills_db is None:
        return set()

    text = text.lower()
    found = set()

    for skill in skills_db:
        if re.search(rf"\b{re.escape(skill)}\b", text):
            found.add(skill)

    return found


def find_missing_skills(resume_skills, jd_skills):
    return list(set(jd_skills or []) - set(resume_skills or []))
