---
title: Integrate CrewAI with kluster.ai API
description: Learn how to integrate kluster.ai with CrewAI, a new framework for orchestrating autonomous AI agents, to launch and configure your AI agent chatbot.
---

# Integrate CrewAI with kluster.ai

[CrewAI](https://www.crewai.com/){target=\_blank} is a multi-agent platform that organizes specialized AI agents—each with defined roles, tools, and goals—within a structured process to tackle complex tasks efficiently. CrewAI agents streamline workflows and deliver reliable, scalable solutions by coordinating tasks and ensuring smooth collaboration.

This guide walks you through integrating [kluster.ai](https://www.kluster.ai/){target=\_blank} with CrewAI, from installation to creating and running a simple AI agent chatbot that leverages the kluster.ai API.

## Prerequisites

Before starting, ensure you have the following prerequisites:

- **A kluster.ai account** - sign up on the [kluster.ai platform](https://platform.kluster.ai/signup){target=\_blank} if you don't have one
- **A kluster.ai API key** - after signing in, go to the [**API Keys**](https://platform.kluster.ai/apikeys){target=\_blank} section and create a new key. For detailed instructions, check out the [Get an API key](/get-started/get-api-key/){target=\_blank} guide
- **CrewAI installed** - the [Installation Guide](https://docs.crewai.com/installation){target=\_blank} on the CrewAI website will walk you through installing CrewAI, setting up a virtual Python environment, and creating a new project. Note that CrewAI requires a Python version >=`3.10` and <`3.13`

## Create a project with the CrewAI CLI

Open your Python virtual environment, and then follow these steps to use the CrewAI CLI to create a new project:

1. **Create a project** - following the installation guide, create your first project with the following command:
```bash
crewai create crew INSERT_PROJECT_NAME
```
2. **Select model and provider** - during setup, the CLI will ask you to choose a provider and a model. Select `openai` as the provider and then choose any available model. Because you'll configure kluster.ai as a custom model, your initial model choice won't affect the final integration. The CLI will prompt you for an OpenAI API key, but this isn’t required. Simply press enter to skip

## Build a simple AI agent

After finishing the CLI setup, you will see a `src` directory with files `crew.py` and `main.py`. This guide won't use these sample files because they include extra features outside the scope. Follow these steps to continue:

1. **Create your first file** - Create a `hello_crew.py` file in `src/YOUR_PROJECT_NAME` to correspond to a simple AI agent chatbot

2. **Import modules and select model** - open `hello_crew.py` to add imports and define a custom LLM for kluster.ai by setting the following parameters:
    - **provider** - you can specify `openai_compatible`
    - **model** - choose one of kluster.ai's available models based on your use case:
    
        --8<-- 'text/real-time-models.md'

        Regardless of which model you choose, prepend its name with `openai/` to ensure CrewAI, which relies on LiteLLM, processes your requests correctly. 

    - **base_url** - use `https://api.kluster.ai/v1` to send requests to the kluster.ai endpoint
    - **api_key** - replace `INSERT_API_KEY` in the code below with your kluster.ai API key. If you don't have one yet, refer to the [Get an API key guide](/get-started/get-api-key/){target=\_blank}
  
    ```python title="hello_crew.py"
    --8<-- "code/get-started/integrations/crewai/hello_crew.py:0:23"
    ```

    This example overrides `agents_config` and `tasks_config` with empty dictionaries to tell CrewAI to ignore all YAML files and rely solely on your code, keeping this guide as streamlined as possible. 

3. **Define your agent** - set the agent's role, goal, and backstory, and assign the custom LLM (via the kluster.ai API) for generating creative greetings:

    ```python title="hello_crew.py"
    --8<-- "code/get-started/integrations/crewai/hello_crew.py:24:36"
    ```

4. **Give the agent a task** - define a task that prompts the agent for a unique, creative greeting using randomness to avoid repetition. Passing this prompt to `hello_agent()` ensures varied responses. CrewAI requires an `expected_output` field, defined here as a short greeting:

    ```python title="hello_crew.py"
    --8<-- "code/get-started/integrations/crewai/hello_crew.py:38:55"
    ```

5. **Tie it all together with a `@crew` method** - Add the following method to return the assembled Crew object with a single agent and task. This method enables CrewAI to coordinate the agent and task you defined:

    ```python title="hello_crew.py"
    --8<-- "code/get-started/integrations/crewai/hello_crew.py:57:67"
    ```

6. **Set up the entry point for the agent** - Create a new file named `hello_main.py`. In `hello_main.py`, import and initialize the `HelloWorldCrew` class, call its `hello_crew()` method, and then `kickoff()` to launch the task sequence:

    ```python title="hello_main.py"
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

??? code "View complete script"
    ```python title="hello_crew.py"
    --8<-- 'code/get-started/integrations/crewai/hello_crew.py'
    ```

## Run the agent

To run your agent, ensure you are in the same directory as your `hello_main.py` file, then use the following command:

```bash
python hello_main.py
```

Upon running the script, you'll see output that looks like the following:

--8<-- 'code/get-started/integrations/crewai/terminal/output.md'

And that's it! You've now successfully configured your AI agent harnessing CrewAI and the power of the kluster.ai API! 