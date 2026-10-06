const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || "http://127.0.0.1:8000";

// In dev, "/api" is proxied by Vite to the local backend (backend has no CORS).
const API_URL = import.meta.env.DEV
  ? "/api/chat"
  : `${API_BASE_URL.replace(/\/+$/, "")}/api/chat`;

export async function sendMessage(message) {
  let res;
  try {
    res = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message }),
    });
  } catch {
    throw new Error("Cannot reach the server. Make sure the backend is running.");
  }

  if (!res.ok) {
    throw new Error(`Server error (${res.status}). Please try again.`);
  }

  const data = await res.json();
  return data.response;
}
