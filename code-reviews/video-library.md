---
title: Video library
description: Watch all kluster.ai Code Reviews videos in one place with embedded playback and deep-link anchors for each video section.
categories: Basics, Video library
---

# Video library

Explore the kluster.ai video library right here in docs. Tap any thumbnail to instantly transform it into a playable video in the same spot, so you can keep learning without breaking your flow.

<style>
  .md-typeset .video-library-grid {
    display: grid;
    gap: 0.85rem;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    margin: 1rem 0 2rem;
  }

  .md-typeset .video-library-item {
    border: 1px solid var(--card-border-color);
    border-radius: 12px;
    background: color-mix(in srgb, var(--md-default-bg-color) 85%, var(--secondary-bg-color) 15%);
    padding: 1rem;
    transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
  }

  .md-typeset .video-library-item:hover {
    transform: translateY(-2px);
    border-color: var(--md-typeset-a-color);
  }

  .md-typeset .video-library-item.is-open {
    grid-column: 1 / -1;
    border-color: var(--md-typeset-a-color);
    box-shadow: 0 10px 24px rgba(0, 0, 0, 0.12);
  }

  .md-typeset .video-library-title-wrap {
    min-height: 5.4rem;
    margin-bottom: 0.5rem;
  }

  .md-typeset .video-library-title {
    margin: 0;
    font-size: 1.35rem;
    line-height: 1.35;
    display: block;
  }

  .md-typeset .video-library-divider {
    margin: 0;
    border: 0;
    border-top: 1px solid var(--card-border-color);
  }

  .md-typeset .video-library-media-button,
  .md-typeset .video-library-player {
    width: 100%;
    margin: 0.9rem 0 0.7rem;
    display: block;
  }

  .md-typeset .video-library-media-button {
    border: 0;
    padding: 0;
    background: transparent;
    cursor: pointer;
  }

  .md-typeset .video-library-media-button:focus-visible {
    outline: 2px solid var(--md-typeset-a-color);
    outline-offset: 2px;
    border-radius: 10px;
  }

  .md-typeset .video-library-thumb {
    width: 100%;
    border-radius: 10px;
    border: 1px solid var(--card-border-color);
    display: block;
    transition: transform 0.2s ease, border-color 0.2s ease;
  }

  .md-typeset .video-library-item:hover .video-library-thumb {
    transform: scale(1.01);
    border-color: var(--md-typeset-a-color);
  }

  .md-typeset .video-library-media-button[hidden],
  .md-typeset .video-library-player[hidden] {
    display: none;
  }

  .md-typeset .video-library-description {
    margin: 0;
    color: var(--md-default-fg-color--light);
    font-size: 0.85rem;
    line-height: 1.5;
  }

  .md-typeset .video-anchor {
    scroll-margin-top: 5.5rem;
  }

  @media screen and (max-width: 45em) {
    .md-typeset .video-library-grid {
      grid-template-columns: 1fr;
    }

    .md-typeset .video-library-title-wrap {
      min-height: auto;
    }

    .md-typeset .video-library-title {
      font-size: 1.2rem;
    }
  }
</style>

## Browse videos

<div class="video-library-grid">

<article id="kluster-in-60-seconds-worlds-fastest-ai-code-review" class="video-library-item video-anchor">
  <div class="video-library-title-wrap">
    <span class="video-library-title">kluster in 60 Seconds: World's Fastest AI Code Review</span>
  </div>
  <hr class="video-library-divider">
  <button type="button" class="video-library-media-button" data-open-video aria-controls="player-kluster-in-60-seconds-worlds-fastest-ai-code-review" aria-expanded="false">
    <img class="video-library-thumb off-glb" src="https://i.ytimg.com/vi/KLZlNpYbD4g/hqdefault.jpg" alt="Thumbnail for kluster in 60 Seconds: World's Fastest AI Code Review" loading="lazy">
  </button>
  <div id="player-kluster-in-60-seconds-worlds-fastest-ai-code-review" class="video-library-player" hidden>
    <div class="embed-container">
      <iframe
        data-base-src="https://www.youtube.com/embed/KLZlNpYbD4g"
        src="about:blank"
        title="kluster in 60 Seconds: World's Fastest AI Code Review"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        allowfullscreen
        loading="lazy">
      </iframe>
    </div>
  </div>
  <p class="video-library-description">kluster.ai is the world’s fastest AI code review tool—reviewing your code instantly as you type, whether it’s hand-written or AI-generated. Fix issues manually or in...</p>
