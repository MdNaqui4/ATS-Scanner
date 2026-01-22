"use client";

import { useState } from "react";
import { analyzeResume } from "@/lib/api";
import { useRouter } from "next/navigation";

export default function UploadForm() {
  const [resume, setResume] = useState<File | null>(null);
  const [jd, setJd] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const router = useRouter();

  async function handleSubmit() {
    if (!resume || !jd) {
      setError("Please upload resume and paste job description");
      return;
    }

    try {
      setLoading(true);
      setError(null);

      const result = await analyzeResume(resume, jd);

      sessionStorage.setItem("ats_result", JSON.stringify(result));
      router.push("/analyze");
    } catch (err) {
      console.error(err);
      setError("Failed to analyze resume. Try again.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="space-y-4 max-w-xl mx-auto">
      <input
        type="file"
        accept=".pdf"
        onChange={(e) => setResume(e.target.files?.[0] || null)}
        className="block w-full"
      />

      <textarea
        placeholder="Paste Job Description"
        className="w-full h-40 border rounded p-3"
        value={jd}
        onChange={(e) => setJd(e.target.value)}
      />

      {error && (
        <p className="text-sm text-red-600">{error}</p>
      )}

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
