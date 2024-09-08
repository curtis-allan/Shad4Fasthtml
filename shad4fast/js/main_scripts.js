function resetDialogAndSheet() {
    document.querySelectorAll('[role="dialog"], .sheet').forEach(element => {
        element.dataset.state = 'closed';
        element.style.display = 'none';
    });
}

htmx.on('htmx:historyRestore', function() {
    resetDialogAndSheet();
});

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


if(!window.themeManager){
  window.themeManager = {
      updateTheme: () => {
          const isDark = document.documentElement.classList.contains('dark') || localStorage.theme === 'dark';
          document.querySelectorAll('zero-md').forEach(el => 
              el.shadowRoot?.querySelectorAll('.light-theme, .dark-theme').forEach(link => 
                  link.disabled = isDark !== link.classList.contains('dark-theme')
              )
          );
      },
      init: () => {
          const update = window.themeManager.updateTheme;
          document.addEventListener('zero-md-rendered', ({target}) => target.shadowRoot && update());
          new MutationObserver(update).observe(document.documentElement, {attributes: true, attributeFilter: ['class']});
          window.addEventListener('storage', update);
          update();
      }
  };
  window.themeManager.init();
}

function setTheme(theme) {
    localStorage.theme = theme;
    document.documentElement.classList.toggle('dark', theme === 'dark');
}

function initTheme() {
    const theme = localStorage.theme || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
    setTheme(theme);
}

document.addEventListener('DOMContentLoaded', () => {
    document.body.addEventListener('click', function(event) {
        const themeToggle = event.target.closest('.theme-toggle');
        if (themeToggle) {
            event.preventDefault();
            const newTheme = document.documentElement.classList.contains('dark') ? 'light' : 'dark';
            setTheme(newTheme);
        }
    });

});

initTheme();

