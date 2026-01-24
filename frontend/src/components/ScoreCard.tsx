type Props = {
  score: number;
};

export default function ScoreCard({ score }: Props) {
  const percentage = Math.round(score);

  const color =
    percentage >= 70
      ? "bg-green-500"
      : percentage >= 40
      ? "bg-yellow-500"
      : "bg-red-500";

  const label =
    percentage >= 70
      ? "Strong ATS Match"
      : percentage >= 40
      ? "Average ATS Match"
      : "Weak ATS Match";

  return (
    <div className="bg-white rounded-xl shadow p-6">
      <h2 className="text-lg font-semibold mb-2">ATS Score</h2>

      <div className="w-full bg-gray-200 rounded h-4 overflow-hidden">
        <div
          className={`${color} h-4`}
          style={{ width: `${percentage}%` }}
        />
      </div>

      <div className="flex justify-between mt-2 text-sm text-gray-600">
        <span>{percentage}%</span>
        <span>{label}</span>
      </div>
    </div>
  );
}
