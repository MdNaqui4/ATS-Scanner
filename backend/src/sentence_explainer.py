from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import re

model = SentenceTransformer("all-MiniLM-L6-v2")


def clean_sentences(text: str):
    text = text.replace("\n", " ")
    raw = re.split(r'(?<=[.!?])\s+', text)

    sentences = []
    for s in raw:
        s = s.strip()

        if len(s) < 40:
            continue
        if len(s) > 280:
            continue
        if s.count(",") > 10:
            continue
        if s.lower().startswith(("skills", "technologies", "tools")):
            continue

        sentences.append(s)

    return sentences


def sentence_level_explainability(resume_text: str, jd_text: str):
    resume_sentences = clean_sentences(resume_text)
    jd_sentences = clean_sentences(jd_text)

    # 🚫 HARD GUARD
    if not resume_sentences or not jd_sentences:
        return []

    resume_emb = model.encode(resume_sentences, normalize_embeddings=True)
    jd_emb = model.encode(jd_sentences, normalize_embeddings=True)

    similarities = cosine_similarity(resume_emb, jd_emb)

    results = []

    for i, row in enumerate(similarities):
        best_idx = int(row.argmax())
        score = float(row[best_idx])

        # 🔒 Strict ATS threshold
        if score < 0.45:
            continue

        jd_sentence = jd_sentences[best_idx].strip()
        if not jd_sentence:
            continue

        results.append({
            "resume_sentence": resume_sentences[i],
            "matched_jd_sentence": jd_sentence,
            "similarity": round(score, 2)
        })

    return results
