# AI-Powered Resume Analyzer (ATS)

A full-stack AI-powered resume analysis platform that evaluates resumes against job descriptions, scores them, highlights skills matches/mismatches, and provides sentence-level explainability.

## Features

- **Resume vs Job Analysis:** Automatically extracts skills from resumes and job descriptions.
- **Skill Scoring & Weighting:** Computes an overall matching score with missing skill identification.
- **Sentence-Level Explainability:** Highlights sentences in the resume that match or relate to the job description.
- **Frontend Dashboard:** Interactive UI with progress bars, badges, and color-coded skill matching.
- **File Upload Support:** Accepts PDF resumes for analysis.
- **Error Handling & Fallbacks:** Robust handling of failed API requests and missing inputs.
- **Extensible Architecture:** Easily add new scoring rules or integrate with other NLP models.
- **Fast & Lightweight:** Powered by `Sentence-Transformers` and `NLTK` for efficient processing.

## Tech Stack

- **Backend:** Python, FastAPI, NLTK, Sentence-Transformers, Scikit-learn
- **Frontend:** Next.js, React, TypeScript, TailwindCSS
- **Deployment:** Can be hosted on Vercel/Netlify (frontend) and any cloud server for FastAPI
- **Other Tools:** Docker for containerized deployment

## Getting Started

### Backend

```
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload

```
Frontend
```
cd frontend
npm install
npm run dev

```
Open your browser at ```http://localhost:3000```
 to access the UI.

Usage

Upload a PDF resume.

Paste or enter the Job Description.

Click Analyze Resume.

View:

Resume Skills

Job Skills

Missing Skills

Sentence-level explainability
