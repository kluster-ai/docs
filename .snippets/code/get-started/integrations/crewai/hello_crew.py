
import random

from crewai import LLM, Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task


@CrewBase
class HelloWorldCrew:
    # Override any default YAML references
    agents_config = {}
    tasks_config = {}

    def __init__(self):
        """
        When this crew is instantiated, create a custom LLM with your base_url.
        """
        self.custom_llm = LLM(
            provider="openai_compatible", 
            model="openai/klusterai/Meta-Llama-3.3-70B-Instruct-Turbo",
            base_url="https://api.kluster.ai/v1",
            api_key="INSERT_KLUSTER_API_KEY"
        )

    @agent
    def hello_agent(self) -> Agent:
        """
        A super simple agent with a single purpose: greet the user in a friendly, varied way.
        """
        return Agent(
            role="HelloWorldAgent",
            goal="Greet the user in a fun and creative way.",
            backstory="I'm a friendly agent who greets everyone in a slightly different manner!",
            llm=self.custom_llm,
            verbose=True
        )

    @task
    def hello_task(self) -> Task:
        """
        A task that asks the agent to produce a dynamic greeting.
        """
        random_factor = random.randint(100000, 999999)
        prompt = f"""
        You are a friendly greeting bot. 
        Please produce a short, creative greeting that changes each time. 
        Random factor: {random_factor}
        Example: "Hey there, how's your day going?"
        """

        return Task(
            description=prompt,
            expected_output="A short, creative greeting",
            agent=self.hello_agent()
        )

    @crew
    def hello_crew(self) -> Crew:
        """
        Our entire 'Hello World' crew—only 1 agent + 1 task in sequence.
        """
        return Crew(
            agents=self.agents,  
            tasks=self.tasks,    
            process=Process.sequential,
            verbose=True
        )
