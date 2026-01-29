from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import re

model = SentenceTransformer("all-MiniLM-L6-v2")

def split_sentences(text: str):
    raw = re.split(r'(?<=[.!?])\s+', text)
    return [s.strip() for s in raw if 20 <= len(s) <= 300]


def sentence_level_explainability(resume_text: str, jd_text: str):
    resume_sents = split_sentences(resume_text)
    jd_sents = split_sentences(jd_text)

    if not resume_sents or not jd_sents:
        return []

    resume_emb = model.encode(resume_sents, normalize_embeddings=True)
    jd_emb = model.encode(jd_sents, normalize_embeddings=True)

    sim = cosine_similarity(resume_emb, jd_emb)
    results = []

    for i, row in enumerate(sim):
        j = row.argmax()
        score = float(row[j])

        if score >= 0.30:
            results.append({
                "resume_sentence": resume_sents[i],
                "matched_jd_sentence": jd_sents[j],
                "similarity": round(score, 2)
            })

    return results
