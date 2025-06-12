import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("api_key")

system_prompt = "You are a helpful assistant that answers questions clearly and concisely."
user_prompt = input("Enter your prompt: ")

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt}
]

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
)

assistant_reply = response.choices[0].message["content"]
total_tokens = response["usage"]["total_tokens"]

print("\n🧠 Assistant's reply:\n")
print(assistant_reply)
print(f"\n🔢 Total tokens used: {total_tokens}")
