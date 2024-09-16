if (typeof window.Select === 'undefined') {
    window.Select = class Select {
    constructor(select) {
        this.select = select;
        this.trigger = select.querySelector('[data-ref="select-trigger"]');
        this.portal = document.getElementById(`${select.id}-portal`);
        this.content = this.portal.querySelector('[data-ref="select-content"]');
        this.input = select.querySelector('input');
        this.items = Array.from(select.querySelectorAll('[data-ref="select-item"]'));
        this.viewport = this.content.querySelector('[data-ref="select-viewport"]');
        this.scrollUpBtn = this.content.querySelector('[data-ref="select-scroll-up"]');
        this.scrollDownBtn = this.content.querySelector('[data-ref="select-scroll-down"]');
        this.state = { scrollInterval: null };

        this.init();
    }

    init() {
        this.setupEventListeners();
        this.setInitialValue();
    }

    setupEventListeners() {
        this.trigger.addEventListener('mousedown', this.toggleSelect.bind(this));
        window.addEventListener('resize', this.close.bind(this))
        this.trigger.addEventListener('keydown', this.handleTriggerKeydown.bind(this));
        this.content.addEventListener('keydown', this.handleContentKeydown.bind(this));
        this.content.addEventListener('focusout', this.handleContentFocusout.bind(this));
        this.items.forEach(item => {
            item.addEventListener('click', () => this.handleItemClick(item));
            item.addEventListener('keydown', event => this.handleItemKeydown(event, item));
            item.addEventListener('mouseover', event => this.handleMouseOver(event, item));
        });
        if (this.viewport) {
            this.viewport.addEventListener('scroll', this.updateScrollButtonVisibility.bind(this));
        }
        this.setupScrollButtons();
        document.addEventListener('mousedown', this.closeOnClickOutside.bind(this));
    }

    initializePortal() {
        if (this.content) this.content.dataset.selectId = this.select.id;
    }

    toggleSelect(event) {
        if (event.button !== 2) {
            event.preventDefault();
            event.stopPropagation();
            this.select.dataset.state === 'closed' ? this.open() : this.close();
        }
    }

    open() {
        this.select.dataset.state = 'open';
        this.content.dataset.state = 'open';
        this.portal.style.display = 'block';
        this.initializePortal();
        this.select.setAttribute('aria-expanded', 'true');
        this.trigger.classList.add('pointer-events-auto');
        this.updateScrollButtonVisibility();
        document.body.classList.add('pointer-events-none');
        this.initializeFocus();
        this.injectPortal();
    }

    close() {
        this.select.dataset.state = 'closed';
        this.content.dataset.state = 'closed';
        this.portal.style.display = 'none';
        this.trigger.classList.remove('pointer-events-auto');
        this.select.setAttribute('aria-expanded', 'false');
        document.body.classList.remove('pointer-events-none');
        this.portal.blur()
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
        const selectValue = this.trigger.querySelector('[data-ref="select-value"]');
        if (selectValue) selectValue.textContent = item.textContent.trim();
        this.input.value = item.getAttribute('value');
        this.select.setAttribute('aria-activedescendant', item.id);
        this.input.dispatchEvent(new Event('change', { bubbles: true }));
    }

    handleTriggerKeydown(event) {
        if (['Enter', ' ', 'ArrowDown', 'ArrowUp'].includes(event.key)) {
            event.preventDefault();
            this.open();
        } else if (['ArrowDown', 'ArrowUp'].includes(event.key)) {
            this.navigateItems(event.key === 'ArrowDown' ? 1 : -1);
        }
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

    handleMouseOver(event, item) {
        item.focus();
    }

    navigateItems(direction) {
        const currentItem = document.activeElement.closest('[data-ref="select-item"]');
        const currentIndex = currentItem ? this.items.indexOf(currentItem) : -1;
        const nextIndex = (currentIndex + direction + this.items.length) % this.items.length;
        this.items[nextIndex].focus();
    }

    initializeFocus() {
        const checkedItem = this.items.find(item => item.dataset.checked === 'true');
        if (checkedItem) {
            checkedItem.focus();
        } else if (this.items.length > 0) {
            this.items[0].focus();
        }
    }

    injectPortal() {
        const { left, right, top, bottom, width, height } = this.trigger.getBoundingClientRect();
        const { innerWidth: viewportWidth, innerHeight: viewportHeight } = window;
        const portalRect = this.portal.getBoundingClientRect();
        const portalHeight = portalRect.height;
        const portalWidth = portalRect.width;
        let translateX = left;
        let translateY = bottom;
        let side = 'bottom';

        this.portal.style.width = `${Math.max(width, 200)}px`;
        this.portal.style.maxWidth = 'max-content';
        requestIdleCallback(() => {
            if (viewportHeight - bottom <= portalHeight && top > portalHeight) {
                translateY = Math.round(top - portalHeight);
                side = 'top';
            }

            if (left + portalWidth > viewportWidth) {
                translateX = Math.max(0, right - portalWidth);
            }

            this.portal.style.willChange = 'transform';
            this.portal.style.zIndex = '50';

            this.portal.style.setProperty('--radix-popper-anchor-width', `${width}px`);
            this.portal.style.setProperty('--radix-popper-anchor-height', `${height}px`);

            this.content.dataset.side = side;
            this.portal.style.transform = `translate(${translateX}px, ${translateY}px)`;

            this.portal.offsetHeight; // Force reflow
        });
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
            this.scrollUpBtn.addEventListener('mouseover', () => this.startScrolling('up'));
            this.scrollUpBtn.addEventListener('mouseleave', this.stopScrolling.bind(this));
        }

        if (this.scrollDownBtn) {
            this.scrollDownBtn.addEventListener('mouseover', () => this.startScrolling('down'));
            this.scrollDownBtn.addEventListener('mouseleave', this.stopScrolling.bind(this));
        }
    }

    startScrolling(direction) {
        this.stopScrolling();
        this.scrollContent(direction);
        this.state.scrollInterval = setInterval(() => this.scrollContent(direction), 30);
    }

    stopScrolling() {
        if (this.state.scrollInterval) {
            clearInterval(this.state.scrollInterval);
            this.state.scrollInterval = null;
        }
    }

    scrollContent(direction) {
        if (this.viewport) {
            const scrollAmount = direction === 'up' ? -20 : 20;
            this.viewport.scrollTop += scrollAmount;
            this.updateScrollButtonVisibility();
        }
    }

    closeOnClickOutside(event) {
        if (!this.portal.contains(event.target) && !this.trigger.contains(event.target)) {
            this.close();
        }
    }

    handleContentFocusout(event) {
        if (!this.content.contains(event.relatedTarget) && event.relatedTarget !== this.trigger) {
            this.close();
        }
    }

    setInitialValue() {
        const defaultValue = this.select.dataset.defaultValue;
        if (defaultValue) {
            const defaultItem = this.items.find(item => item.getAttribute('value') === defaultValue);
            if (defaultItem) {
                this.updateSelectedItem(defaultItem);
            }
        }
    }
}
}

function handleSelectClose() {
    document.querySelectorAll('[data-ref="select"]').forEach(select => {
        if (select._selectInstance) {
            select._selectInstance.close();
        }
    });
}

if (!window.selectInitialized) {
    window.selectInitialized = true;
    proc_htmx('[data-ref="select"]', select => {
        select._selectInstance = new window.Select(select);
    })
    htmx.on("htmx:beforeHistorySave", () => {handleSelectClose()})
    htmx.on('htmx:historyRestore', () => {handleSelectClose()})
}