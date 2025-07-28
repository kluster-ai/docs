// Used to copy the llms-full.txt file to the clipboard in the footer
document.addEventListener('DOMContentLoaded', () => {
  document
    .querySelector('.llms-copy-button')
    .addEventListener('click', async (event) => {
      try {
        const response = await fetch(
          'https://docs.kluster.ai/llms-full.txt'
        );
        const text = await response.text();
        await navigator.clipboard.writeText(text);

        const copiedToClipboard = document.querySelector('.md-dialog');
        copiedToClipboard.classList.add('md-dialog--active');
        const copiedToClipboardMessage =
          copiedToClipboard.querySelector('.md-dialog__inner');
        if (copiedToClipboardMessage) {
          copiedToClipboardMessage.textContent = 'Copied to clipboard';
        }
        // Set a timer to remove the after 2 seconds (2000ms)
        setTimeout(() => {
          copiedToClipboard.classList.remove('md-dialog--active');
        }, 2000);
      } catch (err) {
        console.error('Failed to copy:', err);
        const copiedToClipboard = document.querySelector('.md-dialog');
        if (copiedToClipboard) {
          copiedToClipboard.classList.remove('md-dialog--active');
        }
      }
    });
});
