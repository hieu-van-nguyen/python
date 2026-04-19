import ollama

model = "gemma4:31b-cloud"
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is the capital of France?"}
]

res = ollama.chat(model=model, messages=messages)
print(res["message"]["content"])