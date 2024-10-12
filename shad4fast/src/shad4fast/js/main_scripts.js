// function proc_htmx(sel, func) {
//   htmx.onLoad((elt) => {
//     const elements = any(sel, elt, false);
//     if (elt.matches && elt.matches(sel)) elements.unshift(elt);
//     elements.forEach(func);
//   });
// }

proc_htmx(".preventdbclick", (elt) => {
  elt.addEventListener("mousedown", (event) => {
    if (event.detail > 1) event.preventDefault();
  });
});

// Setup Carousel Scripts

proc_htmx("[data-ref=carousel]", (carousel) => {
  const content = carousel.querySelector('[data-ref="content"]');
  const prevButton = carousel.querySelector('[data-ref="prevButton"]');
  const nextButton = carousel.querySelector('[data-ref="nextButton"]');
  const items = carousel.querySelectorAll("[data-carousel-item]");

  if (!content || !items.length) {
    console.error("Carousel is missing required elements");
    return;
  }

  const { autoplay, orientation } = carousel.dataset;
  let autoplayInterval;

  const { height } = carousel.getBoundingClientRect();

  function setupOrientation() {
    if (orientation === "vertical") {
      items.forEach((item) => item.classList.add("pt-4"));
      content.classList.add("-mt-4", "flex-col");
      content.style.height = `${Math.floor(height + 16)}px`;
      if (prevButton) {
        prevButton.classList.add(
          "-top-12",
          "left-1/2",
          "-translate-x-1/2",
          "rotate-90"
        );
      }
      if (nextButton) {
        nextButton.classList.add(
          "-bottom-12",
          "left-1/2",
          "-translate-x-1/2",
          "rotate-90"
        );
      }
    } else {
      items.forEach((item) => item.classList.add("pl-4"));
      content.classList.add("-ml-4");
      if (prevButton)
        prevButton.classList.add("-left-12", "top-1/2", "-translate-y-1/2");
      if (nextButton)
        nextButton.classList.add("-right-12", "top-1/2", "-translate-y-1/2");
    }
  }

  function updateCarousel(direction) {
    const currentIndex = parseInt(carousel.dataset.index, 10) || 0;
    const newIndex = (currentIndex + direction + items.length) % items.length;
    if (orientation === "vertical") {
      content.style.transform = `translate3d(0px, -${
        (height + 16) * newIndex
      }px, 0px)`;
    } else {
      content.style.transform = `translate3d(-${newIndex * 100}%, 0px, 0px)`;
    }
    carousel.dataset.index = newIndex;
  }

  function setupEventListeners() {
    if (prevButton)
      prevButton.addEventListener("click", () => updateCarousel(-1));
    if (nextButton)
      nextButton.addEventListener("click", () => updateCarousel(1));
  }

  function startAutoplay() {
    if (autoplay === "true" && !autoplayInterval) {
      autoplayInterval = setInterval(() => updateCarousel(1), 5000);
    }
  }

  setupOrientation();
  setupEventListeners();
  startAutoplay();
  updateCarousel(0);
});

