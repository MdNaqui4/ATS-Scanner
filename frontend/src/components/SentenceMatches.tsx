import { SentenceExplainability } from "@/types/ats";

type Props = {
  matches: SentenceExplainability[];
};

export default function SentenceMatches({ matches }: Props) {
  return (
    <div className="space-y-4">
      <h2 className="text-lg font-semibold">Resume ↔ Job Matches</h2>

      {matches.length === 0 && (
        <p className="text-sm text-gray-500">
          No strong sentence-level matches found.
        </p>
      )}

      {matches.map((m, i) => (
        <div
          key={i}
          className="bg-white rounded-xl shadow p-4 space-y-2"
        >
          <div>
            <p className="text-xs uppercase text-gray-400">Resume</p>
            <p className="text-sm">{m.resume_sentence}</p>
          </div>

          <div>
            <p className="text-xs uppercase text-gray-400">Job Description</p>
            <p className="text-sm text-gray-700">
              {m.resume_sentence}
            </p>
          </div>

          <p className="text-xs text-gray-500">
            Similarity: {(m.score ? m.score * 100 : 0).toFixed(0)}%
          </p>
        </div>
      ))}
    </div>
  );
}
