def infer_reason(resume, jd):
    r = resume.lower()
    j = jd.lower()

    if any(k in r for k in ["react", "angular", "vue"]):
        return "Matches front-end framework experience"
    if "performance" in r:
        return "Aligns with performance optimization requirements"
    if "collaborat" in r:
        return "Demonstrates cross-functional collaboration"
    return "Relevant experience aligned with job responsibilities"
