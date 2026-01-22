// interface ScoreCardProps {
//     score: number; // 0–1
//   }
  
//   export default function ScoreCard({ score }: ScoreCardProps) {
//     const percent = Math.round(score * 100);
  
//     const getColor = () => {
//       if (percent >= 75) return "bg-green-500";
//       if (percent >= 50) return "bg-yellow-400";
//       return "bg-red-500";
//     };
  
//     return (
//       <div className="bg-white rounded-xl shadow-md p-6">
//         <h2 className="text-lg font-semibold text-gray-700 mb-4">
//           ATS Match Score
//         </h2>
  
//         <div className="flex items-center gap-6">
//           <div className="text-5xl font-bold text-gray-900">
//             {percent}%
//           </div>
  
//           <div className="flex-1">
//             <div className="h-3 bg-gray-200 rounded-full overflow-hidden">
//               <div
//                 className={`h-full ${getColor()} transition-all duration-700`}
//                 style={{ width: `${percent}%` }}
//               />
//             </div>
  
//             <p className="text-sm text-gray-500 mt-2">
//               Based on skills, keywords & relevance
//             </p>
//           </div>
//         </div>
//       </div>
//     );
//   }
type Props = {
    score: number;
  };
  
  export default function ScoreCard({ score }: Props) {
    const percentage = Math.round(score * 100);
  
    const color =
      percentage >= 75
        ? "bg-green-500"
        : percentage >= 50
        ? "bg-yellow-500"
        : "bg-red-500";
  
    return (
      <div className="bg-white rounded-xl shadow p-6">
        <h2 className="text-lg font-semibold mb-4">ATS Match Score</h2>
  
        <div className="w-full bg-gray-200 rounded-full h-4 overflow-hidden">
          <div
            className={`${color} h-4 transition-all duration-700`}
            style={{ width: `${percentage}%` }}
          />
        </div>
  
        <p className="mt-3 text-sm text-gray-600">
          Match strength:{" "}
          <span className="font-semibold">{percentage}%</span>
        </p>
      </div>
    );
  }
  