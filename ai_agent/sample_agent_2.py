from google import genai
from google.genai import types

# 1. Configuration
API_KEY = "YOUR_API_KEY"
client = genai.Client(api_key=API_KEY)
MODEL_ID = "gemini-3-flash-preview" # High-speed, agentic model

# 2. Define a Tool (The function the agent can use)
def add_numbers(a: float, b: float) -> float:
    """Adds two numbers together."""
    return a + b

# 3. Initialize the Agent with Tools
# We pass the function itself into the 'tools' list
system_instructions = (
    "You are a helpful AI Research Agent. "
    "When asked a complex math or data question, use the code_execution tool "
    "to verify your answers. Always explain your reasoning."
)

config = types.GenerateContentConfig(
    tools=[add_numbers],
    temperature=1.0,
    system_instruction=system_instructions
)

def run_agent():
    print("--- Gemini Agent Active (Type 'quit' to exit) ---")
    chat = client.chats.create(model=MODEL_ID, config=config)
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            break
            
        response = chat.send_message(user_input)
        
        # The SDK automatically calls 'add_numbers' if needed 
        # and sends the result back to Gemini before giving you the final text.
        print(f"Agent: {response.text}")

if __name__ == "__main__":
    run_agent()