import { Droplets, Plus, MessageSquare, Settings, PanelLeftClose, PanelLeftOpen, X } from "lucide-react";

const HISTORY = [
  "Plan my weekly schedule",
  "Explain quantum computing",
  "வணக்கம் - தமிழ் உதவி",
  "Weather in Chennai",
  "Debug my Python code",
];

export default function Sidebar({ collapsed, mobileOpen, onToggle, onCloseMobile, onNewChat }) {
  return (
    <>
      {mobileOpen && <div className="backdrop" onClick={onCloseMobile} />}
      <aside className={`sidebar ${collapsed ? "collapsed" : ""} ${mobileOpen ? "open" : ""}`}>
        <div className="sidebar-top">
          <div className="brand">
            <span className="brand-logo"><Droplets size={20} /></span>
            {!collapsed && <span className="brand-name">Nithish AI</span>}
          </div>
          <button className="icon-btn desktop-only" onClick={onToggle} aria-label="Toggle sidebar">
            {collapsed ? <PanelLeftOpen size={18} /> : <PanelLeftClose size={18} />}
          </button>
          <button className="icon-btn mobile-only" onClick={onCloseMobile} aria-label="Close menu">
            <X size={18} />
          </button>
        </div>

        <button className="new-chat" onClick={onNewChat} title="New Chat">
          <Plus size={18} />
          {!collapsed && <span>New Chat</span>}
        </button>

        {!collapsed && <div className="history-label">Recent</div>}
        <nav className="history">
          {HISTORY.map((t) => (
            <button key={t} className="history-item" title={t}>
              <MessageSquare size={16} />
              {!collapsed && <span>{t}</span>}
            </button>
          ))}
        </nav>

        <button className="history-item settings" title="Settings">
          <Settings size={16} />
          {!collapsed && <span>Settings</span>}
        </button>
      </aside>
    </>
  );
}
