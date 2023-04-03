import discord
from dotenv import load_dotenv
import os
from math import * 
from discord.ext import commands

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

bot.run(token)
