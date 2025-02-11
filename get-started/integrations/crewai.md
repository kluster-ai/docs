---
title: Using CrewAI with the kluster.ai API
description: Learn how to integrate kluster.ai with CrewAI, a new framework for orchestrating autonomous AI agents, to launch and configure your AI agent chatbot.
---

# Using CrewAI with the kluster.ai API

[CrewAI](https://www.crewai.com/){target=\_blank} is a multi-agent platform that organizes specialized AI agents—each with defined roles, tools, and goals—within a structured process to tackle complex tasks efficiently. CrewAI agents streamline workflows and deliver reliable, scalable solutions by coordinating tasks and ensuring smooth collaboration. This guide walks you through integrating [kluster.ai](https://www.kluster.ai/){target=\_blank} with CrewAI, from installation to creating and running a simple AI agent chatbot that leverages the kluster.ai API.

## Prerequisites

Before starting, ensure you have the following prerequisites:

- **A kluster.ai account** - sign up on the [kluster.ai platform](https://platform.kluster.ai/signup){target=\_blank} if you don't have one
- **A kluster.ai API key** - after signing in, go to the [**API Keys**](https://platform.kluster.ai/apikeys){target=\_blank} section and create a new key. For detailed instructions, check out the [Get an API key](/get-started/get-api-key/){target=\_blank} guide

## Installation and CLI

Next, you can follow the [Installation Guide](https://docs.crewai.com/installation){target=\_blank} on the CrewAI website. This guide will walk you through installing CrewAI, setting up a virtual Python environment, and creating a new project. The installation guide will prompt you to create your first project with the following command:

```bash
crewai create crew INSERT_PROJECT_NAME
```

During setup, the CLI will ask you to choose a provider and a model. Select `openai` as the provider and then choose any available model. Because you'll configure kluster.ai as a custom model, your initial model choice won't affect the final integration.

## Build a simple AI Agent

After you finish the CLI setup, a sample folder will appear with `crew.py` and `main.py`. This guide won't use these sample files because they include extra features outside this guide's scope. Instead, you'll create new files corresponding to a simple AI agent chatbot. Create a `hello_crew.py` and a `hello_main.py` file. 

Turning our attention to the `hello_crew` file, you'll first handle our imports and define a custom LLM, the most essential part of the kluster.ai integration. Here are the four parameters you'll need to define to complete the kluster.ai integration:

  1. **provider** - you can specify `openai_compatible`
  2. **model** - choose one of kluster.ai's available models based on your use case. Regardless of which model you choose, prepend its name with `openai/`. This ensures CrewAI, which relies on LiteLLM, processes your requests correctly. For more details, see [kluster.ai's models](/api-reference/reference/#list-supported-models){target=\_blank}
  3. **base_url** - use `https://api.kluster.ai/v1` to send requests to the kluster.ai endpoint
  4. **api_key** - replace `INSERT_API_KEY` in the code below with your kluster.ai API key. If you don't have one yet, refer to the [Get an API key guide](/get-started/get-api-key/){target=\_blank}
  
```python
--8<-- "code/get-started/integrations/crewai/hello_crew.py:0:23"
```

As you can see above, you'll also override `agents_config` and `tasks_config` with empty dictionaries to tell CrewAI to ignore all YAML files and rely solely on your code to make this example guide as streamlined as possible. 

Next, you'll define our agent. This code sets the agent's role, goal, and backstory, then assigns the custom LLM (using kluster.ai API) described earlier for generating creative greetings.


```python
--8<-- "code/get-started/integrations/crewai/hello_crew.py:24:36"
```

Next, you need to give the agent a task to do. This task prompts the agent for a unique, creative greeting each time, incorporating a random factor to prevent repeated responses. Passing this prompt to `hello_agent()`, ensures the final output is varied and fun. Note that CrewAI requires the task to have an `expected_output` field, which you have defined here as a short greeting.  

```python
--8<-- "code/get-started/integrations/crewai/hello_crew.py:38:55"
```

Lastly, let's put together the `hello_main.py` file. This file serves as the entry point for running the Hello World agent. It imports the `HelloWorldCrew` class, then calls `kickoff()` on the `hello_crew` to launch the task sequence with no extra inputs. 

```python
#!/usr/bin/env python
from hello_crew import HelloWorldCrew


def run():
    """
    Kick off the HelloWorld crew with no inputs.
    """
    HelloWorldCrew().hello_crew().kickoff(inputs={})

if __name__ == "__main__":
    run()

```

??? code "Complete Script"
    ```python
    --8<-- 'code/get-started/integrations/crewai/hello_crew.py'
    ```

To run your agent, use the following command:

```bash
python hello_main.py
```

Upon running the script, you'll see output that looks like the following:

--8<-- 'code/get-started/integrations/crewai/terminal/output.md'

And that's it! You've now successfully configured your AI agent harnessing CrewAI and the power of the kluster.ai API! 