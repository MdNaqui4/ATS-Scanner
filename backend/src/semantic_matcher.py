from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

_model = SentenceTransformer("all-MiniLM-L6-v2")

def semantic_similarity(resume_text: str, jd_text: str) -> float:
    embeddings = _model.encode(
        [resume_text, jd_text],
        normalize_embeddings=True
    )

    similarity = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0]

    # ✅ CRITICAL FIX
    return float(similarity)
