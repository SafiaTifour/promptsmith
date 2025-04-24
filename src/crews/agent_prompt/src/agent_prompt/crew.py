from crewai import LLM, Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai import LLM
from dotenv import load_dotenv
import os


load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
llm = LLM(
        model="openrouter/qwen/qwen-2.5-7b-instruct",
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key
	)
@CrewBase
class AgentPromptEnhancementCrew():
    """Crew responsible for enhancing user prompts for AI agents"""

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def prompt_analyzer(self) -> Agent:
        return Agent(
            config=self.agents_config['prompt_analyzer'],
            verbose=True,
			llm = llm
            
        )

    @agent
    def agent_psychology_expert(self) -> Agent:
        return Agent(
            config=self.agents_config['agent_psychology_expert'],
            verbose=True,
            llm = llm
        )

    @agent
    def framework_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['framework_specialist'],
            verbose=True,
            llm = llm
        )

    @agent
    def prompt_enhancer(self) -> Agent:
        return Agent(
            config=self.agents_config['prompt_enhancer'],
            verbose=True,
            llm = llm
        )

    # To learn more about structured task outputs, 
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def analyze_prompt_structure(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_prompt_structure'],
        )

    @task
    def analyze_agent_interpretation(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_agent_interpretation'],
        )

    @task
    def restructure_prompt(self) -> Task:
        return Task(
            config=self.tasks_config['restructure_prompt'],
        )

    @task
    def create_enhanced_prompt(self) -> Task:
        return Task(
            config=self.tasks_config['create_enhanced_prompt'],
            output_file='enhanced_prompt.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Prompt Enhancement crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )