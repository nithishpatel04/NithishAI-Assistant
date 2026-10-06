import { useRef, useState } from "react";
import { SendHorizontal } from "lucide-react";

export default function ChatInput({ onSend, disabled }) {
  const [value, setValue] = useState("");
  const ref = useRef(null);
  const composing = useRef(false);

  const resize = () => {
    const el = ref.current;
    if (!el) return;
    el.style.height = "auto";
    el.style.height = Math.min(el.scrollHeight, 180) + "px";
  };

  const submit = () => {
    if (!value.trim() || disabled) return;
    onSend(value);
    setValue("");
    requestAnimationFrame(resize);
  };

  const onKeyDown = (e) => {
    // Ignore Enter while an IME (e.g. Tamil, Japanese) composition is active.
    if (e.key === "Enter" && !e.shiftKey && !composing.current && !e.nativeEvent.isComposing) {
      e.preventDefault();
      submit();
    }
  };

  return (
    <div className="input-wrap">
      <div className="input-box">
        <textarea
          ref={ref}
          rows={1}
          value={value}
          placeholder="Message Nithish AI..."
          onChange={(e) => { setValue(e.target.value); resize(); }}
          onKeyDown={onKeyDown}
          onCompositionStart={() => (composing.current = true)}
          onCompositionEnd={() => (composing.current = false)}
        />
        <button className="send-btn" onClick={submit} disabled={disabled || !value.trim()} aria-label="Send">
          <SendHorizontal size={18} />
        </button>
      </div>
      <p className="hint">Enter to send · Shift+Enter for a new line</p>
    </div>
  );
}
