document.addEventListener('DOMContentLoaded', () => {
  document
    .querySelector('.full-llms')
    .addEventListener('click', async (event) => {
      try {
        const response = await fetch(
          // TODO: Update this URL for prod
          'http://127.0.0.1:8000/llms-full.txt',
        );
        const text = await response.text();
        await navigator.clipboard.writeText(text);

        const copiedToClipboard = document.querySelector('.md-dialog');
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
