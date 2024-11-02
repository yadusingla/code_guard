import os
import openai
import logging
from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT

def generate_prompt(filename, code_changes):
    return f"Please review the following code changes in {filename} and suggest improvements, identify potential issues, and recommend optimizations:\n\n{code_changes}"

def review_code_with_ai(file_changes):
    client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    suggestions = {}

    for filename, patch in file_changes.items():
        prompt = generate_prompt(filename, patch)
        
        # Prepare the full prompt for Claude
        full_prompt = f"{HUMAN_PROMPT} You are a helpful assistant for reviewing code.\n\n{prompt}{AI_PROMPT}"
        
        response = client.completions.create(
            model="claude-2",  # Use "claude-2" or other available model name
            prompt=full_prompt,
            max_tokens_to_sample=150
        )
        
        # Extract the response content
        suggestions[filename] = response.completion.strip()
        
        # Print suggestions for debugging
        print(f"Suggestions for {filename}:\n{suggestions[filename]}")
        print("-" * 50)

    return suggestions