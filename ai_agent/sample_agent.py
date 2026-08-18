import os
import json
import wikipedia
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key="YOUR_API_KEY")

# ----------- TOOLS ------------

def calculator(expression):
    """Safely evaluate math expressions"""
    try:
        return str(eval(expression))
    except Exception:
        return "Invalid math expression"

def wiki_search(query):
    """Search Wikipedia"""
    try:
        return wikipedia.summary(query, sentences=2)
    except Exception:
        return "No results found."

# ----------- TOOL REGISTRY ------------

TOOLS = {
    "calculator": calculator,
    "wiki_search": wiki_search,
}

# ----------- AGENT LOOP ------------

def ai_agent(user_input):
    system_prompt = """
You are an AI agent.
You can use tools if needed.

Available tools:
1. calculator(expression)
2. wiki_search(query)

If a tool is needed, respond in JSON:
{
    "tool": "tool_name",
    "input": "tool_input"
}

If no tool is needed, respond normally.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    )

    reply = response.choices[0].message.content

    # Try parsing tool call
    try:
        tool_call = json.loads(reply)
        tool_name = tool_call["tool"]
        tool_input = tool_call["input"]

        if tool_name in TOOLS:
            tool_result = TOOLS[tool_name](tool_input)

            # Send result back to model for final response
            second_response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_input},
                    {"role": "assistant", "content": reply},
                    {"role": "assistant", "content": f"Tool result: {tool_result}"}
                ]
            )

            return second_response.choices[0].message.content

    except:
        # No tool call
        return reply


# ----------- RUN ------------

if __name__ == "__main__":
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        result = ai_agent(user_input)
        print("Agent:", result)
