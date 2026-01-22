import UploadForm from "@/components/UploadForm";

export default function Home() {
  return (
    <main className="max-w-3xl mx-auto p-10">
      <h1 className="text-3xl font-bold mb-4">
        AI ATS Resume Analyzer
      </h1>
      <p className="mb-6 text-gray-600">
        Upload your resume and job description to get an ATS-style match score,
        missing skills, and sentence-level explanations.
      </p>

      <UploadForm />
    </main>
  );
}
