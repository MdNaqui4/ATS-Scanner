from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pdfplumber
import tempfile
import os
import traceback

from src.semantic_matcher import semantic_similarity
from src.skill_extractor import extract_skills, find_missing_skills
from src.sentence_explainer import sentence_level_explainability

app = FastAPI(title="ATS Resume Analyzer")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # lock later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/resume/analyze")
async def analyze_resume(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    try:
        # 1️⃣ Save PDF temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(await resume.read())
            pdf_path = tmp.name

        # 2️⃣ Extract resume text
        resume_text = ""
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    resume_text += text + "\n"

        os.remove(pdf_path)

        if not resume_text.strip():
            raise HTTPException(status_code=400, detail="Resume text could not be extracted")

        # 3️⃣ Semantic similarity
        score = semantic_similarity(resume_text, job_description)

        # 4️⃣ Skill extraction + normalization
        resume_skills = extract_skills(resume_text)
        jd_skills = extract_skills(job_description)
        missing_skills = find_missing_skills(resume_skills, jd_skills)

        # 5️⃣ Sentence-level explainability
        sentence_matches = sentence_level_explainability(
            resume_text,
            job_description
        )

        return {
            "score": round(float(score), 2),
            "resume_skills": sorted(resume_skills),
            "job_skills": sorted(jd_skills),
            "missing_skills": sorted(missing_skills),
            "sentence_explainability": sentence_matches
        }

    except HTTPException:
        raise
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