// Setup Dialog Scripts
let dialog_index = 0;
proc_htmx('[data-ref=dialog]', dialog => {
  const trigger = dialog.querySelector('[data-ref=dialog-trigger]');
  const portal = dialog.querySelector('[data-ref=dialog-portal]')
  const dialog_opts = {
      backdrop: 'dynamic',
      backdropClasses:
          'backdrop data-[state=open]:animate-in data-[state=open]:fade-in-0 data-[state=closed]:animate-out data-[state=closed]:fade-out-0 z-40 fixed inset-0 bg-black/80',
      closable: true,
      onShow: (e) => {
          dialog.dataset.state = 'open';
          e._backdropEl.dataset.state = 'open';
      },
      onHide: () => {
          dialog.dataset.state = 'closed';
      },
  };

  if (!Modal.prototype.customHideImplemented) {
      Modal.prototype.customHide = function() {
          if (this.isVisible) {
              this._backdropEl.dataset.state = 'closed';
              setTimeout(() => {
                  this._targetEl.classList.add('hidden');
                  this._targetEl.classList.remove('flex');
                  this._targetEl.setAttribute('aria-hidden', 'true');
                  this._targetEl.removeAttribute('aria-modal');
                  this._targetEl.removeAttribute('role');
                  this._destroyBackdropEl();
                  this._isHidden = true;

                  document.body.classList.remove('overflow-hidden');

                  if (this._options.closable) {
                      this._removeModalCloseEventListeners();
                  }
              }, 100);

              this._options.onHide(this);
          }
      };
      Modal.prototype.hide = Modal.prototype.customHide;
      Modal.prototype.customHideImplemented = true;
  }

  const instanceOptions = {
    id: `dialog-${dialog_index}`,
    override: true
};

  const d = new Modal(portal, dialog_opts);

  dialog_index += 1;

  trigger.addEventListener('click', (e) => {
    e.preventDefault;
    d.show();
  })

  dialog.querySelectorAll('.dialog-close-button').forEach(btn => {
      btn.addEventListener('click', () => d.hide());
  })
});

htmx.on('htmx:beforeHistorySave', () => {
  dialog_index = 0;

  const backdrop = document.querySelector('.backdrop');

  if (backdrop) backdrop.remove();
  document.querySelectorAll('[data-ref=dialog]').forEach(modal => {
    modal.dataset.state = 'closed';
    modal.querySelector('[data-ref=dialog-portal]').classList.add('hidden');
});
});

// Setup Sheet Scripts

proc_htmx("[data-ref=sheet]", (sheet) => {
  const overlay = sheet.querySelector("[data-ref=sheet-overlay]");
  const trigger = sheet.querySelector("[data-ref=sheet-trigger]");
  const portal = sheet.querySelector("[data-ref=sheet-portal]");

  function openSheet() {
    portal.dataset.state = "open";
    portal.style.display = "block";
  }

  function toggleClose() {
    portal.dataset.state = "closed";
  }

  trigger.addEventListener("click", openSheet);

  overlay.addEventListener("mousedown", toggleClose);

  portal.addEventListener("animationend", () => {
    if (portal.dataset.state === "closed") {
      portal.style.display = "none";
    }
  });

  htmx.on("htmx:historyRestore", () => {
    toggleClose();
    portal.style.display = "none";
  });

  document.addEventListener("click", (e) => {
    if (e.target.closest(".sheet-close-button")) toggleClose();
  });
});

// Setup Radio Scripts

proc_htmx('[data-ref="radio-group"]', (group) => {
  const items = any('[data-ref="radio-item"]', group);
  const hiddenInput = me('[data-ref="hidden-input"]', group);

  function updateRadioGroup(selectedValue) {
    items.run((item) => {
      if (item.value === selectedValue) {
        item.setAttribute("aria-checked", "true");
        item.dataset.state = "checked";
      } else {
        item.setAttribute("aria-checked", "false");
        item.dataset.state = "unchecked";
      }
    });
    hiddenInput.value = selectedValue;
    group.dispatchEvent(
      new CustomEvent("change", { detail: { value: selectedValue } })
    );
  }

  items.on("click", (event) => {
    const selectedValue = event.currentTarget.value;
    updateRadioGroup(selectedValue);
  });

  if (group.dataset.value) {
    updateRadioGroup(group.dataset.value);
  }
});

