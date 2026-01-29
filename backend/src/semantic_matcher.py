from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import re

model = SentenceTransformer("all-MiniLM-L6-v2")

def split(text):
    return [s.strip() for s in re.split(r'(?<=[.!?])\s+', text) if len(s) > 20]

def semantic_similarity(resume_text: str, jd_text: str) -> float:
    r = split(resume_text)
    j = split(jd_text)

    if not r or not j:
        return 0.0

    r_emb = model.encode(r, normalize_embeddings=True)
    j_emb = model.encode(j, normalize_embeddings=True)

    sims = cosine_similarity(r_emb, j_emb)
    best = sims.max(axis=1)

    strong = best[best >= 0.30]
    return round(float(np.mean(strong)) * 100, 2) if len(strong) else 0.0
