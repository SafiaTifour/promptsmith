#!/usr/bin/env python
import sys
import warnings
import re

from datetime import datetime

from crew import ShortPromptCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def validate_prompt(prompt_text):
    """
    Validate that the prompt doesn't contain placeholder syntax
    """
    placeholder_pattern = r'\{Insert \$[A-Z_0-9]+\$\}'
    meta_instructions = ["enhance performance", "progressive enhancement", "first address Section"]
    
    if re.search(placeholder_pattern, prompt_text):
        print("WARNING: Prompt contains placeholder syntax. Rerunning with additional instructions.")
        return False
        
    for phrase in meta_instructions:
        if phrase.lower() in prompt_text.lower():
            print("WARNING: Prompt contains meta-instructions. Rerunning with additional instructions.")
            return False
            
    return True

def run():
    """
    Run the crew to create a short prompt.
    """
    inputs = {
        'prompt_task': """Extract person's full name from text""",
        'prompt_requirements': """The prompt should extract only the full name of a person from text. 
        If no name is found, it should return an empty string. No additional text, summaries, or 
        explanations should be included in the output.""",
        'output_format': """Just the full name as a string, or an empty string if no name is found.""",
        'additional_instructions': """IMPORTANT: Create a concrete, final prompt without placeholders 
        or template syntax. Do not use {Insert $VARIABLE$} format. Use only simple variables like 
        {input_text}. Do not include meta-instructions about how to enhance the prompt.""",
        'current_year': str(datetime.now().year)
    }
    
    try:
        result = ShortPromptCrew().crew().kickoff(inputs=inputs)
        
            
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'prompt_task': """Convert dates to ISO format""",
        'prompt_requirements': """The prompt should convert various date formats to ISO 8601 format 
        (YYYY-MM-DD). If the input is not recognizable as a date, return an empty string.""",
        'output_format': """Just the ISO formatted date as a string, or an empty string if the input 
        is not a valid date.""",
        'additional_instructions': """Create a concrete, final prompt without placeholders."""
    }
    try:
        ShortPromptCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        ShortPromptCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'prompt_task': """Extract email addresses from text""",
        'prompt_requirements': """The prompt should extract all valid email addresses from input text. 
        Each email should be on a new line. If no valid emails are found, return an empty string.""",
        'output_format': """Only the email addresses, one per line, or an empty string if none found.""",
        'additional_instructions': """Create a concrete, final prompt without placeholders."""
    }
    try:
        ShortPromptCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

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