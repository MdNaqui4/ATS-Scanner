# src/scoring.py

from typing import Dict


# -----------------------------
# RAW SCORE WEIGHTS (LOCKED)
# -----------------------------
WEIGHTS = {
    "skills": 0.35,
    "experience": 0.30,
    "keywords": 0.20,
    "formatting": 0.15,
}


# -----------------------------
# FINAL SCORE CALCULATION
# -----------------------------
def calculate_final_score(components: Dict[str, float]) -> int:
    """
    components example:
    {
        "skills": 78,
        "experience": 72,
        "keywords": 65,
        "formatting": 80
    }
    """

    raw_score = (
        components.get("skills", 0) * WEIGHTS["skills"]
        + components.get("experience", 0) * WEIGHTS["experience"]
        + components.get("keywords", 0) * WEIGHTS["keywords"]
        + components.get("formatting", 0) * WEIGHTS["formatting"]
    )

    return calibrate_score(raw_score)


# -----------------------------
# SCORE CALIBRATION (VERY IMPORTANT)
# -----------------------------
def calibrate_score(score: float) -> int:
    """
    Human-aligned smoothing:
    - Minimum realistic score: 35
    - Maximum believable score: 95
    """

    calibrated = max(35, min(95, round(score)))
    return calibrated


# -----------------------------
# CONFIDENCE LABEL
# -----------------------------
def confidence_label(score: int) -> str:
    if score >= 80:
        return "Excellent Fit"
    elif score >= 65:
        return "Good Match"
    elif score >= 50:
        return "Partial Match"
    else:
        return "Needs Improvement"


# -----------------------------
# RESUME GRADE
# -----------------------------
def resume_grade(score: int) -> str:
    if score >= 85:
        return "A+"
    elif score >= 75:
        return "A"
    elif score >= 65:
        return "B"
    elif score >= 55:
        return "C"
    else:
        return "D"


# -----------------------------
# MASTER SCORING OUTPUT
# -----------------------------
def build_score_payload(components: Dict[str, float]) -> Dict:
    """
    Final object consumed by frontend
    """

    final_score = calculate_final_score(components)

    return {
        "final_score": final_score,
        "grade": resume_grade(final_score),
        "confidence": confidence_label(final_score),
        "breakdown": components,
    }
