export interface SentenceExplainability {
  resume_sentence: string;
  job_sentence?: string;
  score?: number;
}

export type ResumeGrade = "Excellent" | "Good" | "Average" | "Poor";

export interface ATSResponse {
  score: number;

  // NEW
  grade?: ResumeGrade;
  strengths?: string[];
  improvements?: string[];

  resume_skills: string[];
  job_skills: string[];
  missing_skills: string[];

  sentence_explainability: SentenceExplainability[];
}
