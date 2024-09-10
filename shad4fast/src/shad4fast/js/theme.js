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
  