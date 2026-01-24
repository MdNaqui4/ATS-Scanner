# src/scoring.py

from typing import Dict, List
from src.semantic_matcher import semantic_similarity
from src.sentence_explainer import sentence_level_explainability
from src.skill_extractor import extract_skills, find_missing_skills
from src.experience_matcher import experience_alignment_score


def skill_match_score(resume_skills: List[str], jd_skills: List[str]) -> float:
    if not jd_skills:
        return 0.0

    matched = set(resume_skills) & set(jd_skills)
    return len(matched) / len(jd_skills)


def semantic_sentence_score(sentence_matches: List[Dict]) -> float:
    if not sentence_matches:
        return 0.0

    scores = [m["similarity"] for m in sentence_matches]
    return sum(scores) / len(scores)


def compute_final_score(resume_text: str, jd_text: str) -> Dict:
    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)

    missing_skills = find_missing_skills(resume_skills, jd_skills)

    sentence_matches = sentence_level_explainability(resume_text, jd_text)

    skill_score = skill_match_score(resume_skills, jd_skills)
    semantic_score = semantic_sentence_score(sentence_matches)
    experience_score = experience_alignment_score(resume_text, jd_text)

    final_score = (
        skill_score * 0.40 +
        semantic_score * 0.35 +
        experience_score * 0.15
    )

    return {
        "final_score": round(final_score * 100, 2),
        "skill_score": round(skill_score * 100, 2),
        "semantic_score": round(semantic_score * 100, 2),
        "experience_score": round(experience_score * 100, 2),
        "resume_skills": sorted(resume_skills),
        "job_skills": sorted(jd_skills),
        "missing_skills": sorted(missing_skills),
        "sentence_explainability": sentence_matches
    }
