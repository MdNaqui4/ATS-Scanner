type Props = {
    strengths?: string[];
    improvements?: string[];
  };
  
  export default function StrengthsImprovements({
    strengths = [],
    improvements = [],
  }: Props) {
    return (
      <div className="grid md:grid-cols-2 gap-6">
        {/* Strengths */}
        <div className="bg-white rounded-xl shadow p-6">
          <h3 className="text-lg font-semibold mb-3 text-green-700">
            ✅ Strengths
          </h3>
  
          {strengths.length === 0 ? (
            <p className="text-sm text-gray-500">
              No major strengths detected yet.
            </p>
          ) : (
            <ul className="list-disc pl-5 space-y-2 text-sm">
              {strengths.map((s, i) => (
                <li key={i}>{s}</li>
              ))}
            </ul>
          )}
        </div>
  
        {/* Improvements */}
        <div className="bg-white rounded-xl shadow p-6">
          <h3 className="text-lg font-semibold mb-3 text-red-700">
            ⚠️ Improvements
          </h3>
  
          {improvements.length === 0 ? (
            <p className="text-sm text-gray-500">
              No improvement suggestions available.
            </p>
          ) : (
            <ul className="list-disc pl-5 space-y-2 text-sm">
              {improvements.map((s, i) => (
                <li key={i}>{s}</li>
              ))}
            </ul>
          )}
        </div>
      </div>
    );
  }
  