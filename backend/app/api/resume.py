import os
import tempfile
from fastapi import APIRouter, UploadFile, File, Form, HTTPException

from src.pdf_extractor import extract_text_from_pdf
from src.text_preprocessing import clean_text
from src.skill_extractor import load_skills, extract_skills
from src.matcher import match_skills
from src.semantic_matcher import semantic_similarity

router = APIRouter(prefix="/resume", tags=["Resume"])

SKILLS_DB_PATH = "data/skills_list.csv"


@router.post("/analyze")
async def analyze_resume(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    if resume.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF resumes are supported")

    # Save resume temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(await resume.read())
        resume_path = tmp.name

    try:
        resume_text_raw = extract_text_from_pdf(resume_path)

        if not resume_text_raw.strip():
            raise HTTPException(
                status_code=422,
                detail="Unable to extract text from resume (possibly scanned PDF)"
            )

        resume_clean = clean_text(resume_text_raw)
        jd_clean = clean_text(job_description)

        skills_db = load_skills(SKILLS_DB_PATH)

        resume_skills = extract_skills(resume_clean, skills_db)
        jd_skills = extract_skills(jd_clean, skills_db)

        skill_match_result = match_skills(resume_skills, jd_skills)
        semantic_score = semantic_similarity(resume_clean, jd_clean)

        final_ats_score = round(
            (0.6 * semantic_score) + (0.4 * skill_match_result["match_score"]),
            2
        )

        return {
            "skill_match_score": skill_match_result["match_score"],
            "semantic_match_score": semantic_score,
            "final_ats_score": final_ats_score,
            "matched_skills": sorted(skill_match_result["matched_skills"]),
            "missing_skills": sorted(skill_match_result["missing_skills"]),
        }

    finally:
        os.remove(resume_path)
