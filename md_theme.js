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
