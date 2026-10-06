import { useState } from "react";
import Sidebar from "./components/Sidebar.jsx";
import Header from "./components/Header.jsx";
import ChatWindow from "./components/ChatWindow.jsx";
import ChatInput from "./components/ChatInput.jsx";
import { sendMessage } from "./services/api.js";

export default function App() {
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);
  const [collapsed, setCollapsed] = useState(false);
  const [mobileOpen, setMobileOpen] = useState(false);

  const handleSend = async (text) => {
    const trimmed = text.trim();
    if (!trimmed || loading) return;

    setMessages((m) => [...m, { id: crypto.randomUUID(), role: "user", content: trimmed }]);
    setLoading(true);
    try {
      const reply = await sendMessage(trimmed);
      setMessages((m) => [...m, { id: crypto.randomUUID(), role: "ai", content: reply }]);
    } catch (err) {
      setMessages((m) => [
        ...m,
        { id: crypto.randomUUID(), role: "ai", content: err.message, error: true },
      ]);
    } finally {
      setLoading(false);
    }
  };

  const newChat = () => {
    setMessages([]);
    setMobileOpen(false);
  };

  return (
    <div className="app">
      <Sidebar
        collapsed={collapsed}
        mobileOpen={mobileOpen}
        onToggle={() => setCollapsed((c) => !c)}
        onCloseMobile={() => setMobileOpen(false)}
        onNewChat={newChat}
      />
      <main className="main">
        <Header onMenu={() => setMobileOpen(true)} />
        <ChatWindow messages={messages} loading={loading} onSuggestion={handleSend} />
        <ChatInput onSend={handleSend} disabled={loading} />
      </main>
    </div>
  );
}
