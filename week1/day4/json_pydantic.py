import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("Api Key Not Working")

client=Groq(api_key=my_api_key)
model = "openai/gpt-oss-120b"
role="user"

from pydantic import BaseModel

class Ticket(BaseModel):
    name: str
    email: str
    issue: str

schema = Ticket.model_json_schema()
response_formate={
    "type":"json_object",
}

system_prompt=f"""
Exact the personal information from ticket stictly based on this schema and give me in the json output   
{schema}.
"""
message_system={
    "role":"system",
    "content":system_prompt
}
text="Hello My name is Pratyush. I have an iphone which are not working at all.My address is abc@gmail.com. My contact number is 885544"

prompt= f"""
this is the customer ticket. please extract the personal information from this .
{text}
"""
message={
    "role":role,
    "content":prompt
    }

messages= [message_system, message]

response=client.chat.completions.create(
    model=model,
    messages=messages,
    response_format=response_formate
)

# print("**************************")
answer = response.choices[0].message.content
print(answer)


import json
raw_json =answer
data_file = json.loads(raw_json)
ticket = Ticket(**data_file)

print(ticket.email)
print(ticket.name)
print(ticket.issue)