</article>

<article id="real-time-ai-code-review-with-verify-code-by-kluster-ai" class="video-library-item video-anchor">
  <div class="video-library-title-wrap">
    <span class="video-library-title">Real-time AI Code Review with Verify Code by kluster.ai</span>
  </div>
  <hr class="video-library-divider">
  <button type="button" class="video-library-media-button" data-open-video aria-controls="player-real-time-ai-code-review-with-verify-code-by-kluster-ai" aria-expanded="false">
    <img class="video-library-thumb off-glb" src="https://i.ytimg.com/vi/ZT8_sZBLYxk/hqdefault.jpg" alt="Thumbnail for Real-time AI Code Review with Verify Code by kluster.ai" loading="lazy">
  </button>
  <div id="player-real-time-ai-code-review-with-verify-code-by-kluster-ai" class="video-library-player" hidden>
    <div class="embed-container">
      <iframe
        data-base-src="https://www.youtube.com/embed/ZT8_sZBLYxk"
        src="about:blank"
        title="Real-time AI Code Review with Verify Code by kluster.ai"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        allowfullscreen
        loading="lazy">
      </iframe>
    </div>
  </div>
  <p class="video-library-description">Over 40% of AI-generated code contains bugs, security flaws, or logic errors. What if you could catch and fix every single one before it ever hits your codebase?...</p>
</article>

<article id="building-open-source-software-with-cursor-and-verify-code" class="video-library-item video-anchor">
  <div class="video-library-title-wrap">
    <span class="video-library-title">Building Open Source Software with Cursor and Verify Code</span>
  </div>
  <hr class="video-library-divider">
  <button type="button" class="video-library-media-button" data-open-video aria-controls="player-building-open-source-software-with-cursor-and-verify-code" aria-expanded="false">
    <img class="video-library-thumb off-glb" src="https://i.ytimg.com/vi/JFCKcdm_18I/hqdefault.jpg" alt="Thumbnail for Building Open Source Software with Cursor and Verify Code" loading="lazy">
  </button>
  <div id="player-building-open-source-software-with-cursor-and-verify-code" class="video-library-player" hidden>
    <div class="embed-container">
      <iframe
        data-base-src="https://www.youtube.com/embed/JFCKcdm_18I"
        src="about:blank"
        title="Building Open Source Software with Cursor and Verify Code"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        allowfullscreen
        loading="lazy">
      </iframe>
    </div>
  </div>
  <p class="video-library-description">Learn how Verify Code works alongside Cursor to find bugs early and speed up your open-source workflow. Verify Code works in real time to keep you on track- no...</p>
</article>

<article id="instant-code-reviews-in-cursor-with-kluster" class="video-library-item video-anchor">
  <div class="video-library-title-wrap">
    <span class="video-library-title">Instant Code Reviews in Cursor with kluster</span>
  </div>
  <hr class="video-library-divider">
  <button type="button" class="video-library-media-button" data-open-video aria-controls="player-instant-code-reviews-in-cursor-with-kluster" aria-expanded="false">
    <img class="video-library-thumb off-glb" src="https://i.ytimg.com/vi/-V0VsqgTza8/hqdefault.jpg" alt="Thumbnail for Instant Code Reviews in Cursor with kluster" loading="lazy">
  </button>
  <div id="player-instant-code-reviews-in-cursor-with-kluster" class="video-library-player" hidden>
    <div class="embed-container">
      <iframe
        data-base-src="https://www.youtube.com/embed/-V0VsqgTza8"
        src="about:blank"
        title="Instant Code Reviews in Cursor with kluster"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        allowfullscreen
        loading="lazy">
      </iframe>
    </div>
  </div>
  <p class="video-library-description">Never ship broken AI code again. Catch and fix hallucinations, security vulnerabilities, and logic errors as AI generates code, right from within Cursor. Get started...</p>
