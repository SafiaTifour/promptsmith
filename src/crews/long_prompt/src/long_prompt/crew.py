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
class LongPromptCrew():
    """Crew responsible for creating effective long-form prompts following a comprehensive framework"""

    # Configuration files
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # Agent definitions
    @agent
    def role_persona_designer(self) -> Agent:
        return Agent(
            config=self.agents_config['role_persona_designer'],
            verbose=True,
            llm=llm
        )

    @agent
    def objective_designer(self) -> Agent:
        return Agent(
            config=self.agents_config['objective_designer'],
            verbose=True,
            llm=llm
        )

    @agent
    def context_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['context_specialist'],
            verbose=True,
            llm=llm
        )

    @agent
    def instruction_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['instruction_engineer'],
            verbose=True,
            llm=llm
        )

    @agent
    def example_architect(self) -> Agent:
        return Agent(
            config=self.agents_config['example_architect'],
            verbose=True,
            llm=llm
            
        )

    @agent
    def prompt_synthesizer(self) -> Agent:
        return Agent(
            config=self.agents_config['prompt_synthesizer'],
            verbose=True,
            llm=llm
            
        )

    # Task definitions
    @task
    def create_role_persona(self) -> Task:
        return Task(
            config=self.tasks_config['create_role_persona'],
        )

    @task
    def design_objective(self) -> Task:
        return Task(
            config=self.tasks_config['design_objective'],
        )

    @task
    def develop_context(self) -> Task:
        return Task(
            config=self.tasks_config['develop_context'],
        )

    @task
    def craft_instructions(self) -> Task:
        return Task(
            config=self.tasks_config['craft_instructions'],
        )

    @task
    def design_examples(self) -> Task:
        return Task(
            config=self.tasks_config['design_examples'],
        )

    @task
    def synthesize_long_prompt(self) -> Task:
        return Task(
            config=self.tasks_config['synthesize_long_prompt'],
            output_file='long_prompt.md'
        )

    # Crew definition
    @crew
    def crew(self) -> Crew:
        """Creates the Long Prompt Creation crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )