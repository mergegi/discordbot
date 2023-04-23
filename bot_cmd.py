import discord
from dotenv import load_dotenv
import os
from math import * 
from discord.ext import commands
import openai
import time 

load_dotenv("C_TOKEN")
c_token = os.getenv("C_TOKEN")

openai.api_key = c_token

messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Can you give me hw answers :>?"},
        {"role": "assistant", "content": "ofc bestie :nail_care_tone2:"},
    ]

# Goal: Reset the conversation after 5 minutes 

chat_timestamp = time.time() #time of last chat message

def resetConversationIfExpired(): 
    global chat_timestamp
    global messages
    cur_time = time.time()
    if cur_time - chat_timestamp > 300: #reset history message
        messages = messages[:3] 
        print("Resetting conversation history")
    chat_timestamp = cur_time

def chat(inp):
  messages.append({"role": "user", "content": inp})
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages,
  )
  messages.append(response.choices[0].message)
  return response.choices[0].message.content

#create intents
intents = discord.Intents.default()
intents.message_content = True

# read bot token from env file
load_dotenv("TOKEN")
token = os.environ.get("TOKEN")

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.command(help="says hihi :D")
async def hoi(ctx):
    await ctx.send("hihi :D")

@bot.command(help="slay")
async def hehe(ctx):
    await ctx.send("literally slay :nail_care_tone2:")

@bot.command(help="echoes the message you send")
async def echo(ctx, *, arg):
    await ctx.send(":P -" + arg)

@bot.command(help="solves meeth")
async def meeth(ctx, *, arg):
    await ctx.send("meeth - " + str(eval(arg)))

@bot.command(help="chatgpt")
async def ai(ctx, *, arg):
    await ctx.send(chat(arg))

bot.run(token)
