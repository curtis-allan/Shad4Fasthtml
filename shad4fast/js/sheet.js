function openSheet(button) {
    const sheet = document.querySelector(`#${button.getAttribute("sheet-id")}`);
    sheet.dataset.state = "open";
    sheet.style.display = "flex";
  }
  
  proc_htmx(".sheet", (elt) => {
    var fragment = document.createDocumentFragment();
  
    fragment.appendChild(elt);
  
    document.body.appendChild(fragment);
  
    const overlay = elt.querySelector(".sheet-overlay");
    const closeIcon = elt.querySelector(".sheet-close-x");
    const closeBtn = elt.querySelector(".sheet-close-button");
  
    function toggleClose() {
      elt.dataset.state = "closed";
      setTimeout(() => (elt.style.display = "none"), 110);
    }
  
    if (overlay) overlay.addEventListener("mousedown", toggleClose);
    if (closeBtn) closeBtn.addEventListener("mousedown", toggleClose);
    if (closeIcon) closeIcon.addEventListener("mousedown", toggleClose);
  });
  