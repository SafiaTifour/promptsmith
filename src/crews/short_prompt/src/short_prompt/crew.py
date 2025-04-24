from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from dotenv import load_dotenv
import os
from crewai import LLM

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
llm = LLM(
        model="openrouter/qwen/qwen-2.5-7b-instruct",
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key
	)
@CrewBase
class ShortPromptCrew():
    """Crew responsible for creating effective, token-efficient short prompts"""

    # Configuration files
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # Agent definitions
    @agent
    def objective_instruction_designer(self) -> Agent:
        return Agent(
            config=self.agents_config['objective_instruction_designer'],
            verbose=True,
            llm=llm
        )

    @agent
    def example_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['example_specialist'],
            verbose=True,
            llm=llm
        )

    @agent
    def variable_expert(self) -> Agent:
        return Agent(
            config=self.agents_config['variable_expert'],
            verbose=True,
            llm=llm
        )

    @agent
    def short_prompt_synthesizer(self) -> Agent:
        return Agent(
            config=self.agents_config['short_prompt_synthesizer'],
            verbose=True,
            llm=llm
        )

    # Task definitions
    @task
    def create_objectives_instructions(self) -> Task:
        return Task(
            config=self.tasks_config['create_objectives_instructions'],
        )

    @task
    def develop_examples(self) -> Task:
        return Task(
            config=self.tasks_config['develop_examples'],
        )

    @task
    def identify_variables(self) -> Task:
        return Task(
            config=self.tasks_config['identify_variables'],
        )

    @task
    def synthesize_short_prompt(self) -> Task:
        return Task(
            config=self.tasks_config['synthesize_short_prompt'],
            output_file='short_prompt.md'
        )

    # Crew definition
    @crew
    def crew(self) -> Crew:
        """Creates the Short Prompt Creation crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )