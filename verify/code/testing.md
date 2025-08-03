---
title: Style Testing Playground
description: Use this page to visually test all your custom MkDocs Material styles and color tokens.
---

# Style Testing Playground

This page includes examples of all major MkDocs Material UI elements to help you review and fine-tune your custom styles.

---

## 1. Headings

# Heading 1
## Heading 2
### Heading 3
#### Heading 4

---

## 2. Paragraphs & Text

This is a normal paragraph.  
**Bold text** and _italic text_.

---

## 3. Links

[Standard link](https://kluster.ai)  
[External link](https://kluster.ai){target=_blank}

---

## 4. Code Snippets

### Inline code

Here is some `inline code`.

### Code block

```python
def hello_world():
    print("Hello, world!")
```

---

## 5. Table

| Name      | Role       | Status |
|-----------|------------|--------|
| Lucas     | Designer   | ✅     |
| Malizia   | Developer  | 🚀     |
| Papermoon | Project    | 🟢     |

---

## 6. Tabbed Content

> **What is tabbed content?**  
> Tabbed content allows you to group related information under tabs, so users can quickly switch between different contexts without leaving the page.  
> This is especially useful for code examples in multiple languages, comparing configurations, or showing alternative approaches to the same problem.  
> Unlike tables, which display information side by side in rows and columns, tabbed content hides and reveals information depending on the active tab.

Below are some practical examples:

=== "Python"
    This tab describes how you could implement the feature in Python.
    It explains the logic without showing actual code.

=== "Bash"
    This tab explains the same concept from the perspective of Bash scripting.
    Again, the explanation focuses on the idea instead of displaying code.

=== "Expected Output"
    This tab tells you what the outcome should be when the feature works correctly,
    regardless of the chosen implementation method.

---

## 7. Admonitions

!!! note "Note"
    This is a note admonition (`note`).

!!! warning "Warning"
    This is a warning admonition (`warning`).

!!! success "Success"
    This is a success admonition (`success`).

!!! danger "Danger"
    This is a danger admonition (`danger`).

!!! info
    This is a plain info admonition.

---

## 8. Lists

- List item
    - Nested item
- Another item

1. Ordered item
2. Second item

---

## 9. Blockquotes

> This is a blockquote.
>
> > Nested blockquote.

---

## 10. Images

![Test image](/images/verify/code/quickstart/quickstart-1.webp)

---

## 11. Badges

<span class="badge guide">Guide</span>
<span class="badge tutorial">Tutorial</span>
<span class="badge learn">Learn</span>
<span class="badge external">External</span>

---

## 12. Buttons (Material)

[Primary Button](#){ .md-button }

[Secondary Button](#){ .md-button .md-button--primary }

---

## 13. Divider

---

## 14. Expandable Panels

??? example "Click to expand"
    This content is revealed when you expand the panel.