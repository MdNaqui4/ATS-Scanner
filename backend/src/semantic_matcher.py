from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import re

_model = SentenceTransformer("all-MiniLM-L6-v2")


def _split_sentences(text: str):
    text = text.replace("\n", " ")
    sentences = re.split(r'(?<=[.!?])\s+', text)

    cleaned = []
    for s in sentences:
        s = s.strip()
        if 40 <= len(s) <= 280:
            cleaned.append(s)
    return cleaned


def semantic_similarity(resume_text: str, jd_text: str) -> float:
    """
    ATS-style semantic score:
    - Sentence-level comparison
    - Average of best matches
    """

    resume_sentences = _split_sentences(resume_text)
    jd_sentences = _split_sentences(jd_text)

    # Fallback (JD optional later)
    if not resume_sentences or not jd_sentences:
        return 0.0

    resume_emb = _model.encode(resume_sentences, normalize_embeddings=True)
    jd_emb = _model.encode(jd_sentences, normalize_embeddings=True)

    sim_matrix = cosine_similarity(resume_emb, jd_emb)

    # Best JD match per resume sentence
    best_scores = sim_matrix.max(axis=1)

    # ATS-style filtering (ignore weak noise)
    strong_scores = best_scores[best_scores >= 0.45]

    if len(strong_scores) == 0:
        return 0.0

    final_score = float(np.mean(strong_scores))
    return round(final_score, 3)
