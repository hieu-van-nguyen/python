from google import genai
from google.genai import types

# 1. Initialize the client with your API key
API_KEY = "YOUR_API_KEY"
client = genai.Client(api_key=API_KEY)

# 2. Define the Agent's system instructions
system_instructions = (
    "You are a helpful AI Research Agent. "
    "When asked a complex math or data question, use the code_execution tool "
    "to verify your answers. Always explain your reasoning."
)

# 3. Create the agentic request
MODEL_ID = "gemini-3-flash-preview"
# Updated configuration for the tool
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    config=types.GenerateContentConfig(
        system_instruction=system_instructions,
        tools=[{'code_execution': {}}], 
        temperature=1.0,
    ),
    contents="Calculate the sum of 1 and 2."
)

# 4. Output the result
print(f"Agent Response:\n{response.text}")

# If the agent used a tool, you can see the code it ran:
for part in response.candidates[0].content.parts:
    if part.executable_code:
        print(f"\n--- Code Run by Agent ---\n{part.executable_code.code}")