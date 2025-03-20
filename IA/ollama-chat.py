import requests 
from ollama import chat 
from ollama import ChatResponse

url = "https://localhost:11434/api/generate"

data = {
    'model': 'deepseek-r1:1.5b',
    'prompt': 'qui est le président de la france ?',
    'stream': False,
}


response = chat(model='deepseek-r1:1.5b', messages=[
    {   
        'role': 'user',
        'content': 'what is 5 + 5 ?'
    }
], stream=True
                )


for small in response:
    print(small['message']['content'], end='', flush=True)

# print(response['message']['content'])

# print(response.message.content)

# websocket django channels
# https://channels.readthedocs.io/en/stable/tutorial/part_1.html