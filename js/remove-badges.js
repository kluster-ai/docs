// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - //
// This script dynamically controls the visibility of language selector badges (HTTP, Python) //
// based on the presence of actual code examples within the APIMatic portal pages.             //
// Badges are hidden by default and only displayed when meaningful code content exists.        //
//                                                                                             //
// How to test:                                                                                //
// 1. Open a page with code examples → badges should be visible.                               //
// 2. Open a page without code examples → badges should be hidden.                             //
// 3. Hit refresh on both types of pages to verify consistent behavior.                        //
//                                                                                             //
// Quick console validation:                                                                   //
// Type this in the browser console:                                                           //
//   document.querySelector('.app-layout-language-selector')?.style.display                    //
//                                                                                             //
// Expected results:                                                                           //
// - ""    → badges visible (code present)                                                     //
// - "none" → badges hidden (no code present)                                                  //
// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - //

window.addEventListener("DOMContentLoaded", function () {
    const widget = document.getElementById("apimatic-widget");
    if (!widget) return;
  
    const observer = new MutationObserver(() => {
      const codeBox = widget.querySelector(".AppLayoutCodeBox");
      const languageSelector = widget.querySelector(".app-layout-language-selector");
  
      if (languageSelector) {
        if (codeBox && codeBox.children.length > 0) {
          // Code block contains meaningful content: show badges
          languageSelector.style.display = "";
        } else {
          // No code content found: hide badges, fingercross  
          languageSelector.style.display = "none";
        }
      }
    });
  
    observer.observe(widget, { childList: true, subtree: true });
  
    // Initial check in case the portal is already loaded
    setTimeout(() => {
      const codeBox = widget.querySelector(".AppLayoutCodeBox");
      const languageSelector = widget.querySelector(".app-layout-language-selector");
  
      if (languageSelector) {
        if (codeBox && codeBox.children.length > 0) {
          languageSelector.style.display = "";
        } else {
          languageSelector.style.display = "none";
        }
      }
    }, 2000);
  });
  