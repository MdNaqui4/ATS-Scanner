"use client";

import { useState } from "react";
import { analyzeResume } from "@/lib/api";
import { useRouter } from "next/navigation";

export default function UploadForm() {
  const [resume, setResume] = useState<File | null>(null);
  const [jd, setJd] = useState("");
  const [mode, setMode] = useState<"resume_only" | "resume_vs_jd">(
    "resume_vs_jd"
  );
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const router = useRouter();

  async function handleSubmit() {
    if (!resume) {
      setError("Please upload a resume PDF");
      return;
    }

    if (mode === "resume_vs_jd" && !jd.trim()) {
      setError("Please paste a job description");
      return;
    }

    try {
      setLoading(true);
      setError(null);

      const result = await analyzeResume(
        resume,
        mode === "resume_only" ? "" : jd
      );

      sessionStorage.setItem("ats_result", JSON.stringify(result));
      router.push("/analyze");
    } catch (err) {
      console.error(err);
      setError("Failed to analyze resume. Please try again.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="space-y-5 max-w-xl mx-auto">
      {/* Resume upload */}
      <input
        type="file"
        accept=".pdf"
        onChange={(e) => setResume(e.target.files?.[0] || null)}
        className="block w-full"
      />

      {/* Mode toggle */}
      <div className="flex gap-6 text-sm">
        <label className="flex items-center gap-2">
          <input
            type="radio"
            checked={mode === "resume_vs_jd"}
            onChange={() => setMode("resume_vs_jd")}
          />
          Resume vs Job Description
        </label>

        <label className="flex items-center gap-2">
          <input
            type="radio"
            checked={mode === "resume_only"}
            onChange={() => setMode("resume_only")}
          />
          Resume Only Scan
        </label>
      </div>

      {/* JD textarea */}
      {mode === "resume_vs_jd" && (
        <textarea
          placeholder="Paste Job Description"
          className="w-full h-40 border rounded p-3"
          value={jd}
          onChange={(e) => setJd(e.target.value)}
        />
      )}

      {error && <p className="text-sm text-red-600">{error}</p>}

      <button
        onClick={handleSubmit}
        disabled={loading}
        className="bg-black text-white px-6 py-2 rounded disabled:opacity-50"
      >
        {loading ? "Analyzing..." : "Analyze Resume"}
      </button>
    </div>
  );
}
