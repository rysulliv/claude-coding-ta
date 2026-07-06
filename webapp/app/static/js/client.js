// Live Claude Code client: stream one turn from the server's SSE endpoint,
// which drives `claude --resume ... --output-format stream-json` under the hood.

(function () {
  const transcript = document.getElementById("transcript");
  const input = document.getElementById("msg");
  const sendBtn = document.getElementById("send");
  const permSel = document.getElementById("perm");
  const forkBox = document.getElementById("fork");
  if (!input) return;

  function el(tag, cls, text) {
    const e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text != null) e.textContent = text;
    return e;
  }

  function addMessage(role, avatar) {
    const empty = document.getElementById("empty");
    if (empty) empty.remove();
    const wrap = el("div", "msg " + role);
    wrap.appendChild(el("div", "avatar", avatar));
    const bubble = el("div", "bubble");
    wrap.appendChild(bubble);
    transcript.appendChild(wrap);
    scroll();
    return bubble;
  }

  function scroll() { window.scrollTo({ top: document.body.scrollHeight, behavior: "smooth" }); }

  function setBusy(b) {
    sendBtn.disabled = b;
    sendBtn.textContent = b ? "…" : "Send ▸";
    input.disabled = b;
  }

  async function send() {
    const message = input.value.trim();
    if (!message || sendBtn.disabled) return;

    const userBubble = addMessage("user", "🧑");
    userBubble.appendChild(el("div", "bubble-text", message));
    input.value = "";
    setBusy(true);

    const bubble = addMessage("assistant", "✳️");
    const textNode = el("div", "bubble-text", "");
    bubble.appendChild(textNode);
    let gotText = false;

    const body = new URLSearchParams();
    body.set("message", message);
    body.set("session_id", window.MENTOR_SESSION_ID || "");
    body.set("permission_mode", permSel ? permSel.value : "default");
    body.set("fork", forkBox && forkBox.checked ? "true" : "false");

    try {
      const resp = await fetch("/api/client/stream", { method: "POST", body });
      const reader = resp.body.getReader();
      const decoder = new TextDecoder();
      let buffer = "";

      while (true) {
        const { value, done } = await reader.read();
        if (done) break;
        buffer += decoder.decode(value, { stream: true });
        const chunks = buffer.split("\n\n");
        buffer = chunks.pop();
        for (const chunk of chunks) {
          const line = chunk.trim();
          if (!line.startsWith("data:")) continue;
          let ev;
          try { ev = JSON.parse(line.slice(5).trim()); } catch { continue; }
          handle(ev, textNode, bubble, () => { gotText = true; });
        }
      }
    } catch (err) {
      bubble.appendChild(toolLine("err", "⚠️ " + err.message));
    } finally {
      if (!gotText && !textNode.textContent) textNode.remove();
      setBusy(false);
      input.focus();
    }
  }

  function toolLine(kind, text) {
    return el("div", "tool " + kind, text);
  }

  function handle(ev, textNode, bubble, markText) {
    switch (ev.type) {
      case "text":
        textNode.textContent += ev.text;
        markText();
        scroll();
        break;
      case "tool_use": {
        let s = "🔧 " + ev.name;
        if (ev.input && Object.keys(ev.input).length) {
          const j = JSON.stringify(ev.input);
          s += " · " + (j.length > 160 ? j.slice(0, 160) + "…" : j);
        }
        bubble.appendChild(toolLine("", s));
        scroll();
        break;
      }
      case "tool_result":
        bubble.appendChild(toolLine("result" + (ev.is_error ? " err" : ""), (ev.text || "").slice(0, 1200)));
        scroll();
        break;
      case "init":
        if (ev.session_id) updateSession(ev.session_id);
        break;
      case "result":
        if (ev.session_id) updateSession(ev.session_id);
        if (ev.is_error && ev.text) bubble.appendChild(toolLine("err", "⚠️ " + ev.text));
        break;
      case "error":
        bubble.appendChild(toolLine("err", "⚠️ " + (ev.message || "stream error")));
        break;
    }
  }

  function updateSession(id) {
    window.MENTOR_SESSION_ID = id;
    // reflect it in the URL without reloading, so a refresh resumes correctly
    const url = new URL(window.location);
    if (url.searchParams.get("session") !== id) {
      url.searchParams.set("session", id);
      history.replaceState({}, "", url);
    }
  }

  sendBtn.addEventListener("click", send);
  input.addEventListener("keydown", function (e) {
    if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); send(); }
  });
})();
