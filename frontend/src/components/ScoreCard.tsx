type Props = {
  score: number;
};

export default function ScoreCard({ score }: Props) {
  const percentage = Math.round(score);

  const color =
    percentage >= 75
      ? "bg-green-500"
      : percentage >= 50
      ? "bg-yellow-500"
      : "bg-red-500";

  const label =
    percentage >= 75
      ? "Strong ATS Compatibility"
      : percentage >= 50
      ? "Moderate ATS Compatibility"
      : "Low ATS Compatibility";

  return (
    <div className="bg-white rounded-xl shadow p-6 space-y-3">
      <div className="flex justify-between items-center">
        <h2 className="text-lg font-semibold">ATS Match Score</h2>
        <span className="text-xl font-bold">{percentage}%</span>
      </div>

      <div className="w-full bg-gray-200 rounded h-3 overflow-hidden">
        <div
          className={`${color} h-3 transition-all duration-500`}
          style={{ width: `${percentage}%` }}
        />
      </div>

      <p className="text-sm text-gray-600">{label}</p>
    </div>
  );
}
