function resetDialogAndSheet() {
    document.querySelectorAll('[role="dialog"], .sheet').forEach(element => {
        element.dataset.state = 'closed';
        element.style.display = 'none';
    });
}

htmx.on('htmx:historyRestore', function() {
    resetDialogAndSheet();
});

htmx.on('htmx:beforeSwap', function() {
  resetDialogAndSheet();
})

function toggleCheckbox(e) {
  e.dataset.state = e.dataset.state === "unchecked" ? "checked" : "unchecked";
  e.querySelector("input").checked = e.dataset.state === "checked";
}

function proc_htmx(sel, func) {
  htmx.onLoad((elt) => {
    const elements = any(sel, elt, false);
    if (elt.matches && elt.matches(sel)) elements.unshift(elt);
    elements.forEach(func);
  });
}

proc_htmx(".preventdbclick", (elt) => {
  elt.addEventListener("mousedown", (event) => {
    if (event.detail > 1) event.preventDefault();
  });
});