// Setup Slider Scripts
proc_htmx('[data-ref="slider"]', (slider) => {
  const track = slider.querySelector('[data-ref="track"]');
  const range = slider.querySelector('[data-ref="range"]');
  const thumb = slider.querySelector('[data-ref="thumb"]');
  const hiddenInput = slider.querySelector('[data-ref="hidden-input"]');

  if (!track || !range || !thumb || !hiddenInput) {
    console.error("Slider is missing required elements");
    return;
  }

  const { min, max, step, value } = slider.dataset;
  let currentValue = parseInt(value) || parseInt(min) || 0;

  const config = {
    min: parseInt(min) || 0,
    max: parseInt(max) || 100,
    step: parseInt(step) || 1,
  };

  function updateSlider(percentage) {
    currentValue =
      Math.round(
        (percentage * (config.max - config.min) + config.min) / config.step
      ) * config.step;
    currentValue = Math.max(config.min, Math.min(config.max, currentValue));

    const displayPercentage =
      ((currentValue - config.min) / (config.max - config.min)) * 100;
    range.style.width = `${displayPercentage}%`;
    thumb.style.left = `${displayPercentage}%`;
    slider.setAttribute("aria-valuenow", currentValue);
    hiddenInput.value = currentValue;

    slider.dispatchEvent(
      new CustomEvent("change", { detail: { value: currentValue } })
    );
  }

  function handleMove(clientX) {
    const rect = track.getBoundingClientRect();
    const percentage = (clientX - rect.left) / rect.width;
    updateSlider(percentage);
  }

  function addDragListeners(startEvent) {
    startEvent.preventDefault();
    const moveHandler = (moveEvent) =>
      handleMove(moveEvent.clientX || moveEvent.touches[0].clientX);
    const upHandler = () => {
      document.removeEventListener("mousemove", moveHandler);
      document.removeEventListener("touchmove", moveHandler);
      document.removeEventListener("mouseup", upHandler);
      document.removeEventListener("touchend", upHandler);
    };
    document.addEventListener("mousemove", moveHandler);
    document.addEventListener("touchmove", moveHandler, { passive: false });
    document.addEventListener("mouseup", upHandler);
    document.addEventListener("touchend", upHandler);
  }

  track.addEventListener("mousedown", (e) => {
    if (e.button === 0) {
      handleMove(e.clientX);
      addDragListeners(e);
    }
  });

  track.addEventListener(
    "touchstart",
    (e) => {
      handleMove(e.touches[0].clientX);
      addDragListeners(e);
    },
    { passive: false }
  );

  thumb.addEventListener("mousedown", (e) => {
    if (e.button === 0) addDragListeners(e);
  });

  thumb.addEventListener(
    "touchstart",
    (e) => {
      addDragListeners(e);
    },
    { passive: false }
  );

  updateSlider((currentValue - config.min) / (config.max - config.min));
});

// Setup Tabs Scripts

proc_htmx("[data-ref=tabs]", (tabs) => {
  const triggers = tabs.querySelectorAll("[data-tab-trigger]");
  const contents = tabs.querySelectorAll("[data-tab-content]");

  function setActiveTab(value) {
    triggers.forEach((trigger) => {
      if (trigger.dataset.value === value) {
        trigger.setAttribute("aria-selected", "true");
        trigger.dataset.state = "active";
      } else {
        trigger.setAttribute("aria-selected", "false");
        trigger.dataset.state = "";
      }
    });

    contents.forEach((content) => {
      if (content.dataset.value === value) {
        content.dataset.state = "active";
        content.removeAttribute("hidden");
      } else {
        content.dataset.state = "";
        content.setAttribute("hidden", "");
      }
    });
  }

  triggers.forEach((trigger) => {
    trigger.addEventListener("click", (event) => {
      const value = event.currentTarget.dataset.value;
      setActiveTab(value);
    });
  });

  if (tabs.dataset.defaultValue) {
    setActiveTab(tabs.dataset.defaultValue);
  } else if (triggers.length > 0) {
    setActiveTab(triggers[0].dataset.value);
  }
});

