document.addEventListener('DOMContentLoaded', () => {
  document
    .querySelector('.full-llms')
    .addEventListener('click', async (event) => {
      const copiedToClipboard = document.querySelector('.md-dialog');
      try {
        const llmsUrl = new URL('/ai/llms-full.jsonl', window.location.origin);
          const response = await fetch(llmsUrl, { credentials: 'omit' });
        const text = await response.text();
        await navigator.clipboard.writeText(text);
        
        if (copiedToClipboard) {
          copiedToClipboard.classList.add('md-dialog--active');

          const copiedToClipboardMessage =
            copiedToClipboard.querySelector('.md-dialog__inner');
          if (copiedToClipboardMessage) {
            copiedToClipboardMessage.textContent = "Copied to clipboard";
          }
          // Set a timer to remove the after 2 seconds (2000ms)
          setTimeout(() => {
            copiedToClipboard.classList.remove('md-dialog--active');
          }, 2000);
        }
      } catch (err) {
        console.error('Failed to copy:', err);
        copiedToClipboard.classList.remove('md-dialog--active');
      }
    });
});