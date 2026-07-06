// Small shared helpers: theme toggle (persisted).
function toggleTheme() {
  const html = document.documentElement;
  const now = html.getAttribute("data-theme");
  const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
  const current = now || (prefersDark ? "dark" : "light");
  const next = current === "dark" ? "light" : "dark";
  html.setAttribute("data-theme", next);
  localStorage.setItem("theme", next);
}
