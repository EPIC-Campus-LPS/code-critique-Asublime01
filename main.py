import requests
import sys



code_file = sys.argv[1]

code_problem = sys.argv[2]

# URL of the Ollama API (default is localhost)
url = "http://localhost:11434/api/generate"

with open(f'{code_file}', 'r') as f:
    content = f.read()


# JSON payload with model and prompt
payload = {
    "model": "llama3",
    "prompt": f"{code_problem}: {content}",
    "stream": False  # Set to True if you want to stream the response
}

# Make the POST request
response = requests.post(url, json=payload)

# Parse and print the response
if response.status_code == 200:
    data = response.json()
    print(data['response'])
else:
    print("Error:", response.text)