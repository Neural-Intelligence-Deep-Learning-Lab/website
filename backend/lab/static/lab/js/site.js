(() => {
  const root = document.documentElement;
  const theme = document.querySelector(".theme-button");
  const menu = document.querySelector(".menu-button");
  const links = document.querySelector(".nav-links");
  theme?.addEventListener("click", () => {
    const next = root.dataset.theme === "dark" ? "light" : "dark";
    root.dataset.theme = next;
    localStorage.setItem("nidl-theme", next);
  });
  menu?.addEventListener("click", () => {
    const open = links.classList.toggle("open");
    menu.setAttribute("aria-expanded", String(open));
  });
  const search = document.querySelector("#publication-search");
  const year = document.querySelector("#publication-year");
  const noResults = document.querySelector("#no-results");
  const filter = () => {
    if (!search) return;
    const query = search.value.toLowerCase();
    let visible = 0;
    document.querySelectorAll(".searchable").forEach((item) => {
      const matches = item.textContent.toLowerCase().includes(query) &&
        (year.value === "all" || item.dataset.year === year.value);
      item.hidden = !matches;
      if (matches) visible += 1;
    });
    noResults.hidden = visible !== 0;
  };
  search?.addEventListener("input", filter);
  year?.addEventListener("change", filter);
})();
