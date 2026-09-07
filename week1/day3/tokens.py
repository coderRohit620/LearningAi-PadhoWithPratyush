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
# we use 3 prompt
prompt1= "Hii!"
prompt2= "Explain time travel in detail under 100 words"
prompt3= "Write a 1000 word essay on machine learning"

prompts=[prompt1,prompt2,prompt3]
for prompt in prompts:
    message={
        "role":role,
        "content":prompt
    }
    messages= [message]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=6000
    )
    usage = response.usage
    print(
        f"Prompt: {prompt} --> "
        f"your tokens: {usage.prompt_tokens} "
        f"completion tokens: {usage.completion_tokens} "
        f"total tokens: {usage.total_tokens} "
        f"Finish Reason: {response.choices[0].finish_reason}"
    )

# message_system={
#     "role":"system",
#     # "content":"You are my loving girlfriend"
#     # "content":"You are my strict office colleague who is also my manager"
#     "content":"You are my brand manager who suggests name for my company.name should be in one word. suggest only one name with its proper meaning"
    
# }

# message me role content


# print(response)
# print("*****")
# print(response.choices[0].message.content)