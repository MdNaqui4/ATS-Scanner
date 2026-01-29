import os
import tempfile
from fastapi import APIRouter, UploadFile, File, Form, HTTPException

from src.pdf_extractor import extract_text_from_pdf
from src.text_preprocessing import clean_text
from src.skill_extractor import load_skills, extract_skills
from src.experience_matcher import compute_experience_score
from src.semantic_matcher import compute_keyword_score
from src.utils import compute_formatting_score
from src.scoring import build_score_payload

router = APIRouter(prefix="/resume", tags=["Resume"])

SKILLS_DB_PATH = "data/skills_list.csv"


@router.post("/analyze")
async def analyze_resume(
    resume: UploadFile = File(...),
    job_description: str = Form(default="")
):
    # -----------------------------
    # VALIDATION
    # -----------------------------
    if resume.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF resumes are supported")

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(await resume.read())
        resume_path = tmp.name

    try:
        # -----------------------------
        # PDF → TEXT
        # -----------------------------
        resume_text_raw = extract_text_from_pdf(resume_path)

        if not resume_text_raw or not resume_text_raw.strip():
            raise HTTPException(
                status_code=422,
                detail="Unable to extract text from resume (possibly scanned PDF)"
            )

        resume_text = clean_text(resume_text_raw)
        jd_text = clean_text(job_description) if job_description else None

        # -----------------------------
        # LOAD SKILLS DATABASE
        # -----------------------------
        skills_db = load_skills(SKILLS_DB_PATH)

        # -----------------------------
        # COMPONENT SCORES (0–100)
        # -----------------------------
        skills_score = extract_skills(
            resume_text=resume_text,
            jd_text=jd_text,
            skills_db=skills_db
        )

        experience_score = compute_experience_score(
            resume_text=resume_text,
            jd_text=jd_text
        )

        keyword_score = compute_keyword_score(
            resume_text=resume_text,
            jd_text=jd_text
        )

        formatting_score = compute_formatting_score(resume_text)

        components = {
            "skills": skills_score,
            "experience": experience_score,
            "keywords": keyword_score,
            "formatting": formatting_score,
        }

        # -----------------------------
        # FINAL CALIBRATED SCORE
        # -----------------------------
        score_payload = build_score_payload(components)

        return {
            "score": score_payload["final_score"],
            "grade": score_payload["grade"],
            "confidence": score_payload["confidence"],
            "breakdown": score_payload["breakdown"],
        }

    finally:
        os.remove(resume_path)
