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

function openDialog(button) {
  const dialog = document.querySelector(`#${button.getAttribute("dialog-id")}`);
  dialog.dataset.state = "open";
  dialog.style.display = "flex";
}

proc_htmx(".dialog", (dialog) => {
  var fragment = document.createDocumentFragment();

  fragment.appendChild(dialog);

  document.body.appendChild(fragment);

  const overlay = dialog.querySelector(".dialog-overlay");
  const closeIcon = dialog.querySelector(".dialog-close-btn");
  const closeBtn = dialog.querySelector(".dialog-close-button");

  function toggleClose() {
    dialog.dataset.state = "closed";
    setTimeout(() => (dialog.style.display = "none"), 110);
  }

  if (overlay) overlay.addEventListener("mousedown", toggleClose);
  if (closeBtn) closeBtn.addEventListener("mousedown", toggleClose);
  if (closeIcon) closeIcon.addEventListener("mousedown", toggleClose);
});

proc_htmx("#toast-container", function (toast) {
  let dismissTimeout;
  const closeButton = toast.querySelector(".toast-close-button");
  const duration = 6000;

  function dismissToast() {
    clearTimeout(dismissTimeout);
    toast.style.transform = "translateX(100%)";
    setTimeout(() => toast.remove(), 300);
  }

  function resetTimer() {
    clearTimeout(dismissTimeout);
    dismissTimeout = setTimeout(dismissToast, duration);
  }

  // Mouse drag functionality
  let isDragging = false;
  let startX;
  let originalTransform;
  const threshold = 100;

  toast.addEventListener("mousedown", (e) => {
    e.preventDefault(); // Prevent text selection
    toast.style.transition = "none";
    isDragging = true;
    startX = e.clientX;
    originalTransform = window.getComputedStyle(toast).transform;
  });

  toast.addEventListener("mousemove", (e) => {
    if (!isDragging) return;
    resetTimer();
    let deltaX = e.clientX - startX;
    if (deltaX > 0) {
      toast.style.transform = `translateX(${deltaX}px)`;
    }
  });

  toast.addEventListener("mouseup", (e) => {
    if (!isDragging) return;
    toast.style.transition = "transform 0.2s";
    isDragging = false;
    let deltaX = e.clientX - startX;
    if (deltaX >= threshold) {
      dismissToast();
    } else {
      toast.style.transform = "translateX(0)";
    }
  });

  if (closeButton) closeButton.addEventListener("click", dismissToast);

  toast.addEventListener("mouseleave", resetTimer);

  resetTimer();
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

document.addEventListener('zero-md-rendered', function(event) {
    const zeroMd = event.target;
    const shadowRoot = zeroMd.shadowRoot;

    if (shadowRoot) {
        const preElements = shadowRoot.querySelectorAll('pre');
        preElements.forEach(pre => {
            const button = document.createElement('button');
            const clipboard = '<svg xmlns="http://www.w3.org/2000/svg" width="16"  height="16" viewBox="0 0 24 24" id="clipboard" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-clipboard"><rect width="8" height="4" x="8" y="2" rx="1" ry="1"/><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/></svg>';
            const tick = '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" style="display:none;" id="tick" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-check"><path d="M20 6 9 17l-5-5"/></svg>';
            button.innerHTML = clipboard + tick;
            button.className = 'copy-button';
            
            button.addEventListener('click', function() {
                const code = pre.querySelector('code');
                const text = code.textContent;
                
                if (navigator.clipboard && window.isSecureContext) {
                    // Use Clipboard API if available (HTTPS only)
                    navigator.clipboard.writeText(text).then(() => {
                        showCopiedFeedback(button);
                    }).catch(err => {
                        console.error('Failed to copy text: ', err);
                    });
                } else {
                    // Fallback for older browsers or HTTP
                    const textArea = document.createElement('textarea');
                    textArea.value = text;
                    textArea.style.position = 'fixed';
                    document.body.appendChild(textArea);
                    textArea.focus();
                    textArea.select();
                    try {
                        document.execCommand('copy');
                        showCopiedFeedback(button);
                    } catch (err) {
                        console.error('Failed to copy text: ', err);
                    }
                    document.body.removeChild(textArea);
                }
            });
            pre.appendChild(button);
        });

        function showCopiedFeedback(button) {
            button.querySelector('#tick').style.display = 'block';
            button.querySelector('#clipboard').style.display = 'none';
            setTimeout(() => {
                button.querySelector('#tick').style.display = 'none';
                button.querySelector('#clipboard').style.display = 'block';
            }, 2000);
        }

        const style = document.createElement('style');
        style.textContent = `
            .copy-button {
                appearance: none;
                display: flex;
                position: fixed;
                top: 0.3rem;
                right: 0.3rem;
                padding:3px;
                background-color: transparent;
                border: 1px solid;
                border-color: hsl(var(--border));
                border-radius: 5px;
                cursor: pointer;
            }
            .copy-button:hover {
                background-color: hsl(var(--muted));
            }

        `;
        shadowRoot.appendChild(style);
    }
});
