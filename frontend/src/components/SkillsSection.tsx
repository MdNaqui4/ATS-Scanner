type Props = {
  title: string;
  skills: string[];
  variant?: "good" | "missing" | "neutral";
};

export default function SkillsSection({
  title,
  skills,
  variant = "neutral",
}: Props) {
  const color =
    variant === "good"
      ? "bg-green-100 text-green-800"
      : variant === "missing"
      ? "bg-red-100 text-red-800"
      : "bg-gray-100 text-gray-800";

  return (
    <div className="bg-white rounded-xl shadow p-6">
      <h3 className="font-semibold mb-3">{title}</h3>

      <div className="flex flex-wrap gap-2">
        {skills.length === 0 ? (
          <span className="text-sm text-gray-500">
            No data available
          </span>
        ) : (
          skills.map((skill) => (
            <span
              key={skill}
              className={`px-3 py-1 rounded-full text-sm font-medium ${color}`}
            >
              {skill}
            </span>
          ))
        )}
      </div>
    </div>
  );
}
