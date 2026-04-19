import requests

url = "http://localhost:11434/api/chat"
data = {
    "model": "Qwen2.5-Coder:1.5b",
    "stream": False,
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ]
}

res = requests.post(url, json=data)
res.raise_for_status()
print(res.json())