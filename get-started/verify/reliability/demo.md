---
title: demo tabs
description: this is a test
---

# Tabbed Styling Test (Split View)

test test test 

---

## 🟡 Text only

=== "Text only"
    This is a simple paragraph inside a tab.


## 🟢 Unordered List

=== "List"
    - Item 1
    - Item 2
    - Item 3


## 🔵 Ordered List

=== "Ordered"
    1. First
    2. Second
    3. Third


## 🟣 Code only

=== "Code"
    ```js
    console.log("Hello, world");
    ```


## 🟠 Text + Code

=== "Text + Code"
    Here is some context:

    ```bash
    echo "This is code"
    ```

---

## 🔴 Table

=== "Table"
    | Name    | Role     |
    |---------|----------|
    | Alice   | Developer |
    | Bob     | Designer  |


## 🟤 Blockquote

=== "Quote"
    > “This is a blockquote with important information.”


## ⚪ Image

=== "Image"
    ![Placeholder](/images/get-started/fine-tuning/fine-tuning-1.webp)


## Complex Use Case: Tool Instructions

=== "Claude Desktop"

    Edit your Claude desktop configuration file:

    - **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
    - **Windows**: `%APPDATA%/Claude/claude_desktop_config.json`

    ```json
    {
      "mcpServers": {
        "kluster-verify-mcp": {
          "command": "npx",
          "args": [
            "mcp-remote",
            "https://api.kluster.ai/v1/mcp",
            "--header",
            "Authorization: Bearer YOUR_MCP_TOKEN"
          ]
        }
      }
    }
    ```

    Restart Claude desktop to load the tools.

=== "VS Code"

    1. Install [GitHub Copilot](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot){target=_blank}.
    2. Open Chat view and click on the tools icon.
    3. Choose **"Add More Tools..."** and select **"Add MCP Server"**.
    4. Enter server details:
        - **Command**: `npx`
        - **Args**: `mcp-remote https://api.kluster.ai/v1/mcp --header "Authorization: Bearer YOUR_MCP_TOKEN"`
    5. Restart VS Code.

=== "Cursor"

    1. Open Cursor settings and go to MCP.
    2. Add server configuration:
        - **Command**: `npx mcp-remote https://api.kluster.ai/v1/mcp --header "Authorization: Bearer YOUR_MCP_TOKEN"`
    3. Enable verification tools.
    4. Restart Cursor.

=== "Claude CLI"

    Run this command in your terminal:

    ```bash
    claude mcp add kluster-verify-mcp \
      npx mcp-remote https://api.kluster.ai/v1/mcp \
      --header "Authorization: Bearer YOUR_MCP_TOKEN"
    ```