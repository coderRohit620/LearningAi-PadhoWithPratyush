import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("Api Error")

# Initialize Groq client
client = Groq(api_key = my_api_key)

# select model
model = "openai/gpt-oss-120b"
role = "user"
prompt ="Do you know Mahatma Ghandi?"

# define message
message = {
    "role":role,
    "content":prompt
}

messages = [message]

# Generate response
response = client.chat.completions.create(
    model=model,
    messages=messages
)

# Print output
# print(response)

print("#########################################")
print(response.choices[0].message.content)