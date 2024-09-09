proc_htmx(".dialog", (dialog) => {
  var fragment = document.createDocumentFragment();

  fragment.appendChild(dialog);

  document.body.appendChild(fragment);

  const overlay = dialog.querySelector(".dialog-overlay");
  const closeIcon = dialog.querySelector(".dialog-close-btn");
  const closeBtn = dialog.querySelector(".dialog-close-button");
  const openBtn = document.querySelector(`button[data-dialog-id=${dialog.id}]`)

  function openDialog() {
    dialog.dataset.state = "open";
    dialog.style.display = "flex";
  }


  function toggleClose() {
    dialog.dataset.state = "closed";
    setTimeout(() => (dialog.style.display = "none"), 110);
  }

  if (overlay) overlay.addEventListener("mousedown", toggleClose);
  if (closeBtn) closeBtn.addEventListener("mousedown", toggleClose);
  if (closeIcon) closeIcon.addEventListener("mousedown", toggleClose);
  if (openBtn) openBtn.addEventListener("click", openDialog);
});