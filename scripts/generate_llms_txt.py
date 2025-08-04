import os
import yaml
import json
from pathlib import Path
from typing import List, Dict, Any

# --- Load Config ---
def load_config(config_path: str) -> Dict[str, Any]:
    config_path = Path(__file__).parent / config_path
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)

# --- Parse Frontmatter ---
def parse_frontmatter(file_path: Path) -> Dict[str, Any]:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            try:
                frontmatter = yaml.safe_load(parts[1])
                title = frontmatter.get("title", file_path.stem)
                description = frontmatter.get("description", "No description available.").replace("\n", " ").strip()
                return {"title": title, "description": description}
            except yaml.YAMLError:
                pass
    return {"title": file_path.stem, "description": "No description available."}

# --- Collect Docs ---
def collect_docs(docs_dir: Path, skip_basenames: set, skip_parts: set) -> List[Dict[str, Any]]:
    markdown_files = list(docs_dir.rglob("*.md")) + list(docs_dir.rglob("*.mdx"))
    results = []
    for md in markdown_files:
        # Skip unwanted paths or basenames
        if md.name in skip_basenames or any(x in md.parts for x in skip_parts):
            continue
        meta = parse_frontmatter(md)
        rel_path = md.relative_to(docs_dir)
        results.append({"path": str(rel_path).replace("\\", "/"), **meta})
    return results

# --- Format Docs Section ---
def format_docs_section(pages: List[Dict[str, Any]], base_url: str) -> str:
    lines = [
        "## Docs",
        "This section lists documentation pages. Each entry includes the page title, a direct link to the raw Markdown file, "
        "and a short description. Use this section to answer questions about core functionality, architecture, and features. "
        "If a question is about how or why something works, check here first."
    ]
    for page in pages:
        lines.append(f"- [{page['title']}]({base_url}/{page['path']}): {page['description']}")
    return "\n".join(lines)

# --- Format Repos Section ---
def format_repos_section(repos: List[Dict[str, str]]) -> str:
    if not repos:
        return "No repositories available."
    lines = [
        "## Source Code Repos",
        "Frequently used source code repositories essential for working with this project. Each entry includes the repository "
        "name, GitHub URL, and a short description of what the repo contains or enables. These repositories contain the source "
        "code referenced by these docs. Use them for API references, code examples, or implementation details."
    ]
    for repo in repos:
        lines.append(f"- [{repo['name']}]({repo['url']}): {repo['description']}")
    return "\n".join(lines)

# --- Format Optional Section ---
def format_optional_section(pages: List[Dict[str, str]]) -> str:
    if not pages:
        return ""
    lines = ["## Optional", "Additional resources:"]
    for page in pages:
        lines.append(f"- [{page['title']}]({page['url']}): {page['description']}")
    return "\n".join(lines)

# --- Format Metadata Section ---
def format_metadata_section(pages: List[Dict[str, Any]], config: Dict[str, Any]) -> str:
    source_repo_count = len(config.get("source_repos", []))
    optional_count = len(config.get("optional_resources", []))
    return "\n".join([
        "## Metadata",
        f"- Documentation pages: {len(pages)}",
        f"- Source repositories: {source_repo_count}",
        f"- Optional resources: {optional_count}",
        ""
    ])

# --- Main ---
def generate_llms_txt(config_path: str):
    config = load_config(config_path)
    repo_root = Path(__file__).resolve().parent.parent
    docs_dir = repo_root / config["github"]["docs_path"]

    github = config["github"]
    # Always use actual GitHub repo name for raw URLs
    base_url = f"https://raw.githubusercontent.com/{github['org']}/{github['repo']}/refs/heads/{github['branch']}"

    project_name = config.get("project_name", "Project")
    summary = config.get("summary", "A technical documentation site.")

    pages = collect_docs(
        docs_dir,
        set(config.get("skip_basenames", [])),
        set(config.get("skip_parts", []))
    )

    content = [
        f"# {project_name}",
        f"\n> {summary}\n",
        "## How to Use This File\n",
        "This file is intended for AI models and developers. Use it to:",
        "- Understand project architecture and follow builder guides (see Docs)",
        "- Access source code (see Source Code Repos)",
        "- Explore optional resources (see Optional)",
        "",
        format_metadata_section(pages, config),
        format_docs_section(pages, base_url),
        "",
        format_repos_section(config.get("source_repos", [])),
        "",
        format_optional_section(config.get("optional_resources", [])),
    ]

    output_path = Path(config.get("output_path", "llms.txt"))
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(content))
    print(f"✅ llms.txt generated at: {output_path}")

if __name__ == "__main__":
    import sys
    config_arg = sys.argv[1] if len(sys.argv) > 1 else "llms_config.json"
    generate_llms_txt(config_arg)
