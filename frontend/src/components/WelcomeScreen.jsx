import { Droplets, Code2, CloudSun, Lightbulb, Languages } from "lucide-react";

const SUGGESTIONS = [
  { icon: CloudSun, title: "Check the weather", text: "What's the weather in Chennai today?" },
  { icon: Code2, title: "Help with code", text: "Explain how Python decorators work" },
  { icon: Lightbulb, title: "Get ideas", text: "Give me 5 creative project ideas" },
  { icon: Languages, title: "Multilingual", text: "வணக்கம்! நீங்கள் எப்படி இருக்கிறீர்கள்?" },
];

export default function WelcomeScreen({ onSelect }) {
  return (
    <div className="welcome">
      <div className="welcome-logo"><Droplets size={34} /></div>
      <h2>How can I help you today?</h2>
      <p>Ask me anything — I'm Nithish AI, your assistant.</p>
      <div className="cards">
        {SUGGESTIONS.map(({ icon: Icon, title, text }) => (
          <button key={title} className="card" onClick={() => onSelect(text)}>
            <span className="card-icon"><Icon size={18} /></span>
            <strong>{title}</strong>
            <span>{text}</span>
          </button>
        ))}
      </div>
    </div>
  );
}
