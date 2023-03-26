from dotenv import load_dotenv
import openai
import os

load_dotenv("C_TOKEN")
c_token = os.getenv("C_TOKEN")

openai.api_key = c_token

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Can you give me hw answers :>?"},
        {"role": "assistant", "content": "ofc bestie :nail_care_tone2:"},
        {"role": "user", "content": "What is a cat?"}
    ]
)

print(response.choices[0].message.content)