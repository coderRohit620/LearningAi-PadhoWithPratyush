import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("Api Key Not Working")

client=Groq(api_key=my_api_key)
model = "openai/gpt-oss-20b"
role="user"
prompt= "Suggest a name for my clothing company."

message_system={
    "role":"system",
    # "content":"You are my loving girlfriend"
    # "content":"You are my strict office colleague who is also my manager"
    "content":"You are my brand manager who suggests name for my company.name should be in one word. suggest only one name with its proper meaning"
    
}
message={
    "role":role,
    "content":prompt
}
# message me role content
messages= [message_system , message]
response=client.chat.completions.create(
    model=model,
    messages=messages,
    # Temperature by default is 0 meaning safe. alwase take range [0, 2]
    temperature=2
    )
# print(response)
print("*****")
print(response.choices[0].message.content)