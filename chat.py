from dotenv import load_dotenv
import openai
import os

load_dotenv("C_TOKEN")
c_token = os.getenv("C_TOKEN")

openai.api_key = c_token

messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Can you give me hw answers :>?"},
        {"role": "assistant", "content": "ofc bestie :nail_care_tone2:"},
    ]

def chat(inp):
  messages.append({"role": "user", "content": inp})
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages,
  )
  messages.append(response.choices[0].message)
  return response.choices[0].message.content

print(chat("What is a cat?"))
print(chat("What is Ivy?"))