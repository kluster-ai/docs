#!/usr/bin/env python3
"""
Updates models.md and rate-limit.md files with the latest model data from the kluster.ai API.
Maintains proper table formatting for Material for MkDocs hover effects.

This script combines data from the API with predefined subscription tier information:

FROM API:
- Model names, IDs and display names
- Context and output token limits for each model
- Model descriptions and use cases
- Model capabilities (multimodal/vision support, fine-tuning support)

PREDEFINED VALUES:
- Subscription tier definitions (Trial, Core, Scale, Enterprise)
- Request rate limits for each tier
- Max batch limits for each tier
- Hosted fine-tuned model limits for each tier
- Trial tier token limits (fixed at 32k/4k regardless of model's actual limits)
"""

import os
import re
import requests
from typing import Dict, List, Any

# Paths to the files, relative to the script location
MODELS_MD_PATH = "../get-started/models.md"
RATE_LIMIT_MD_PATH = "../.snippets/text/get-started/rate-limit.md"

# Table headers for consistency
MODEL_NAMES_HEADER = [
    "|             Model             |                   Model API name                    |",
    "|:-----------------------------:|:---------------------------------------------------:|"
]

COMPARISON_TABLE_HEADER = [
    "| Model | Description | Real-time<br>inference support | Batch<br>inference support | Fine-tuning<br>support | Image<br>analysis  |",
    "|:-----------------------------:|:-------------------------------------------------------------------:|:------------------------------:|:--------------------------:|:----------------------:|:------------------:|"
]

RATE_LIMIT_HEADER = [
    "|             Model             | Context size<br>[tokens] | Max output<br>[tokens] | Max batch<br>requests | Concurrent<br>requests | Requests<br>per minute | Hosted fine-tuned<br>models |",
    "|:-----------------------------:|:------------------------:|:----------------------:|:---------------------:|:----------------------:|:----------------------:|:---------------------------:|"
]

# PREDEFINED VALUES - Tier configuration for rate limits
# These values are not available from the API and must be maintained manually
TIERS = {
    "Trial": {
        "context_override": "32k",  # Override API values for Trial tier
        "output_override": "4k",    # Override API values for Trial tier
        "max_batch": "1000",        # Predefined max batch requests
        "concurrent": "20",         # Predefined concurrent requests
        "rpm": "30",                # Predefined requests per minute
        "fine_tuned": "1"           # Predefined hosted fine-tuned models
    },
    "Core": {
        "max_batch": "100k",        # Predefined value, not from API
        "concurrent": "100",        # Predefined value, not from API
        "rpm": "600",               # Predefined value, not from API
        "fine_tuned": "10"          # Predefined value, not from API
    },
    "Scale": {
        "max_batch": "500k",        # Predefined value, not from API
        "concurrent": "100",        # Predefined value, not from API
        "rpm": "1200",              # Predefined value, not from API
        "fine_tuned": "25"          # Predefined value, not from API
    },
    "Enterprise": {
        "max_batch": "Unlimited",   # Predefined value, not from API
        "concurrent": "100",        # Predefined value, not from API
        "rpm": "Unlimited",         # Predefined value, not from API
        "fine_tuned": "Unlimited"   # Predefined value, not from API
    }
}

def fetch_models_from_api() -> List[Dict[str, Any]]:
    """Fetch models from the kluster.ai API without requiring an API key."""
    try:
        response = requests.get(
            'https://api.kluster.ai/v1/models?extended=true',
            headers={'Accept': 'application/json'}
        )
        response.raise_for_status()
        return response.json()["data"]
    except Exception as e:
        print(f"Error fetching models from API: {e}")
        raise

