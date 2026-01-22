import nltk
from sentence_transformers import util
from src.semantic_matcher import model

nltk.download("punkt", quiet=True)

def sentence_level_match(resume_text: str, job_description: str, top_k=5):
    resume_sentences = nltk.sent_tokenize(resume_text)

    resume_embeddings = model.encode(resume_sentences, convert_to_tensor=True)
    jd_embedding = model.encode(job_description, convert_to_tensor=True)

    scores = util.cos_sim(resume_embeddings, jd_embedding).squeeze()

    results = []
    for idx, score in enumerate(scores):
        results.append({
            "sentence": resume_sentences[idx],
            "score": round(float(score), 3)
        })

    results.sort(key=lambda x: x["score"], reverse=True)

    return results[:top_k]
