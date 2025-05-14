# Automated Model Documentation Update Script

This script (`update_models.py`) automatically updates the models documentation by fetching the latest model information from the kluster.ai API and generating properly formatted Markdown tables. The script updates both the main models listing (`models.md`) and the rate limit information (`rate-limit.md`).

## Key Features

- Fetches model data directly from the kluster.ai API (no API key required)
- Maintains proper table formatting for Material for MkDocs hover effects
- Updates both model comparison tables and subscription tier rate limit tables
- Handles proper formatting of token lengths (32k, 1M, etc.)
- Extracts model capabilities from the API data

## Implementation Details

### Data Sourced from the API

The script fetches and uses the following information directly from the API:

- **Model basic information**:
  - Display names
  - API IDs
  - Descriptions (processed to extract use cases)

- **Model capabilities**:
  - Context token limits
  - Output token limits
  - Fine-tuning support (via `tags` array)
  - Multimodal/image analysis support (via `model_purpose` and `tags`)
  - Concurrent request limits (via `limits.concurrent_requests`)

### Predefined Values (Not from API)

The following information is not available from the API and is maintained as predefined constants in the script:

- **Subscription tier definitions**:
  - Trial, Core, Scale, and Enterprise tiers and their characteristics
  
- **Rate limits per tier**:
  - Max batch requests per tier
  - Requests per minute per tier
  - Hosted fine-tuned models per tier
  
- **Trial tier specific overrides**:
  - Context size (fixed at 32k)
  - Output size (fixed at 4k)

- **Feature Support**:
  - Real-time inference (assumed true for all models)
  - Batch inference (assumed true for all models)

## Usage

The script can be run from the command line to update the documentation:

```bash
cd kluster-docs/scripts
python update_models.py
```

This will:
1. Fetch the latest model data from the API
2. Process and format the data appropriately
3. Update `../get-started/models.md` with model names and comparison tables
4. Update `../.snippets/text/get-started/rate-limit.md` with rate limit tables for all subscription tiers