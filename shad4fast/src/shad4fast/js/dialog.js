proc_htmx(".dialog", (dialog) => {

  var fragment = document.createDocumentFragment();

  fragment.appendChild(dialog);

  document.body.appendChild(fragment);

  function openDialog(e) {
    e.preventDefault();
    dialog.dataset.state = "open";
    dialog.classList.remove('hidden');
  }

  function toggleClose(e) {
    e.stopPropagation();
    dialog.dataset.state = "closed";
  }

  const overlay = dialog.querySelector(".dialog-overlay");

  if (overlay) overlay.addEventListener("mousedown",(e) => toggleClose(e));

  dialog.addEventListener("animationend", () => {
    if (dialog.dataset.state === "closed") dialog.classList.add('hidden');
});

document.addEventListener("click", (e) => {
    if (e.target.closest(".dialog-close-button")) toggleClose(e); 
    if (e.target.closest(`button[data-dialog-id=${dialog.id}]`)) openDialog(e);
});
})

