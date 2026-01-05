import json
import ollama
from pathlib import Path

MODEL_NAME = "phi3:mini"
PROMPT_PATH = Path("prompts/intent_extraction.txt")

def call_llm(user_query: str) -> str:
    """Calls Phi-3 via Ollama and returns RAW text output."""
    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": PROMPT_PATH.read_text(encoding="utf-8")
            },
            {
                "role": "user",
                "content": user_query
            }
        ]
    )
    return response["message"]["content"]

def extract_json(text: str) -> dict:
    """
    Robustly extracts the first valid JSON object using brace counting.
    Ignores any text (instructions/hallucinations) that appears after the JSON.
    """
    try:
        text = text.strip()
        start_index = text.find('{')
        
        # If no JSON start is found, assume the query was off-topic/unanswerable
        if start_index == -1:
            return {"intent": "unknown", "metrics": []}

        # Brace Counting Logic
        balance = 0
        end_index = -1
        
        for i in range(start_index, len(text)):
            char = text[i]
            if char == '{':
                balance += 1
            elif char == '}':
                balance -= 1
            
            # When balance returns to 0, we have the complete object
            if balance == 0:
                end_index = i + 1
                break

        if end_index == -1:
            # Found a start but no end? Return unknown rather than crashing
            return {"intent": "unknown", "metrics": []}

        clean_json_str = text[start_index:end_index]
        return json.loads(clean_json_str)

    except (json.JSONDecodeError, ValueError):
        # Fallback for any parsing error -> treat as unknown
        return {"intent": "unknown", "metrics": []}

def extract_intent(user_query: str) -> dict:
    """
    MAIN ENTRY POINT.
    """
    if not isinstance(user_query, str):
        raise TypeError(f"extract_intent expects str, got {type(user_query)}")

    llm_output = call_llm(user_query)
    
    # Debug: Print this to console to see what the LLM actually said
    print(f"--- LLM RAW OUTPUT ---\n{llm_output}\n------------------------")
    
    intent_data = extract_json(llm_output)
    
    # Ensure 'metrics' is always a list (fixes LLM returning strings)
    if "metrics" in intent_data and isinstance(intent_data["metrics"], str):
        intent_data["metrics"] = [intent_data["metrics"]]
        
    return intent_data