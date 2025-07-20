const sid = crypto.randomUUID();
const chat = document.getElementById("chat");
const form = document.getElementById("chat-form");
const input = document.getElementById("message");

const append = (role, text) => {
  const div = document.createElement("div");
  div.className = role === "user" ? "text-right" : "text-left";
  div.textContent = text;
  chat.appendChild(div);
  chat.scrollTop = chat.scrollHeight;
};

form.addEventListener("submit", async e => {
  e.preventDefault();
  const text = input.value.trim();
  if (!text) return;
  append("user", text);
  input.value = "";
  const res = await fetch("/api/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ session_id: sid, message: text })
  });
  const data = await res.json();
  append("assistant", data.reply);
});