// Setup Toast Scripts

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

  let isDragging = false;
  let startX;
  let originalTransform;
  const threshold = 100;

  toast.addEventListener("mousedown", (e) => {
    e.preventDefault();
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

// Scroll Area Scripts
proc_htmx("[data-ref-scrollarea]", scrollArea => {
  const viewport = scrollArea.querySelector('[data-ref="viewport"]');
  const scrollbar = scrollArea.querySelector('[data-ref="scrollbar"]');
  const thumb = scrollbar.querySelector('[data-ref="thumb"]');
  const isVertical = scrollArea.dataset.orientation !== 'horizontal';
  
  let isMouseOver = false, isScrolling = false, isDragging = false, hideTimeout;
  let scrollTimeout, state = { thumbSize: 0, thumbClickOffset: 0 };
  
  const debounce = (func, wait) => (...args) => {
    clearTimeout(scrollTimeout);
    scrollTimeout = setTimeout(() => func(...args), wait);
  };
  
  const showThumb = () => {
    clearTimeout(hideTimeout);
    thumb.classList.remove('hidden');
  };

  const onWheel = (e) => {
    e.preventDefault();
    const delta = isVertical ? e.deltaY : e.deltaX;
    const scrollAmount = delta * 1;

    if (isVertical) {
      viewport.scrollTop += scrollAmount;
    } else {
      viewport.scrollLeft += scrollAmount;
    }

    updateScrollbar();
  };
  
  const hideThumb = () => {
    if (!isMouseOver && !isScrolling && !isDragging) {
      hideTimeout = setTimeout(() => thumb.classList.add('hidden'), 700);
    }
  };
  
  const debouncedScrollEnd = debounce(() => {
    isScrolling = false;
    hideThumb();
  }, 150);
  
  const updateScrollbar = () => {
    const { clientHeight, clientWidth, scrollHeight, scrollWidth, scrollTop, scrollLeft } = viewport;
    const viewportSize = isVertical ? clientHeight : clientWidth;
    const scrollSize = isVertical ? scrollHeight : scrollWidth;
    const scrollPos = isVertical ? scrollTop : scrollLeft;
    const isOverflow = scrollSize > viewportSize;
    
    if (isOverflow) {
      state.thumbSize = Math.max((viewportSize / scrollSize) * viewportSize, 20);
      const trackSize = viewportSize;
      const thumbTrack = trackSize - state.thumbSize;
      const scrollRange = scrollSize - viewportSize;
      const thumbPos = (scrollPos / scrollRange) * thumbTrack;
      
      thumb.style[isVertical ? 'height' : 'width'] = `${state.thumbSize-2}px`;
      thumb.style.transform = isVertical ? `translate3d(0, ${thumbPos}px, 0)` : `translate3d(${thumbPos}px, 0, 0)`;
      
      if (isMouseOver || isScrolling || isDragging) showThumb();
    } else {
      hideThumb();
    }
    
    scrollbar.style.display = isOverflow ? 'flex' : 'none';
  };
  
  const onScroll = () => {
    isScrolling = true;
    updateScrollbar();
    debouncedScrollEnd();
  };
  
  const setScrollPosition = (clientPos) => {
    const trackRect = scrollbar.getBoundingClientRect();
    const trackStart = isVertical ? trackRect.top : trackRect.left;
    const trackLength = isVertical ? trackRect.height : trackRect.width;
    const pointerOffset = clientPos - trackStart - state.thumbClickOffset;
    const thumbTrack = trackLength - state.thumbSize;
    const scrollRange = isVertical ? viewport.scrollHeight - viewport.clientHeight : viewport.scrollWidth - viewport.clientWidth;
    let scrollPos = (pointerOffset / thumbTrack) * scrollRange;
    scrollPos = Math.max(0, Math.min(scrollPos, scrollRange));
    
    if (isVertical) {
      viewport.scrollTop = scrollPos;
    } else {
      viewport.scrollLeft = scrollPos;
    }
    
    updateScrollbar();
  };
  
  const onPointerDown = e => {
    if (e.button !== 0) return;
    e.preventDefault();
    isDragging = true;
    showThumb();
    const clientPos = isVertical ? e.clientY : e.clientX;
    const thumbRect = thumb.getBoundingClientRect();
    state.thumbClickOffset = isVertical ? clientPos - thumbRect.top : clientPos - thumbRect.left;
    
    setScrollPosition(clientPos);
    
    document.addEventListener('pointermove', onPointerMove);
    document.addEventListener('pointerup', onPointerUp);
  };
  
  const onPointerMove = e => {
    if (!isDragging) return;
    const clientPos = isVertical ? e.clientY : e.clientX;
    setScrollPosition(clientPos);
  };
  
  const onTrackPointerDown = e => {
    if (e.button !== 0) return;
    e.preventDefault();
    isDragging = true;
    showThumb();
    const clientPos = isVertical ? e.clientY : e.clientX;

    state.thumbClickOffset = state.thumbSize / 2;
    
    setScrollPosition(clientPos);
    
    document.addEventListener('pointermove', onPointerMove);
    document.addEventListener('pointerup', onPointerUp);
  };
  
  const onPointerUp = () => {
    isDragging = false;
    hideThumb();
    document.removeEventListener('pointermove', onPointerMove);
    document.removeEventListener('pointerup', onPointerUp);
  };
  
  viewport.addEventListener('scroll', onScroll);
  thumb.addEventListener('pointerdown', onPointerDown);
  scrollbar.addEventListener('pointerdown', onTrackPointerDown);
  scrollArea.addEventListener('pointerenter', () => { isMouseOver = true; updateScrollbar(); });
  scrollArea.addEventListener('pointerleave', () => { isMouseOver = false; hideThumb(); });
  scrollbar.addEventListener('wheel', onWheel, { passive: false });
  
  const resizeObserver = new ResizeObserver(debounce(updateScrollbar, 100));
  resizeObserver.observe(viewport);
  resizeObserver.observe(viewport.firstElementChild);
  
  updateScrollbar();
  thumb.classList.add('hidden');
  
  return () => {
    viewport.removeEventListener('scroll', onScroll);
    thumb.removeEventListener('pointerdown', onPointerDown);
    scrollbar.removeEventListener('pointerdown', onTrackPointerDown);
    scrollArea.removeEventListener('pointerenter', () => {});
    scrollArea.removeEventListener('pointerleave', () => {});
    resizeObserver.disconnect();
    document.removeEventListener('pointermove', onPointerMove);
    document.removeEventListener('pointerup', onPointerUp);
    scrollbar.removeEventListener('wheel', onWheel);
  };
});

// Select Component Scripts

let select_index = 0;
proc_htmx('[data-ref=select]', select => {

  const trigger = select.querySelector('[data-ref=select-trigger]');
  const viewport = select.querySelector('[data-ref=select-viewport]');
  const content = select.querySelector('[data-ref=select-content]');
  const scrollUpBtn = select.querySelector('[data-ref=select-scroll-up]');
  const scrollDownBtn = select.querySelector('[data-ref=select-scroll-down]');
  const input = select.querySelector('input');
  const items = Array.from(select.querySelectorAll('[data-ref=select-item]'));

  trigger.addEventListener('mousedown', (event) => event.preventDefault());

  let scrollInterval = null;
  
  const {width, height} = trigger.getBoundingClientRect();

  viewport.style.minWidth = `${width}px`;

  viewport.style.minHeight = `${height}px`;
  
  const options = {
      placement: 'bottom-start',
      triggerType: 'click',
      offsetSkidding: -1,
      offsetDistance: 5,
      delay:0,
      ignoreClickOutsideClass: false,
      onHide: () => {
        select.dataset.state = 'closed';
      },
      onShow: () => {
          select.dataset.state = 'open';
          initializeFocus();
          updateScrollButtonVisibility();
      },
  };

  Dropdown.prototype.show = function() {
    this._targetEl.classList.remove('hidden');
    this._targetEl.classList.add('flex');
    updateOffsetSkidding();
    this._targetEl.removeAttribute('aria-hidden');

    // Enable the event listeners
    this._popperInstance.setOptions((options) => ({
        ...options,
        modifiers: [
            ...options.modifiers,
            { name: 'eventListeners', enabled: true },
        ],
    }));

    this._setupClickOutsideListener();

    // Update its position
    this._popperInstance.update();
    this._visible = true;

    // callback function
    this._options.onShow(this);
}

  function updateOffsetSkidding(dropdownWidth) {
    const triggerRect = trigger.getBoundingClientRect();
    const viewportWidth = window.innerWidth;

    const leftSpace = triggerRect.left;
    const rightSpace = viewportWidth - triggerRect.right;

    let offsetSkidding = 0;

    if (leftSpace < dropdownWidth && rightSpace < dropdownWidth) {
      offsetSkidding = 0;
    } else if (leftSpace < rightSpace) {
      offsetSkidding = dropdownWidth / 2;
    } else if (rightSpace < leftSpace) {
      offsetSkidding = -(dropdownWidth / 2);
    }

    return Math.round(offsetSkidding);
  }

  const instanceOptions = {
    id: `select-${select_index}`,
    override: true
};

  const dropdown = new Dropdown(content, trigger, options, instanceOptions);

  select_index += 1;

  function updateSelectedItem(item) {
    items.forEach(i => {
      i.dataset.checked = 'false';
      i.setAttribute('aria-selected', 'false');
    });
    item.dataset.checked = 'true';
    item.setAttribute('aria-selected', 'true');
    const selectValue = trigger.querySelector('[data-ref="select-value"]');
    if (selectValue) selectValue.textContent = item.textContent.trim();
    input.value = item.getAttribute('value');
    select.setAttribute('aria-activedescendant', item.id);
    input.dispatchEvent(new Event('change', { bubbles: true }));
  }

  function navigateItems(direction) {
    const currentItem = document.activeElement.closest('[data-ref="select-item"]');
    const currentIndex = currentItem ? items.indexOf(currentItem) : -1;
    const nextIndex = (currentIndex + direction + items.length) % items.length;
    items[nextIndex].focus();
  }

  function initializeFocus() {
    const checkedItem = items.find(item => item.dataset.checked === 'true');
    (checkedItem || items[0])?.focus({preventScroll: true});
  }

  function updateScrollButtonVisibility() {
    if (!viewport) return;
    const isAtTop = viewport.scrollTop === 0;
    const isAtBottom = viewport.scrollHeight - viewport.clientHeight <= viewport.scrollTop + 1;
    const noScroll = viewport.scrollHeight <= viewport.clientHeight;

    if (scrollUpBtn) scrollUpBtn.style.display = isAtTop || noScroll ? 'none' : 'flex';
    if (scrollDownBtn) scrollDownBtn.style.display = isAtBottom || noScroll ? 'none' : 'flex';
  }

  function startScrolling(direction) {
    stopScrolling();
    scrollContent(direction);
    scrollInterval = setInterval(() => scrollContent(direction), 30);
  }

  function stopScrolling() {
    if (scrollInterval) {
      clearInterval(scrollInterval);
      scrollInterval = null;
    }
  }

  function scrollContent(direction) {
    if (viewport) {
      viewport.scrollTop += direction === 'up' ? -20 : 20;
      updateScrollButtonVisibility();
    }
  }

  trigger.addEventListener('keydown', (event) => {
    if (['Enter', ' ', 'ArrowDown', 'ArrowUp'].includes(event.key)) {
      event.preventDefault();
        dropdown.toggle();
      } else {
        navigateItems(event.key === 'ArrowUp' ? -1 : 1);
      }
  });


  content.addEventListener('keydown', (event) => {
    if (['ArrowDown', 'ArrowUp'].includes(event.key)) {
      event.preventDefault();
      navigateItems(event.key === 'ArrowDown' ? 1 : -1);
    } else if (event.key === 'Escape') {
      dropdown.hide();
      trigger.focus();
    }
  });

  items.forEach(item => {
    item.addEventListener('click', () => {
      updateSelectedItem(item);
      dropdown.hide();
      trigger.focus();
    });
    item.addEventListener('keydown', (event) => {
      if (['Enter', ' '].includes(event.key)) {
        event.preventDefault();
        updateSelectedItem(item);
        dropdown.hide();
        trigger.focus();
      }
    });
    item.addEventListener('mouseover', () => item.focus());
  });

  const defaultValue = select.dataset.defaultValue;
  if (defaultValue) {
    const defaultItem = items.find(item => item.getAttribute('value') === defaultValue);
    if (defaultItem) {
      updateSelectedItem(defaultItem);
    }
  }

  if (viewport) {
    viewport.addEventListener('scroll', updateScrollButtonVisibility);
  }

  if (scrollUpBtn) {
    scrollUpBtn.addEventListener('mouseover', () => startScrolling('up'));
    scrollUpBtn.addEventListener('mouseleave', stopScrolling);
  }

  if (scrollDownBtn) {
    scrollDownBtn.addEventListener('mouseover', () => startScrolling('down'));
    scrollDownBtn.addEventListener('mouseleave', stopScrolling);
  }

  window.addEventListener('resize', () => {
    dropdown.hide();
    dropdown._popperInstance.update();
  })
});

htmx.on("htmx:beforeHistorySave", () => {
  select_index = 0;

  document.querySelectorAll("[data-ref=select]").forEach(select => {
    select.dataset.state = 'closed';
    select.querySelector('[data-ref=select-content]').classList.add('hidden');
  })
})

let accordion_index = 0;
proc_htmx('[data-ref=accordion]', accordion => {
  const accordionItems = [];

  accordion_index += 1;

  Accordion.prototype.init = function() {
    if (this._items.length && !this._initialized) {
        // show accordion item based on click
        this._items.forEach((item) => {
          item.targetEl.addEventListener('animationend', () => {
            if (!item.active) {
              item.targetEl.classList.add('hidden');
            }
          })
            if (item.active) {
                this.open(item.id);
            }

            const clickHandler = () => {
                this.toggle(item.id);
            };

            item.triggerEl.addEventListener('click', clickHandler);

            // Store the clickHandler in a property of the item for removal later
            item.clickHandler = clickHandler;
        });
        this._initialized = true;
    }
}

Accordion.prototype.toggle = function(id) {
  const item = this.getItem(id);

  if (item.active) {
    item.triggerEl.dataset.state = 'closed';
      this.close(id);
  } else {
    item.triggerEl.dataset.state = 'open';
      this.open(id);
      item.targetEl.style.setProperty("--accordion-content-height", `${item.targetEl.scrollHeight}px`);
  }

  // callback function
  this._options.onToggle(this, item);
}

Accordion.prototype.close = function(id) {
  const item = this.getItem(id);

  item.triggerEl.setAttribute('aria-expanded', 'false');
  item.triggerEl.dataset.state = 'closed';
  item.active = false;

  // callback function
  this._options.onClose(this, item);
}

Accordion.prototype.open = function(id) {
  const item = this.getItem(id);

  // don't hide other accordions if always open
  if (!this._options.alwaysOpen) {
      this._items.map((i) => {
          if (i !== item) {
              i.triggerEl.dataset.state = 'closed';
              i.triggerEl.setAttribute('aria-expanded', 'false');
              i.active = false;
          }
      });
  }
  // show active item
  item.triggerEl.setAttribute('aria-expanded', 'true');
  item.targetEl.classList.remove('hidden');
  item.active = true;

  // callback function
  this._options.onOpen(this, item);
}

  accordion.querySelectorAll('[data-ref=accordion-item]').forEach((item, index) => {
    const content = item.querySelector('[data-ref=accordion-content]');
    const trigger = item.querySelector('[data-ref=accordion-trigger]');

    accordionItems.push({id: `item-${index + 1}`, triggerEl: trigger, targetEl: content, active: false})
  })

  const instanceOptions = {
    id: `accordion-${accordion_index}`,
    override: true,
};

  const acc = new Accordion(accordion, accordionItems, {}, instanceOptions);

});

function handleAccordionClose() {
  document.querySelectorAll('[data-ref=accordion]').forEach(accordion => {
    accordion.querySelectorAll('[data-ref=accordion-item]').forEach((item) => {
      const trigger = item.querySelector('[data-ref=accordion-trigger]');
      const content = item.querySelector('[data-ref=accordion-content]');

      trigger.dataset.state = 'closed';
      trigger.setAttribute("aria-expanded", "false");
      content.classList.add('hidden');
    })
  })
}

htmx.on("htmx:beforeHistorySave", () => handleAccordionClose());