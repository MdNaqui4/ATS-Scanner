import streamlit as st
import os
import tempfile

from src.pdf_extractor import extract_text_from_pdf
from src.text_preprocessing import clean_text
from src.skill_extractor import load_skills, extract_skills
from src.matcher import match_skills
from src.semantic_matcher import semantic_similarity

# ---------------- CONFIG ---------------- #

st.set_page_config(
    page_title="AI Resume Skill Matcher",
    page_icon="📄",
    layout="centered"
)

SKILLS_DB_PATH = "data/skills_list.csv"

# ---------------- UI ---------------- #

st.title("📄 AI Resume Parser & Skill Matcher")
st.caption("ATS-style resume analysis using NLP & semantic similarity")

resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
jd_text = st.text_area("Paste Job Description", height=220)

analyze_btn = st.button("Analyze Resume")

# ---------------- LOGIC ---------------- #

if analyze_btn:
    if not resume_file or not jd_text.strip():
        st.warning("Please upload a resume and paste a job description.")
        st.stop()

    with st.spinner("Analyzing resume..."):

        # ---- Save resume safely (temp file for production readiness) ---- #
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(resume_file.read())
            resume_path = tmp.name

        try:
            # ---- Text Extraction ---- #
            resume_text_raw = extract_text_from_pdf(resume_path)

            if not resume_text_raw.strip():
                st.error("Unable to extract text from resume. PDF may be image-based.")
                st.stop()

            # ---- Preprocessing ---- #
            resume_text = clean_text(resume_text_raw)
            jd_clean = clean_text(jd_text)

            # ---- Load Skills DB ---- #
            skills_db = load_skills(SKILLS_DB_PATH)

            # ---- Skill Extraction ---- #
            resume_skills = extract_skills(resume_text, skills_db)
            jd_skills = extract_skills(jd_clean, skills_db)

            # ---- Rule-based Skill Matching ---- #
            skill_match_result = match_skills(resume_skills, jd_skills)

            # ---- Semantic Similarity ---- #
            semantic_score = semantic_similarity(resume_text, jd_clean)

            # ---- Final ATS Score (Weighted) ---- #
            FINAL_ATS_SCORE = round(
                (0.6 * semantic_score) + (0.4 * skill_match_result["match_score"]),
                2
            )

        finally:
            os.remove(resume_path)

    # ---------------- OUTPUT ---------------- #

    st.success("Analysis Complete")

    col1, col2, col3 = st.columns(3)

    col1.metric("Skill Match %", skill_match_result["match_score"])
    col2.metric("Semantic Match %", semantic_score)
    col3.metric("Final ATS Score", FINAL_ATS_SCORE)

    st.divider()

    st.subheader("✅ Matched Skills")
    if skill_match_result["matched_skills"]:
        st.write(", ".join(sorted(skill_match_result["matched_skills"])))
    else:
        st.write("No matched skills found")

    st.subheader("❌ Missing Skills")
    if skill_match_result["missing_skills"]:
        st.write(", ".join(sorted(skill_match_result["missing_skills"])))
    else:
        st.write("No missing skills")

    st.subheader("📌 Recommendation")
    if FINAL_ATS_SCORE >= 75:
        st.success("Strong match for this role.")
    elif FINAL_ATS_SCORE >= 50:
        st.warning("Moderate match. Upskilling recommended.")
    else:
        st.error("Low match. Significant skill gap detected.")
