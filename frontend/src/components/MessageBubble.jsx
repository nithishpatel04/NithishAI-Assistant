import { Sparkles, User } from "lucide-react";

export default function MessageBubble({ message }) {
  const isUser = message.role === "user";
  return (
    <div className={`msg-row ${isUser ? "user" : "ai"}`}>
      <div className="avatar">{isUser ? <User size={16} /> : <Sparkles size={16} />}</div>
      <div className={`bubble ${isUser ? "bubble-user" : "bubble-ai"} ${message.error ? "bubble-error" : ""}`}>
        {message.content}
      </div>
    </div>
  );
}
