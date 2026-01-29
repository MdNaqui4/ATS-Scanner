type Props = {
    grade: "Excellent" | "Good" | "Average" | "Poor";
  };
  
  const gradeStyles: Record<Props["grade"], string> = {
    Excellent: "bg-green-100 text-green-700 border-green-300",
    Good: "bg-blue-100 text-blue-700 border-blue-300",
    Average: "bg-yellow-100 text-yellow-700 border-yellow-300",
    Poor: "bg-red-100 text-red-700 border-red-300",
  };
  
  export default function QualityGrade({ grade }: Props) {
    return (
      <div
        className={`inline-flex items-center px-4 py-2 rounded-full border text-sm font-semibold ${gradeStyles[grade]}`}
      >
        Resume Quality: {grade}
      </div>
    );
  }
  