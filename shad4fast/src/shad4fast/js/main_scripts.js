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

// Setup Carousel Scripts

proc_htmx("[data-ref=carousel]", (carousel) => {
  const content = carousel.querySelector('[data-ref="content"]');
  const prevButton = carousel.querySelector('[data-ref="prevButton"]');
  const nextButton = carousel.querySelector('[data-ref="nextButton"]');
  const items = carousel.querySelectorAll("[data-carousel-item]");

  const { autoplay, orientation} = carousel.dataset;
  let autoplayInterval;

  const { height } = carousel.getBoundingClientRect();

  function setupOrientation() {
    if (orientation === "vertical") {
      items.forEach((item) => item.classList.add("pt-4"));
      content.classList.add("-mt-4", "flex-col");
      content.style.height = `${Math.floor(height + 16)}px`;
      if (prevButton)
        prevButton.classList.add("-top-12", "left-1/2", "-translate-x-1/2", "rotate-90");
      if (nextButton)
        nextButton.classList.add("-bottom-12", "left-1/2", "-translate-x-1/2", "rotate-90");
    } else {
      items.forEach((item) => item.classList.add("pl-4"));
      content.classList.add("-ml-4");
      if (prevButton) prevButton.classList.add("-left-12", "top-1/2", "-translate-y-1/2");
      if (nextButton) nextButton.classList.add("-right-12", "top-1/2", "-translate-y-1/2");
    }
  }

  function updateCarousel(direction) {
      const index = (parseInt(carousel.dataset.index, 10)+direction+items.length) % items.length;
    if (orientation === "vertical") {
      content.style.transform = `translate3d(0px, -${(height + 16) * index}px, 0px)`;
    } else {
      content.style.transform = `translate3d(-${index * 100}%, 0px, 0px)`;
    }
    carousel.dataset.index = index;
  }

  function setupEventListeners() {
    if (prevButton) prevButton.addEventListener("click", () => updateCarousel(-1));
    if (nextButton) nextButton.addEventListener("click", () => updateCarousel(1));
  }

  function startAutoplay() {
    if (autoplay === "true" && !autoplayInterval) {
      autoplayInterval = setInterval(() => updateCarousel(1), 5000);
    }
  }
      setupOrientation();
      setupEventListeners();
      startAutoplay();
      updateCarousel(parseInt(carousel.dataset.index, 10));

});

// Setup Dialog Scripts

proc_htmx("[data-ref=dialog]", (dialog) => {
  const overlay = dialog.querySelector("[data-ref=dialog-overlay]");
  const trigger = dialog.querySelector("[data-ref=dialog-trigger]");
  const portal = dialog.querySelector("[data-ref=dialog-portal]");

  function openDialog() {
    portal.dataset.state = "open";
    portal.style.display = "block";
  }

  function toggleClose() {
    portal.dataset.state = "closed";
  }

  trigger.addEventListener("click", openDialog);

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
    if (e.target.closest(".dialog-close-button")) toggleClose();
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

proc_htmx('[data-ref="radio-group"]', group => {
  const items = any('[data-ref="radio-item"]', group)
  const hiddenInput = me('[data-ref="hidden-input"]', group)

  function updateRadioGroup(selectedValue) {
      items.run(item => {
          if (item.value === selectedValue) {
              item.setAttribute('aria-checked', 'true')
              item.dataset.state = 'checked'
          } else {
              item.setAttribute('aria-checked', 'false')
              item.dataset.state = 'unchecked'
          }
      })
      hiddenInput.value = selectedValue
      group.dispatchEvent(new CustomEvent('change', { detail: { value: selectedValue } }))
  }

  items.on('click', (event) => {
      const selectedValue = event.currentTarget.value
      updateRadioGroup(selectedValue)
  })

  if (group.dataset.value) {
      updateRadioGroup(group.dataset.value)
  }
})

// Setup Slider Scripts

proc_htmx('[data-ref="slider"]', slider => {
  const track = slider.querySelector('[data-ref="track"]')
  const range = slider.querySelector('[data-ref="range"]')
  const thumb = slider.querySelector('[data-ref="thumb"]')
  const hiddenInput = slider.querySelector('[data-ref="hidden-input"]')

  const {min, max, step, value} = slider.dataset
  let currentValue = parseInt(value) || 0

  function updateSlider() {
      const percentage = ((currentValue - min) / (max - min)) * 100
      range.style.width = `${percentage}%`
      thumb.style.left = `${percentage}%`
      slider.setAttribute('aria-valuenow', currentValue)
      hiddenInput.value = currentValue
  }

  function handleMove(clientX) {
      const rect = track.getBoundingClientRect()
      const percentage = (clientX - rect.left) / rect.width
      currentValue = Math.round((percentage * (max - min) + parseInt(min)) / step) * step
      currentValue = Math.max(min, Math.min(max, currentValue))
      updateSlider()
      slider.dispatchEvent(new CustomEvent('change', { detail: { value: currentValue } }))
  }

  function addDragListeners(startEvent) {
      if (startEvent.button !== 0 && startEvent.type !== 'touchstart') return;
      startEvent.preventDefault()
      const moveHandler = moveEvent => handleMove(moveEvent.clientX || moveEvent.touches[0].clientX)
      const upHandler = () => {
          document.removeEventListener('mousemove', moveHandler)
          document.removeEventListener('mouseup', upHandler)
          document.removeEventListener('touchmove', moveHandler)
          document.removeEventListener('touchend', upHandler)
      }
      document.addEventListener('mousemove', moveHandler)
      document.addEventListener('mouseup', upHandler)
      document.addEventListener('touchmove', moveHandler)
      document.addEventListener('touchend', upHandler)
  }

  track.addEventListener('mousedown', e => {
      if (e.button === 0) { 
          handleMove(e.clientX)
          addDragListeners(e)
      }
  })

  track.addEventListener('touchstart', e => {
      handleMove(e.touches[0].clientX)
      addDragListeners(e)
  })

  thumb.addEventListener('mousedown', e => {
      if (e.button === 0) addDragListeners(e) 
  })

  thumb.addEventListener('touchstart', e => {
      addDragListeners(e)
  })

  updateSlider()
})

// Setup Tabs Scripts

proc_htmx('[data-ref=tabs]', tabs => {
  const triggers = tabs.querySelectorAll('[data-tab-trigger]')
  const contents = tabs.querySelectorAll('[data-tab-content]')
  
  function setActiveTab(value) {
      triggers.forEach(trigger => {
          if (trigger.dataset.value === value) {
            trigger.setAttribute('aria-selected', 'true');
            trigger.dataset.state = 'active';

          } else {
              trigger.setAttribute('aria-selected', 'false');
              trigger.dataset.state = '';
          }
      })
      
      contents.forEach(content => {
          if (content.dataset.value === value) {
              content.dataset.state = 'active'
              content.removeAttribute('hidden')
          } else {
              content.dataset.state = ''
              content.setAttribute('hidden', '')
          }
      })
  }
  
  triggers.forEach((trigger) => {
    trigger.addEventListener('click', (event) => {
      const value = event.currentTarget.dataset.value
      setActiveTab(value)
  })
})

  if (tabs.dataset.defaultValue) {
    setActiveTab(tabs.dataset.defaultValue)
  } else if (triggers.length > 0) {
      setActiveTab(triggers[0].dataset.value)
  }
})

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