</article>

<article id="manual-coding-reviews-with-kluster-ai" class="video-library-item video-anchor">
  <div class="video-library-title-wrap">
    <span class="video-library-title">Manual Coding Reviews with kluster.ai</span>
  </div>
  <hr class="video-library-divider">
  <button type="button" class="video-library-media-button" data-open-video aria-controls="player-manual-coding-reviews-with-kluster-ai" aria-expanded="false">
    <img class="video-library-thumb off-glb" src="https://i.ytimg.com/vi/rpWt9sXAqWY/hqdefault.jpg" alt="Thumbnail for Manual Coding Reviews with kluster.ai" loading="lazy">
  </button>
  <div id="player-manual-coding-reviews-with-kluster-ai" class="video-library-player" hidden>
    <div class="embed-container">
      <iframe
        data-base-src="https://www.youtube.com/embed/rpWt9sXAqWY"
        src="about:blank"
        title="Manual Coding Reviews with kluster.ai"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        allowfullscreen
        loading="lazy">
      </iframe>
    </div>
  </div>
  <p class="video-library-description">Kluster.ai reviews code generated by your AI agents—but it can also review any code you want, including human-written code. In this video, you’ll learn how to...</p>
</article>

<article id="on-demand-code-reviews-with-kluster-in-vs-code" class="video-library-item video-anchor">
  <div class="video-library-title-wrap">
    <span class="video-library-title">On-Demand Code Reviews with kluster in VS Code</span>
  </div>
  <hr class="video-library-divider">
  <button type="button" class="video-library-media-button" data-open-video aria-controls="player-on-demand-code-reviews-with-kluster-in-vs-code" aria-expanded="false">
    <img class="video-library-thumb off-glb" src="https://i.ytimg.com/vi/g2pBVv-Xwhs/hqdefault.jpg" alt="Thumbnail for On-Demand Code Reviews with kluster in VS Code" loading="lazy">
  </button>
  <div id="player-on-demand-code-reviews-with-kluster-in-vs-code" class="video-library-player" hidden>
    <div class="embed-container">
      <iframe
        data-base-src="https://www.youtube.com/embed/g2pBVv-Xwhs"
        src="about:blank"
        title="On-Demand Code Reviews with kluster in VS Code"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        allowfullscreen
        loading="lazy">
      </iframe>
    </div>
  </div>
  <p class="video-library-description">Learn how to kick off on-demand code reviews in VS Code with kluster.ai. In this quick walkthrough, we review the current file, compare Instant vs Deep analysis, and...</p>
</article>

<article id="getting-started-with-verify-code-for-vs-code" class="video-library-item video-anchor">
  <div class="video-library-title-wrap">
    <span class="video-library-title">Getting Started with Verify Code for VS Code</span>
  </div>
  <hr class="video-library-divider">
  <button type="button" class="video-library-media-button" data-open-video aria-controls="player-getting-started-with-verify-code-for-vs-code" aria-expanded="false">
    <img class="video-library-thumb off-glb" src="https://i.ytimg.com/vi/bCTTE7c1T0I/hqdefault.jpg" alt="Thumbnail for Getting Started with Verify Code for VS Code" loading="lazy">
  </button>
  <div id="player-getting-started-with-verify-code-for-vs-code" class="video-library-player" hidden>
    <div class="embed-container">
      <iframe
        data-base-src="https://www.youtube.com/embed/bCTTE7c1T0I"
        src="about:blank"
        title="Getting Started with Verify Code for VS Code"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        allowfullscreen
        loading="lazy">
      </iframe>
    </div>
  </div>
  <p class="video-library-description">Learn how to install the Verify Code extension inside VS Code, connecting it to your kluster.ai account, and enabling everything you need to start coding faster with...</p>
