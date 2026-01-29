def generate_quality_feedback(breakdown: dict):
    strengths = []
    improvements = []

    if breakdown["experience"] >= 70:
        strengths.append("Strong and relevant professional experience")

    if breakdown["formatting"] >= 80:
        strengths.append("Well-structured and ATS-friendly resume format")

    if breakdown["skills"] < 70:
        improvements.append("Add more role-specific technical skills")

    if breakdown["keywords"] < 65:
        improvements.append("Improve keyword alignment with target job roles")

    if not improvements:
        improvements.append("Resume is strong overall; fine-tuning can improve competitiveness")

    return {
        "strengths": strengths,
        "improvements": improvements
    }
