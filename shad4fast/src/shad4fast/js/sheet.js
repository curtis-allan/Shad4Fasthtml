proc_htmx(".sheet", (elt) => {
  var fragment = document.createDocumentFragment();

  fragment.appendChild(elt);

  document.body.appendChild(fragment);

  const overlay = elt.querySelector(".sheet-overlay");
  const closeIcon = elt.querySelector(".sheet-close-x");
  const closeBtn = elt.querySelector(".sheet-close-button");
  const openBtn = document.querySelector(`button[data-sheet-id=${elt.id}]`);

  function toggleClose() {
    elt.dataset.state = "closed";
    setTimeout(() => (elt.style.display = "none"), 110);
  }

  function openSheet(e) {
    e.preventDefault();
    elt.dataset.state = "open";
    elt.style.display = "flex";
  }

  if (overlay) overlay.addEventListener("mousedown", toggleClose);
  if (closeBtn) closeBtn.addEventListener("mousedown", toggleClose);
  if (closeIcon) closeIcon.addEventListener("mousedown", toggleClose);
  if (openBtn) openBtn.addEventListener("click", (e) => openSheet(e))
});