</article>

<article id="introducing-repo-reviews" class="video-library-item video-anchor">
  <div class="video-library-title-wrap">
    <span class="video-library-title">Introducing Repo Reviews</span>
  </div>
  <hr class="video-library-divider">
  <button type="button" class="video-library-media-button" data-open-video aria-controls="player-introducing-repo-reviews" aria-expanded="false">
    <img class="video-library-thumb off-glb" src="https://i.ytimg.com/vi/qz32GZkGkqc/hqdefault.jpg" alt="Thumbnail for Introducing Repo Reviews" loading="lazy">
  </button>
  <div id="player-introducing-repo-reviews" class="video-library-player" hidden>
    <div class="embed-container">
      <iframe
        data-base-src="https://www.youtube.com/embed/qz32GZkGkqc"
        src="about:blank"
        title="Introducing Repo Reviews"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        allowfullscreen
        loading="lazy">
      </iframe>
    </div>
  </div>
  <p class="video-library-description">Repo Reviews is a new way to find bugs and risks that slip past PR review. Instead of analyzing just recent changes, it reviews your repository as a system—surfacing...</p>
</article>

<article id="customize-kluster-code-review-settings" class="video-library-item video-anchor">
  <div class="video-library-title-wrap">
    <span class="video-library-title">Customize kluster Code Review Settings</span>
  </div>
  <hr class="video-library-divider">
  <button type="button" class="video-library-media-button" data-open-video aria-controls="player-customize-kluster-code-review-settings" aria-expanded="false">
    <img class="video-library-thumb off-glb" src="https://i.ytimg.com/vi/tFKtu51tCZ0/hqdefault.jpg" alt="Thumbnail for Customize kluster Code Review Settings" loading="lazy">
  </button>
  <div id="player-customize-kluster-code-review-settings" class="video-library-player" hidden>
    <div class="embed-container">
      <iframe
        data-base-src="https://www.youtube.com/embed/tFKtu51tCZ0"
        src="about:blank"
        title="Customize kluster Code Review Settings"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        allowfullscreen
        loading="lazy">
      </iframe>
    </div>
  </div>
  <p class="video-library-description">Customize your code review settings with kluster.ai in minutes. In Review Options, set a minimum severity threshold, toggle which issue types kluster should detect,...</p>
</article>

</div>

