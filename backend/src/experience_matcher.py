import re

def extract_years(text: str) -> int:
    matches = re.findall(r'(\d+)\+?\s*years?', text.lower())
    return max(map(int, matches)) if matches else 0


def experience_alignment_score(resume_text: str, jd_text: str | None = None) -> float:
    resume_years = extract_years(resume_text)

    if not jd_text:
        return min(resume_years / 10, 1.0)  # resume-only mode

    jd_years = extract_years(jd_text)

    if jd_years == 0:
        return 1.0

    return min(resume_years / jd_years, 1.0)
