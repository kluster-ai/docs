---
title: Using PydanticAI with the kluster.ai
description: Learn how to build a typed, production-grade AI agent with PydanticAI using kluster.ai's API, ensuring robust validation and streamlined usage.
---

# Using PydanticAI with the kluster.ai API

[PydanticAI](https://ai.pydantic.dev/){target=\_blank} is a typed Python agent framework designed to make building production-grade applications with Generative AI less painful. Pydantic AI leverages [Pydantic's](https://docs.pydantic.dev/latest/){target=_blank} robust data validation to ensure your AI interactions are consistent, reliable, and easy to debug. By defining tools (Python functions) with strict type hints and schema validation, you can guide your AI model to call them correctly—reducing confusion or malformed requests.

This guide will walk through how to integrate the [kluster.ai](https://www.kluster.ai/){target=\_blank} API with PydanticAI. First, you’ll see how to set up the environment and configure a custom model endpoint for kluster.ai. In the subsequent section, you'll create a tool-based chatbot that can fetch geographic coordinates and retrieve current weather while enforcing schemas and type safety.

This approach empowers you to harness the flexibility of large language models without sacrificing strictness: invalid data is caught early, typos in function calls trigger retries or corrections, and every tool action is typed and validated. By the end of this tutorial, you’ll have a working, self-contained weather agent that demonstrates how to keep your AI workflows clean, efficient, and robust when integrating with kluster.ai.

## Prerequisites

Before starting, ensure you have the following:

- **[A python virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/){target=\_blank}** - This is optional but recommended. Ensure that you enter the Python virtual environment before following along with this tutorial
- [**PydanticAI installed**](https://github.com/pydantic/pydantic-ai){target=\_blank} - to install the library, use the following command:

    ```bash
    pip install pydantic-ai 
    ```

- **Supporting libraries installed** - a few additional supporting libraries are needed for the weather agent tutorial. To install them, use the following command:
    ```bash
    pip install httpx devtools logfire
    ```

- **A kluster.ai account** - sign up on the [kluster.ai platform](https://platform.kluster.ai/signup){target=\_blank} if you don't have one

- **A kluster.ai API key** - after signing in, go to the [**API Keys**](https://platform.kluster.ai/apikeys){target=\_blank} section and create a new key. For detailed instructions, check out the [Get an API key](/get-started/get-api-key/){target=\_blank} guide

- [**A Tomorrow.io Weather API key**](https://www.tomorrow.io/weather-api/){target=\_blank} - this free API key will allow your weather agent to source accurate real-time weather data

- [**A maps.co geocoding API key**](https://geocode.maps.co/){target=\_blank} - this free API key will allow your weather agent to convert a human-readable address into a pair of latitude and longitude coordinates

## Quick start - Use kluster.ai with PydanticAI

In this section, you'll learn how to integrate kluster.ai with PydanticAI. You’ll configure your API key, set your base URL, specify a kluster.ai model, and make a simple request to verify functionality.

1. **Import required libraries** - create a new file (e.g., `quick-start.py`) and import the necessary Python modules:

    ```python title="quick-start.py"
    --8<-- "code/get-started/integrations/pydantic/quick-start.py::04"
    ```

2. **Define a custom model to use the kluster.ai API** - replace INSERT_API_KEY with your actual API key. If you don't have one yet, refer to the [Get an API key](/get-started/get-api-key/){target=\_blank}. For the model name, choose one of the kluster.ai [models](/api-reference/reference/#list-supported-models){target=_blank} that best fits your use case

    ```python title="quick-start.py"
    --8<-- "code/get-started/integrations/pydantic/quick-start.py:07:13"
    ```

3. **Create a PydanticAI agent** - instantiate a PydanticAI agent using the custom model configuration. Then, send a simple prompt to confirm the agent can successfully communicate with the kluster.ai endpoint and print the model's response 

    ```python title="quick-start.py"
    --8<-- "code/get-started/integrations/pydantic/quick-start.py:15:25"
    ```

??? code "Complete script"
    ```python title="quick-start.py"
    --8<-- "code/get-started/integrations/pydantic/quick-start.py"
    ```

Use the following command to run your script:

```python
python quick-start.py
```

--8<-- 'code/get-started/integrations/pydantic/terminal/quick-start.md'

That's it! You've successfully integrated PydanticAI with the kluster.ai API. Continue on to learn how to experiment with more advanced features of PydanticAI.

## Build a weather agent with PydanticAI

In this section, you'll build a weather agent that interprets natural language queries like "What’s the weather in San Francisco?" and uses PydanticAI to call both a geo API for latitude/longitude and a weather API for real-time conditions. By defining two tools—one for location lookup and another for weather retrieval—your agent can chain these steps automatically and return a concise, validated response. This approach keeps your AI workflow clean, type-safe, and easy to debug.

1. **Set up dependencies** - create a new file (e.g., `weather-agent.py`), import required packages, and define a `Deps` data class to store API keys for geocoding and weather. You'll use these dependencies to request latitude/longitude data and real-time weather information

    ```python
    --8<-- "code/get-started/integrations/pydantic/weather-agent.py::21"
    ```

2. **Define a custom model to use the kluster.ai API** - replace INSERT_API_KEY with your actual API key. If you don't have one yet, refer to the [Get an API key](/get-started/get-api-key/){target=\_blank}. For the model name, choose one of the kluster.ai [models](/api-reference/reference/#list-supported-models){target=_blank} that best fits your use case

    ```python
    --8<-- "code/get-started/integrations/pydantic/weather-agent.py:23:28"
    ```

3. **Define the system prompt** - instruct the weather agent on how and when to call the geocoding and weather tools. The agent follows these rules to get valid lat/lng data, fetch the weather, and return a concise response

    ```python
    --8<-- "code/get-started/integrations/pydantic/weather-agent.py:30:74"
    ```

4. **Define the geocoding tool** - create a tool the agent calls behind the scenes to transform city names to lat/lng using the geocoding API. If the API key is missing or the location is invalid, it defaults to London or raises an error for self-correction

    ```python
    --8<-- "code/get-started/integrations/pydantic/weather-agent.py:76:102"
    ```

5. **Define the weather fetching tool** - create a tool that fetches weather from [Tomorrow.io](https://www.tomorrow.io/weather-api/){target=_blank} for a given lat/lng, converting temperatures to Celsius and Fahrenheit. Defaults to a mock response if the API key is missing

    ```python
    --8<-- "code/get-started/integrations/pydantic/weather-agent.py:104:160"
    ```

6. **Create a CLI chat** - prompt users for a location, send it to the weather agent, and print the final response

    ```python
    --8<-- "code/get-started/integrations/pydantic/weather-agent.py:162:194"
    ```

??? code "View full code file"
    ```python title="weather-agent.py"
    --8<-- "code/get-started/integrations/pydantic/weather-agent.py"
    ```

Use the following command to run your script:

```python
python weather-agent.py
```

--8<-- 'code/get-started/integrations/pydantic/terminal/weather-agent.md'

That's it! You've built a fully functional weather agent using PydanticAI and kluster.ai, showcasing how to integrate type-safe tools and LLMs for real-world data retrieval. Visit the [PydanticAI docs site](https://ai.pydantic.dev/){target=\_blank} to continue exploring PydanticAI's flexible tool and system prompt features to expand your agent's capabilities and handle more complex use cases with ease.