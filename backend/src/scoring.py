def calibrate_score(raw_score: float) -> int:
    """
    Clamp score into realistic ATS range
    """
    return round(min(95, max(35, raw_score)))


def get_confidence_label(score: int) -> str:
    if score >= 80:
        return "Excellent Fit"
    if score >= 65:
        return "Good Match"
    if score >= 50:
        return "Partial Match"
    return "Needs Improvement"


def get_grade(score: int) -> str:
    if score >= 85:
        return "A+"
    if score >= 75:
        return "A"
    if score >= 65:
        return "B"
    if score >= 55:
        return "C"
    return "D"


def build_score_payload(components: dict) -> dict:
    """
    components = {
        "skills": int,
        "experience": int,
        "keywords": int,
        "formatting": int
    }
    """

    # Weights (LOCKED)
    weighted_score = (
        components["skills"] * 0.35 +
        components["experience"] * 0.30 +
        components["keywords"] * 0.20 +
        components["formatting"] * 0.15
    )

    final_score = calibrate_score(weighted_score)

    return {
        "final_score": final_score,
        "grade": get_grade(final_score),
        "confidence": get_confidence_label(final_score),
        "breakdown": components
    }






# def safe_score(value, default=50):
#     """
#     Prevent zero-collapse in resume-only mode
#     """
#     if value is None:
#         return default
#     return max(0, min(100, value))


# def calibrate_score(raw_score: float) -> int:
#     """
#     Clamp score into realistic ATS range
#     """
#     return round(min(95, max(35, raw_score)))


# def get_confidence_label(score: int) -> str:
#     if score >= 80:
#         return "Excellent Fit"
#     if score >= 65:
#         return "Good Match"
#     if score >= 50:
#         return "Partial Match"
#     return "Needs Improvement"


# def get_grade(score: int) -> str:
#     if score >= 85:
#         return "Excellent"
#     if score >= 70:
#         return "Good"
#     if score >= 55:
#         return "Average"
#     return "Poor"


# def build_score_payload(components: dict, resume_only: bool = False) -> dict:
#     """
#     components = {
#         "skills": int,
#         "experience": int,
#         "keywords": int,
#         "formatting": int
#     }
#     """

#     # ✅ SAFE NORMALIZATION
#     skills = safe_score(components.get("skills"))
#     experience = safe_score(components.get("experience"))
#     keywords = safe_score(components.get("keywords"))
#     formatting = safe_score(components.get("formatting"))

#     # ✅ RESUME-ONLY REWEIGHT
#     if resume_only:
#         weighted_score = (
#             skills * 0.45 +
#             experience * 0.30 +
#             formatting * 0.25
#         )
#     else:
#         weighted_score = (
#             skills * 0.35 +
#             experience * 0.30 +
#             keywords * 0.20 +
#             formatting * 0.15
#         )

#     final_score = calibrate_score(weighted_score)

#     return {
#         "score": final_score,
#         "grade": get_grade(final_score),
#         "confidence": get_confidence_label(final_score),
#         "breakdown": {
#             "skills": skills,
#             "experience": experience,
#             "keywords": keywords,
#             "formatting": formatting
#         }
#     }
