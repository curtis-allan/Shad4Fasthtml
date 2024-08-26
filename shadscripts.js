class SelectMenu {
    constructor(select) {
        this.select = select;
        this.trigger = select.querySelector('.select-trigger');
        this.portal = document.getElementById(`${select.id}-portal`);
        this.content = this.portal.querySelector('.select-content');
        this.input = select.querySelector('input');
        this.items = this.content.querySelectorAll('.select-item');
        this.viewport = this.content.querySelector('.viewport');
        this.scrollUpBtn = this.content.querySelector('.scroll-up');
        this.scrollDownBtn = this.content.querySelector('.scroll-down');

        this.setupEventListeners();
        this.initializePortal();
    }

    setupEventListeners() {
        this.trigger.addEventListener('mousedown', this.toggleSelect.bind(this));
        this.trigger.addEventListener('keydown', this.handleTriggerKeydown.bind(this));
        this.portal.addEventListener('click', this.handlePortalClick.bind(this));
        this.content.addEventListener('keydown', this.handleContentKeydown.bind(this));
        this.content.addEventListener('focusout', this.handleContentFocusout.bind(this));
        this.items.forEach(item => {
            item.addEventListener('click', () => this.handleItemClick(item));
            item.addEventListener('keydown', (event) => this.handleItemKeydown(event, item));
        });
        if (this.viewport) {
            this.viewport.addEventListener('scroll', () => this.updateScrollButtonVisibility());
        }
        this.setupScrollButtons();
        window.addEventListener('resize', this.handleWindowResize.bind(this));
    }

    initializePortal() {
        document.body.appendChild(this.portal);
        if (this.content) this.content.dataset.selectId = this.select.id;
    }

    toggleSelect(event) {
        // Check if it's not a right-click (contextmenu) event
        if (event.button !== 2) {
            event.preventDefault();
            event.stopPropagation();
            this.select.dataset.state === 'open' ? this.close() : this.open();
        }
    }

    open() {
        document.querySelectorAll('.select[data-state="open"]').forEach(select => new SelectMenu(select).close());
        this.select.dataset.state = 'open';
        this.content.dataset.state = 'open';
        this.portal.style.display = 'flex';
        this.select.setAttribute('aria-expanded', 'true');
        this.injectPortal();
        this.updateScrollButtonVisibility(); 
        document.body.classList.add('pointer-events-none');
        setTimeout(() => {
            document.addEventListener('mousedown', this.closeOnClickOutside);
            this.updateScrollButtonVisibility();
        }, 0);
        this.initializeFocus();
    }

    close() {
        this.select.dataset.state = 'closed';
        this.content.dataset.state = 'closed';
        this.portal.style.display = 'none';
        this.select.setAttribute('aria-expanded', 'false');
        document.body.classList.remove('pointer-events-none');
        document.removeEventListener('mousedown', this.closeOnClickOutside);
        this.portal.blur();
    }

    handleItemClick(item) {
        if (this.input.value !== item.getAttribute('value')) {
            this.updateSelectedItem(item);
        }
        this.close();
        this.trigger.focus();
    }


        updateSelectedItem(item) {
            this.items.forEach(i => {
                i.dataset.checked = 'false';
                i.setAttribute('aria-selected', 'false');
            });
            item.dataset.checked = 'true';
            item.setAttribute('aria-selected', 'true');
            const selectValue = this.trigger.querySelector('.select-value');
            if (selectValue) selectValue.textContent = item.textContent;
            this.input.value = item.getAttribute('value');
            this.select.setAttribute('aria-activedescendant', item.id);
            this.input.dispatchEvent(new Event('change', { bubbles: true }));
        }
    
    handleTriggerKeydown(event) {
        if (['Enter', ' ', 'ArrowDown', 'ArrowUp'].includes(event.key)) {
            event.preventDefault();
            if (this.select.dataset.state !== 'open') {
                this.open();
            } else if (['ArrowDown', 'ArrowUp'].includes(event.key)) {
                this.navigateItems(event.key === 'ArrowDown' ? 1 : -1);
            }
        }
    }

    handlePortalClick(event) {
        const clickedItem = event.target.closest('.select-item');
        if (clickedItem) {
            this.handleItemClick(clickedItem);
        } else if (!event.target.closest('.select-content')) {
            this.close();
        }
        event.stopPropagation();
    }

    handleContentKeydown(event) {
        if (['ArrowDown', 'ArrowUp'].includes(event.key)) {
            event.preventDefault();
            this.navigateItems(event.key === 'ArrowDown' ? 1 : -1);
        } else if (event.key === 'Escape') {
            this.close();
            this.trigger.focus();
        }
    }

    handleItemKeydown(event, item) {
        if (['Enter', ' '].includes(event.key)) {
            event.preventDefault();
            this.handleItemClick(item);
        }
    }

    handleContentFocusout(event) {
        if (!this.content.contains(event.relatedTarget) && event.relatedTarget !== this.trigger) {
            this.close();
        }
    }

    navigateItems(direction) {
        const itemsArray = Array.from(this.items);
        const currentItem = document.activeElement.closest('.select-item');
        const currentIndex = currentItem ? itemsArray.indexOf(currentItem) : -1;
        const nextIndex = (currentIndex + direction + itemsArray.length) % itemsArray.length;
        itemsArray[nextIndex].focus();
    }

    initializeFocus() {
        const checkedItem = Array.from(this.items).find(item => item.dataset.checked === 'true');
        if (checkedItem) {
            checkedItem.focus();
        } else if (this.items.length > 0) {
            this.items[0].focus();
        }
    }

    injectPortal() {
        const { left, right, top, bottom, width, height } = this.trigger.getBoundingClientRect();
        const { innerWidth: viewportWidth, innerHeight: viewportHeight } = window;
        const portalHeight = this.portal.getBoundingClientRect().height;
        const portalWidth = this.portal.getBoundingClientRect().width;

        let translateX = left;
        let translateY = bottom;
        let side = 'bottom';

        // Check vertical space
        if (viewportHeight - bottom < portalHeight && top > portalHeight) {
            translateY = top - portalHeight;
            side = 'top';
        }

        // Check horizontal space
        if (viewportWidth - right < portalWidth && left > portalWidth) {
            translateX = right - portalWidth;
            side = side === 'top' ? 'top-right' : 'bottom-right';
        }

        const availableWidth = viewportWidth - translateX;
        const availableHeight = side.includes('top') ? top : viewportHeight - bottom;

        this.portal.style.setProperty('--radix-popper-transform-origin', `${side.includes('right') ? '100%' : '0%'} ${side.includes('top') ? '100%' : '0%'}`);
        this.portal.style.setProperty('--radix-popper-available-width', `${availableWidth}px`);
        this.portal.style.setProperty('--radix-popper-available-height', `${availableHeight}px`);
        this.portal.style.setProperty('--radix-popper-anchor-width', `${width}px`);
        this.portal.style.setProperty('--radix-popper-anchor-height', `${height}px`);
        this.portal.style.transform = `translate(${translateX}px, ${translateY}px)`;

        this.content.dataset.side = side;
        this.portal.offsetHeight; // Force a reflow
    }

    updateScrollButtonVisibility() {
        if (!this.viewport) return;
        const isAtTop = this.viewport.scrollTop === 0;
        const isAtBottom = this.viewport.scrollHeight - this.viewport.clientHeight <= this.viewport.scrollTop + 1;
        const noScroll = this.viewport.scrollHeight <= this.viewport.clientHeight;

        if (this.scrollUpBtn) this.scrollUpBtn.style.display = isAtTop || noScroll ? 'none' : 'flex';
        if (this.scrollDownBtn) this.scrollDownBtn.style.display = isAtBottom || noScroll ? 'none' : 'flex';
    }

    setupScrollButtons() {
        if (this.scrollUpBtn) {
            this.scrollUpBtn.addEventListener('mouseover', this.startScrolling.bind(this, 'up'));
            this.scrollUpBtn.addEventListener('mouseleave', this.stopScrolling.bind(this));
        }

        if (this.scrollDownBtn) {
            this.scrollDownBtn.addEventListener('mouseover', this.startScrolling.bind(this, 'down'));
            this.scrollDownBtn.addEventListener('mouseleave', this.stopScrolling.bind(this));
        }
    }

    startScrolling(direction) {
        this.stopScrolling(); // Clear any existing interval
        this.scrollContent(direction);
        this.scrollInterval = setInterval(() => this.scrollContent(direction), 30); // Increased frequency for smoother and quicker scrolling
    }

    stopScrolling() {
        if (this.scrollInterval) {
            clearInterval(this.scrollInterval);
            this.scrollInterval = null;
        }
    }

    scrollContent(direction) {
        if (this.viewport) {
            const scrollAmount = direction === 'up' ? -20 : 20; // Increased scroll amount for quicker scrolling
            this.viewport.scrollTop += scrollAmount;
            this.updateScrollButtonVisibility();
        }
    }

    closeOnClickOutside = (event) => {
        if (!this.portal.contains(event.target) && !this.trigger.contains(event.target)) {
            this.close();
        }
    }

    handleWindowResize = () => {
        if (this.select.dataset.state === 'open') {
            this.close();
        }
    }
}