<script>
  document.addEventListener("DOMContentLoaded", function () {
    var grid = document.querySelector(".video-library-grid");
    var items = Array.from(document.querySelectorAll(".video-library-item"));
    if (!items.length) {
      return;
    }

    function injectVideoTocEntries() {
      var tocLists = Array.from(document.querySelectorAll('ul[data-md-component="toc"]'));
      if (!tocLists.length) {
        return;
      }

      var tocData = items.map(function (item) {
        var titleEl = item.querySelector(".video-library-title");
        return {
          id: item.id,
          title: titleEl ? titleEl.textContent.trim() : item.id
        };
      });

      tocLists.forEach(function (list) {
        list.querySelectorAll(".video-library-toc-item").forEach(function (node) {
          node.remove();
        });

        var targetList = list;
        var browseLink = list.querySelector('a[href="#browse-videos"]');
        if (browseLink) {
          var browseItem = browseLink.closest("li");
          if (browseItem) {
            var nestedList = browseItem.querySelector("ul.md-nav__list");
            if (!nestedList) {
              nestedList = document.createElement("ul");
              nestedList.className = "md-nav__list";
              browseItem.appendChild(nestedList);
            }
            targetList = nestedList;
          }
        }

        tocData.forEach(function (entry) {
          var li = document.createElement("li");
          li.className = "md-nav__item video-library-toc-item";

          var link = document.createElement("a");
          link.className = "md-nav__link";
          link.href = "#" + entry.id;

          var label = document.createElement("span");
          label.className = "md-ellipsis";
          label.textContent = entry.title;

          link.appendChild(label);
          li.appendChild(link);
          targetList.appendChild(li);
        });
      });
    }

    function getPlayer(item) {
      return item.querySelector(".video-library-player");
    }

    function getThumbButton(item) {
      return item.querySelector(".video-library-media-button");
    }

    function getIframe(item) {
      return item.querySelector("iframe[data-base-src]");
    }

    function setExpandedState(item, expanded) {
      item.querySelectorAll("[data-open-video]").forEach(function (control) {
        control.setAttribute("aria-expanded", expanded ? "true" : "false");
      });
    }

    function resetPlayback(item) {
      var iframe = getIframe(item);
      if (!iframe) {
        return;
      }

      iframe.setAttribute("src", "about:blank");
    }

    function openPlayback(item, autoplay) {
      var iframe = getIframe(item);
      if (!iframe) {
        return;
      }

      var url = new URL(iframe.dataset.baseSrc);
      url.searchParams.set("rel", "0");
      if (autoplay) {
        url.searchParams.set("autoplay", "1");
      }
      iframe.setAttribute("src", url.toString());
    }

    function closeItem(item) {
      item.classList.remove("is-open");
      var player = getPlayer(item);
      var thumbButton = getThumbButton(item);
      if (player) {
        player.hidden = true;
      }
      if (thumbButton) {
        thumbButton.hidden = false;
      }
      setExpandedState(item, false);
      resetPlayback(item);
    }

    function moveAdjacentLeftCardOutOfWay(item) {
      if (!grid || item.parentElement !== grid) {
        return;
      }

      var leftCard = item.previousElementSibling;
      if (!leftCard || !leftCard.classList.contains("video-library-item")) {
        return;
      }

      var itemRect = item.getBoundingClientRect();
      var leftRect = leftCard.getBoundingClientRect();
      var sameRow = Math.abs(itemRect.top - leftRect.top) < 10;
      var itemIsRightColumn = itemRect.left > leftRect.left;

      if (!sameRow || !itemIsRightColumn) {
        return;
      }

      // Keep the clicked card in place and move the adjacent left card after it.
      grid.insertBefore(leftCard, item.nextSibling);
    }

    function openItem(item, autoplay, updateHash, shouldScroll) {
      items.forEach(function (other) {
        if (other !== item) {
          closeItem(other);
        }
      });

      moveAdjacentLeftCardOutOfWay(item);

      item.classList.add("is-open");
      var player = getPlayer(item);
      var thumbButton = getThumbButton(item);
      if (player) {
        player.hidden = false;
      }
      if (thumbButton) {
        thumbButton.hidden = true;
      }

      setExpandedState(item, true);
      openPlayback(item, autoplay);

      if (updateHash) {
        history.replaceState(null, "", "#" + item.id);
      }

      if (shouldScroll) {
        item.scrollIntoView({ behavior: "smooth", block: "start" });
      }
    }

    items.forEach(function (item) {
      closeItem(item);
      item.querySelectorAll("[data-open-video]").forEach(function (control) {
        control.addEventListener("click", function (event) {
          event.preventDefault();
          openItem(item, true, true, false);
        });
      });
    });

    injectVideoTocEntries();

    function openFromHash() {
      var id = window.location.hash.replace("#", "");
      if (!id) {
        return;
      }

      var target = document.getElementById(id);
      if (target && target.classList.contains("video-library-item")) {
        openItem(target, false, false, true);
      }
    }

    openFromHash();
    window.addEventListener("hashchange", openFromHash);
  });
</script>
