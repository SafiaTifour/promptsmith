#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from crew import LongPromptCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew to create a long prompt.
    """
    inputs = {
        'prompt_task': """Create a prompt that helps users summarize long research papers effectively""",
        'prompt_requirements': """The generated prompt should guide the AI to extract key findings, 
        methodologies, and conclusions while maintaining academic accuracy. The summary should be 
        concise yet comprehensive, and include proper citations.""",
        'output_format': """The output should follow academic summary standards with clearly delineated 
        sections for introduction, methodology, results, and conclusion.""",
        'current_year': str(datetime.now().year)
    }
    
    try:
        LongPromptCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'prompt_task': """Create a prompt that helps users draft comprehensive business plans""",
        'prompt_requirements': """The generated prompt should guide the AI to include all essential 
        business plan components including executive summary, market analysis, operational plan, 
        financial projections, and marketing strategy.""",
        'output_format': """The output should be structured as a professional business document with 
        appropriate sections and subsections."""
    }
    try:
        LongPromptCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        LongPromptCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'prompt_task': """Create a prompt that helps users write detailed technical documentation""",
        'prompt_requirements': """The generated prompt should guide the AI to create technical 
        documentation that is clear, comprehensive, and accessible to the target audience while 
        maintaining technical accuracy.""",
        'output_format': """The output should follow standard technical documentation formats with 
        appropriate sections for overview, prerequisites, step-by-step instructions, and troubleshooting."""
    }
    try:
        LongPromptCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "train":
            train()
        elif sys.argv[1] == "replay":
            replay()
        elif sys.argv[1] == "test":
            test()
    else:
        run()