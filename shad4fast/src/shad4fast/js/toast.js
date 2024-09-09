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
  