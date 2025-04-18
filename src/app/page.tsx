// src/app/page.tsx
export default function HomePage() {
  return (
    <main className="min-h-screen bg-gray-50 p-6 flex flex-col items-center justify-center">
      <div className="w-full max-w-2xl bg-white shadow-xl rounded-2xl p-6">
        <h1 className="text-2xl font-bold mb-4">Ask AI Anything ✨</h1>
        <textarea
          placeholder="What would you like to ask?"
          className="w-full border p-3 rounded-md focus:outline-none focus:ring focus:ring-blue-300 resize-none min-h-[100px]"
        />
        <button className="mt-4 px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 transition">
          Send
        </button>
      </div>
    </main>
  );
}
