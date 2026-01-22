from src.pdf_extractor import extract_text_from_pdf

text = extract_text_from_pdf("data/resumes/1.pdf")
print(text[:1000])
