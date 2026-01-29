"use client";

import { useEffect, useState } from "react";
import ScoreCard from "@/components/ScoreCard";
import SkillsSection from "@/components/SkillsSection";
import SentenceMatches from "@/components/SentenceMatches";
import QualityGrade from "@/components/QualityGrade";
import StrengthsImprovements from "@/components/StrengthsImprovements";
import { ATSResponse } from "@/types/ats";

export default function AnalyzePage() {
  const [data, setData] = useState<ATSResponse | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    try {
      const stored = sessionStorage.getItem("ats_result");
      if (!stored) throw new Error("No result found");

      const parsed: ATSResponse = JSON.parse(stored);
      setData(parsed);
    } catch (err) {
      console.error(err);
      setError("No analysis data found. Please upload again.");
    } finally {
      setLoading(false);
    }
  }, []);

  if (loading) {
    return (
      <div className="flex justify-center items-center h-[60vh]">
        <p className="text-gray-500">Analyzing resume…</p>
      </div>
    );
  }

  if (error || !data) {
    return (
      <div className="max-w-xl mx-auto mt-20 bg-red-50 border border-red-200 p-6 rounded-xl">
        <h2 className="font-semibold text-red-700 mb-2">
          Something went wrong
        </h2>
        <p className="text-sm text-red-600">
          {error ?? "Unexpected error occurred"}
        </p>
      </div>
    );
  }

  const matchedSkills = data.resume_skills.filter(skill =>
    data.job_skills.includes(skill)
  );

  return (
    <div className="max-w-5xl mx-auto px-4 py-8 space-y-8">
      {/* Score + Grade */}
      <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-4">
        <ScoreCard score={data.score} />
        {data.grade && <QualityGrade grade={data.grade} />}
      </div>

      {/* Skills */}
      <div className="grid md:grid-cols-2 gap-6">
        <SkillsSection
          title="Matched Skills"
          skills={matchedSkills}
          variant="good"
        />

        <SkillsSection
          title="Missing Skills"
          skills={data.missing_skills}
          variant="missing"
        />
      </div>

      {/* Strengths & Improvements */}
      <StrengthsImprovements
        strengths={data.strengths}
        improvements={data.improvements}
      />

      {/* Sentence level explanation */}
      <SentenceMatches matches={data.sentence_explainability} />
    </div>
  );
}
