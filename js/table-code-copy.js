/* Table Code Copy
   Adds a copy-to-clipboard button to inline <code> elements inside table cells.
   Reuses Material for MkDocs' built-in .md-dialog toast for feedback.
*/

(function () {
  'use strict';

  if (typeof window === 'undefined') {
    return;
  }

  function ensureDialog() {
    var dlg = document.querySelector('[data-md-component="dialog"]');
    if (!dlg) {
      dlg = document.createElement('div');
      dlg.className = 'md-dialog';
      dlg.setAttribute('data-md-component', 'dialog');
      var inner = document.createElement('div');
      inner.className = 'md-dialog__inner md-typeset';
      dlg.appendChild(inner);
      document.body.appendChild(dlg);
    }
    return dlg;
  }

  function showToast(message) {
    var dlg = ensureDialog();
    var msg = dlg.querySelector('.md-dialog__inner');
    if (msg) msg.textContent = message;
    dlg.classList.add('md-dialog--active');
    setTimeout(function () {
      dlg.classList.remove('md-dialog--active');
    }, 2000);
  }

  function createCopyButton(codeEl) {
    var btn = document.createElement('button');
    btn.className = 'table-code-copy-btn';
    btn.title = 'Copy to clipboard';
    btn.setAttribute('aria-label', 'Copy to clipboard');
    btn.innerHTML =
      '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="14" height="14">' +
      '<path fill="currentColor" d="M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 ' +
      '4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11c1.1 0 2-.9 ' +
      '2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z"/></svg>';

    btn.addEventListener('click', function (e) {
      e.preventDefault();
      e.stopPropagation();
      var text = codeEl.textContent;
      navigator.clipboard.writeText(text).then(function () {
        showToast('Copied to clipboard');
      });
    });

    return btn;
  }

  function init() {
    var cells = document.querySelectorAll('td code');
    cells.forEach(function (codeEl) {
      if (codeEl.parentNode.classList.contains('table-code-copy-wrapper')) {
        return;
      }
      var wrapper = document.createElement('span');
      wrapper.className = 'table-code-copy-wrapper';
      codeEl.parentNode.insertBefore(wrapper, codeEl);
      wrapper.appendChild(codeEl);
      wrapper.appendChild(createCopyButton(codeEl));
    });
  }

  // Run on initial load and on Material instant-loading navigation
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
  document.addEventListener('DOMContentSwitch', init);
})();