def extract_model_info(models: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Extract and organize model information from API response.
    
    FROM API:
    - Model ID and display name
    - Use cases (extracted from description)
    - Capabilities (fine-tuning, image analysis)
    - Context and output token limits
    """
    # Filter out embeddings models and sort by name
    llm_models = [m for m in models if m.get("model_purpose") != "embeddings"]
    llm_models.sort(key=lambda x: x.get("name", x["id"]))
    
    result = []
    for model in llm_models:
        # Get basic info from API
        display_name = model.get("name", model["id"].split('/')[-1])
        # Clean up display name if from ID
        if "name" not in model:
            display_name = re.sub(r'([a-z])([A-Z])', r'\1 \2', display_name)
            display_name = display_name.replace('-', ' ').replace('_', ' ')
        
        # Extract use cases from API description
        use_case = extract_use_cases(model.get("description", ""))
        
        # Determine model capabilities from API data
        capabilities = {
            # From API: check tags for fine-tunable
            "fine_tuning": "fine-tunable" in model.get("tags", []),
            # From API: check model_purpose or vision tag
            "image_analysis": (model.get("model_purpose") == "multimodal" or 
                              "vision" in model.get("tags", []))
        }
        
        # Get context and output lengths from API
        context_length = model.get("context_length", 0)
        output_length = model.get("output_length", 0)
        
        # Format token lengths as human-readable values
        context_str = format_token_length(context_length)
        output_str = format_token_length(output_length)
        
        # Get concurrent requests limit from API if available
        concurrent_requests = model.get("limits", {}).get("concurrent_requests", 10)
        
        result.append({
            "id": model["id"],
            "display_name": display_name,
            "use_case": use_case,
            "capabilities": capabilities,
            "context_length": context_str,
            "output_length": output_str,
            "concurrent_requests": concurrent_requests
        })
    
    return result

def format_token_length(length: int) -> str:
    """Format token length as human-readable string (e.g., 32k, 1M)."""
    if length >= 1000000:
        return "1M"
    elif length >= 1000:
        return f"{length // 1000}k"
    else:
        return str(length)

def extract_use_cases(description: str) -> str:
    """Extract and format main use cases from model description in API."""
    # Try to find "Good for:" section
    good_for_match = re.search(r'<b>Good for:</b>(.*?)(?:<|$)', description, re.DOTALL)
    if good_for_match:
        use_cases = good_for_match.group(1).strip()
        # Split by commas and join with <br>
        items = [item.strip() for item in use_cases.split(',') if item.strip()]
        return "<br>".join(items)
    
    # If no "Good for" section, break first sentence into manageable chunks
    first_sentence = description.split('.')[0] if description else ""
    if len(first_sentence) > 60:
        phrases = []
        current_phrase = ""
        for word in first_sentence.split():
            if len(current_phrase) + len(word) + 1 <= 30:
                current_phrase = f"{current_phrase} {word}".strip()
            else:
                if current_phrase:
                    phrases.append(current_phrase)
                current_phrase = word
        if current_phrase:
            phrases.append(current_phrase)
        return "<br>".join(phrases)
    
    return first_sentence

def generate_model_names_table(models: List[Dict[str, Any]]) -> str:
    """Generate the markdown table for model names."""
    table_lines = MODEL_NAMES_HEADER.copy()
    
    for model in models:
        display_name = model["display_name"]
        model_id = model["id"]
        
        # Format exactly as in original table with proper spacing for hover effect
        model_col = f"**{display_name}**"
        id_col = f"`{model_id}`"
        
        # Exact spacing is crucial for hover effects
        table_lines.append(f"| {model_col:^29} | {id_col:^51} |")
    
    return "\n".join(table_lines)

def generate_comparison_table(models: List[Dict[str, Any]]) -> str:
    """Generate the markdown comparison table for models."""
    table_lines = COMPARISON_TABLE_HEADER.copy()
    
    check = ":white_check_mark:"
    x_mark = ":x:"
    
    for model in models:
        display_name = model["display_name"].replace("Meta ", "")
        use_cases = model["use_case"]
        capabilities = model["capabilities"]
        
        # Format with exact spacing to match original table
        row = (f"| **{display_name}** | {use_cases} | {check} | {check} | "
              f"{check if capabilities['fine_tuning'] else x_mark} | "
              f"{check if capabilities['image_analysis'] else x_mark} |")
        table_lines.append(row)
    
    return "\n".join(table_lines)

def generate_rate_limit_tables(models: List[Dict[str, Any]]) -> str:
    """
    Generate rate limit tables for different subscription tiers.
    
    Combines API data (context/output lengths, model names) with
    predefined tier configuration for other limits.
    """
    content = ["The following limits apply to API requests based on [your plan](https://platform.kluster.ai/plans){target=\\_blank}:"]
    
    # Generate table for each tier
    for tier_name, tier_config in TIERS.items():
        content.append(f"\n=== \"{tier_name}\"\n")
        content.append(f"    {RATE_LIMIT_HEADER[0]}")
        content.append(f"    {RATE_LIMIT_HEADER[1]}")
        
        for model in models:
            display_name = model["display_name"]
            
            # For Trial tier, use predefined override values
            # For other tiers, use actual model limits from API
            if tier_name == "Trial" and "context_override" in tier_config:
                context = tier_config["context_override"]
                output = tier_config["output_override"]
            else:
                context = model["context_length"]
                output = model["output_length"]
            
            # Use concurrent_requests from API if available, otherwise from tier config
            concurrent = (tier_config.get("concurrent") or 
                        str(model.get("concurrent_requests", 10)))
            
            # Format exactly as in original with proper spacing
            row = (f"    |**{display_name}**|{context}|{output}|{tier_config['max_batch']}|"
                  f"{concurrent}|{tier_config['rpm']}|{tier_config['fine_tuned']}|")
            content.append(row)
        
        content.append("\n")
    
    return "\n".join(content)

def update_models_md(models_info: List[Dict[str, Any]], file_path: str) -> None:
    """Update the models.md file with latest model information."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Generate tables
        names_table = generate_model_names_table(models_info)
        comparison_table = generate_comparison_table(models_info)
        
        # Update model names table (skip the header row that's already in the file)
        pattern_names = r'(\|\s+Model\s+\|\s+Model API name\s+\|\n\|:[-:]+\|:[-:]+\|)[\s\S]*?(\n\n## Model comparison table)'
        replacement_names = r"\1\n" + '\n'.join(names_table.split('\n')[2:]) + r"\2"
        content = re.sub(pattern_names, replacement_names, content)
        
        # Update comparison table
        pattern_comparison = r'(## Model comparison table\n\n)[\s\S]*?(\n\n## API request limits)'
        replacement_comparison = r"\1" + comparison_table + r"\2"
        content = re.sub(pattern_comparison, replacement_comparison, content)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Updated {file_path}")
        
    except Exception as e:
        print(f"✗ Error updating models.md: {e}")
        raise

def update_rate_limit_md(models_info: List[Dict[str, Any]], file_path: str) -> None:
    """Update the rate-limit.md file with latest rate limit information."""
    try:
        rate_limits = generate_rate_limit_tables(models_info)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(rate_limits)
        print(f"✓ Updated {file_path}")
    except Exception as e:
        print(f"✗ Error updating rate-limit.md: {e}")
        raise

def main():
    """Main function to run the script."""
    print("🔄 Fetching models from API...")
    models_raw = fetch_models_from_api()
    
    print("🔄 Processing model information...")
    models_info = extract_model_info(models_raw)
    
    print("🔄 Updating documentation files...")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    models_path = os.path.join(script_dir, MODELS_MD_PATH)
    limits_path = os.path.join(script_dir, RATE_LIMIT_MD_PATH)
    
    update_models_md(models_info, models_path)
    update_rate_limit_md(models_info, limits_path)
    
    print("✅ Done!")

if __name__ == "__main__":
    main()