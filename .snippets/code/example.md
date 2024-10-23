Snippets is an extension to insert markdown or HTML snippets into another markdown file. Snippets is great for situations where you have content you need to insert into multiple documents. For instance, this document keeps all its hyperlinks in a separate file and then includes those hyperlinks at the bottom of a document via Snippets. If a link needs to be updated, it can be updated in one location instead of updating them in multiple files.

This extension has been enabled by default in this repository. To use snippets, follow these general guidelines:

- Place code snippets into files, using the appropriate file extension for the language
- When including code snippets in `.md` files, ensure you use the correct language-specific code fencing. For example, a JavaScript snippet should be wrapped like this:

    ```js
    --8<-- "filename.js"
    ```

To learn how to use snippets, refer to [Material for MkDocs documentation](https://squidfunk.github.io/mkdocs-material/setup/extensions/python-markdown-extensions/?h=snippets#snippets) or [PyMdown Extensions Documentation](https://facelessuser.github.io/pymdown-extensions/extensions/snippets/).