htmx.onLoad((content) => {
    content.querySelectorAll('.select').forEach(select => new SelectMenu(select));
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

proc_htmx(".theme-toggle", (elt) => {
  elt.addEventListener("mousedown", (event) => {
    event.preventDefault();
    const zeroMd = document.querySelectorAll("zero-md");

    if (
      localStorage.theme === "dark" ||
      document.documentElement.classList.contains("dark")
    ) {
      localStorage.theme = "light";
      document.documentElement.classList.remove("dark");
    } else {
      localStorage.theme = "dark";
      document.documentElement.classList.add("dark");
    }
    swapTheme();
    zeroMd.forEach((zeroMd) => {
      if (zeroMd.shadowRoot) {
        const links = zeroMd.shadowRoot.querySelectorAll("link");
        links.forEach((link) => handleMdThemeChange(link));
      } else {
        console.log("No shadow roots found");
      }
    });
  });
});

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

function highlightActiveLink(content) {
    const currentPath = window.location.pathname;
    const links = content.querySelectorAll(`a[href=${CSS.escape(currentPath)}] button`);

    links.forEach(() => {
        links.forEach(link => {link.classList.add('border-r-2', '!border-primary','font-semibold', 'rounded-none'); link.classList.remove('!text-muted-foreground');});

    })}

    htmx.onLoad((content) => highlightActiveLink(content));
    
const sunIcons = document.querySelectorAll('#theme-icon-sun');
const moonIcons = document.querySelectorAll('#theme-icon-moon');

if (localStorage.theme === 'dark' || document.documentElement.classList.contains('dark')) {
    if(sunIcons && moonIcons) {
        sunIcons.forEach(icon => icon.style.display = 'block')
        moonIcons.forEach(icon => icon.style.display = 'none')
        }
} else {
    if(sunIcons && moonIcons) {
        sunIcons.forEach(icon => icon.style.display = 'none')
        moonIcons.forEach(icon => icon.style.display = 'block')
    }
}

function swapTheme() {
    const sunIcons = document.querySelectorAll('#theme-icon-sun');
    const moonIcons = document.querySelectorAll('#theme-icon-moon');

    if (localStorage.theme === 'dark' || document.documentElement.classList.contains('dark')) {
        if(sunIcons && moonIcons) {
            sunIcons.forEach(icon => icon.style.display = 'block')
            moonIcons.forEach(icon => icon.style.display = 'none')
            }
} else {
        if(sunIcons && moonIcons) {
            sunIcons.forEach(icon => icon.style.display = 'none')
            moonIcons.forEach(icon => icon.style.display = 'block')
        }
    }
}

function handleThemeChange() {
if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", () => {
        swapTheme()
        document.body.addEventListener("htmx:afterSwap", () => {
            swapTheme()
        });
    });
} else {
    swapTheme()
    document.body.addEventListener("htmx:afterSwap", () => {
        swapTheme()
    });
}
}

if (localStorage.theme === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
document.documentElement.classList.add('dark')
handleThemeChange()
} else {
document.documentElement.classList.remove('dark')
handleThemeChange()
}

function handleMdThemeChange(link) {
const isDarkMode = localStorage.theme === 'dark' || document.documentElement.classList.contains('dark');
const themeClass = isDarkMode ? 'dark-theme' : 'light-theme';
link.disabled = !link.classList.contains(themeClass); 
}

document.addEventListener('zero-md-rendered', function(event) {
        const zeroMd = event.target;
        const shadowRoot = zeroMd.shadowRoot;

    if (shadowRoot) {
        const preElements = shadowRoot.querySelectorAll('pre');

        shadowRoot.querySelectorAll('link').forEach(link => handleMdThemeChange(link));
        
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
