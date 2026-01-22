import { ATSResponse } from "@/types/ats";

export async function analyzeResume(
  resume: File,
  jobDescription: string
): Promise<ATSResponse> {
  const formData = new FormData();
  formData.append("resume", resume);
  formData.append("job_description", jobDescription);

  const res = await fetch("http://127.0.0.1:8000/api/resume/analyze", {
    method: "POST",
    body: formData,
  });

  if (!res.ok) {
    throw new Error("Failed to analyze resume");
  }

  const data = await res.json();

  return {
    score: data.score ?? 0,
    resume_skills: data.resume_skills ?? [],
    job_skills: data.job_skills ?? [],
    missing_skills: data.missing_skills ?? [],
    sentence_explainability: data.sentence_explainability ?? [],
  };
}
