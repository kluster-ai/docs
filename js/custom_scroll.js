document.addEventListener("DOMContentLoaded", function () {
  // --- Configuration ---
  // Adjust this selector to match your theme's fixed header.
  const headerSelector = ".md-header";
  const additionalOffset = 16;

  function getHeaderHeight() {
    const header = document.querySelector(headerSelector);
    return header ? header.offsetHeight : 0;
  }

  function scrollToTarget(targetId, isInitialLoad = false) {
    const targetElement = document.getElementById(targetId);

    if (targetElement) {
      const headerHeight = getHeaderHeight();
      // Calculate element's position relative to the document top
      const elementPosition =
        targetElement.getBoundingClientRect().top + window.pageYOffset;
      const offsetPosition = elementPosition - headerHeight - additionalOffset;

      const scrollOptions = {
        top: offsetPosition,
        behavior: "auto",
      };
      if (isInitialLoad) {
        requestAnimationFrame(() => {
          window.scrollTo(scrollOptions);
        });
      } else {
        window.scrollTo(scrollOptions);
      }
    }
  }

  // --- Handle Clicks on Anchor Links ---
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener("click", function (event) {
      const href = this.getAttribute("href");
      // Ensure it's a page-local fragment and the target element exists
      if (href.length > 1 && href.startsWith("#")) {
        const targetId = href.substring(1);
        if (document.getElementById(targetId)) {
          event.preventDefault(); // Stop the default browser jump
          scrollToTarget(targetId);

          // Optionally, update the URL hash in the address bar without adding to browser history
          // This makes the URL reflect the current section without lots of back-button steps.
          if (history.replaceState) {
            history.replaceState(null, null, href);
          }
        }
      }
    });
  });

  // --- Handle Initial Page Load with Hash ---
  if (window.location.hash) {
    const targetId = window.location.hash.substring(1);
    // Ensure the element exists before trying to scroll
    if (document.getElementById(targetId)) {
      // Using requestAnimationFrame helps ensure that the layout is stable
      // and all elements (like the header) have their final dimensions.
      requestAnimationFrame(() => {
        scrollToTarget(targetId, true); // Pass true for initial load handling
      });
    }
  }
});
