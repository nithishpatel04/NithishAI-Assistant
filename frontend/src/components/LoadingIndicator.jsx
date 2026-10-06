import { Sparkles } from "lucide-react";

export default function LoadingIndicator() {
  return (
    <div className="msg-row ai">
      <div className="avatar"><Sparkles size={16} /></div>
      <div className="bubble bubble-ai typing" aria-label="Nithish AI is thinking">
        <span /><span /><span />
      </div>
    </div>
  );
}
