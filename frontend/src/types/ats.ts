export interface SentenceExplainability {
  resume_sentence: string;
  job_sentence: string;
  score?: number;
}

export interface ATSResponse {
  score: number;
  resume_skills: string[];
  job_skills: string[];
  missing_skills: string[];
  sentence_explainability: SentenceExplainability[];
}
