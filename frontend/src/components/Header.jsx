import { Menu, Sparkles } from "lucide-react";

export default function Header({ onMenu }) {
  return (
    <header className="header">
      <button className="icon-btn mobile-only" onClick={onMenu} aria-label="Open menu">
        <Menu size={20} />
      </button>
      <div className="header-avatar"><Sparkles size={18} /></div>
      <div className="header-text">
        <h1>Nithish AI</h1>
        <span className="status"><i className="dot" /> Online</span>
      </div>
    </header>
  );
}
