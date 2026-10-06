import { useEffect, useRef } from "react";
import WelcomeScreen from "./WelcomeScreen.jsx";
import MessageBubble from "./MessageBubble.jsx";
import LoadingIndicator from "./LoadingIndicator.jsx";

export default function ChatWindow({ messages, loading, onSuggestion }) {
  const endRef = useRef(null);

  useEffect(() => {
    endRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, loading]);

  return (
    <div className="chat-window">
      {messages.length === 0 && !loading ? (
        <WelcomeScreen onSelect={onSuggestion} />
      ) : (
        <div className="messages">
          {messages.map((m) => (
            <MessageBubble key={m.id} message={m} />
          ))}
          {loading && <LoadingIndicator />}
          <div ref={endRef} />
        </div>
      )}
    </div>
  );
}
