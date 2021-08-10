import discord
import random
from discord.ext import commands
import json
import os

BASE_PATH = os.getcwd() or "/Users/lachl/OneDrive/Desktop/StarscapeOCR/" # Get the Current Directory else use defined path

client = commands.Bot(command_prefix = ".")

core = "Aegis\nBastion\nConcord\nGuard\nHippa\nLiro\nLisin\nLycentia\nMetuar-xin\nPolma\nShield\nCitadel\nTriage\nUaspogar\nVanos\nVesox"
archived = "Aegis\nBastion\nCitadel\nConcord\nGuard\nShield\nTriage"

@client.event
async def on_ready():
    print("Bot online.")

@client.command(description="Returns bot latency.")
async def ping(ctx):
    await ctx.send(f'Latency of {round(client.latency * 1000)}ms')
    print(f'Latency of {round(client.latency * 1000)}ms')

@client.command(description="Get information about a specific star, planet, or moon.")
async def info(ctx,system,classification = "star",specific = "A"):
    if os.path.isfile(f"{system}/{classification}/{specific}.jpg") is True:  
        await ctx.send(file=discord.File(BASE_PATH + f"{system}/{classification}/{specific}.jpg"))
    else:
        await ctx.send("Unable to find requested file.")

@client.command(description="Allows you to query information about a system")
async def query(ctx,system):
    if os.path.isfile(BASE_PATH + f"{system}/Star/A.jpg") is True:
        list = os.listdir(BASE_PATH + f"{system}/Moon") 
        number_files_moon = len(list)
        list = os.listdir(BASE_PATH + f"{system}/Planet") 
        number_files_planet = len(list)
        list = os.listdir(BASE_PATH + f"{system}/Star") 
        number_files_star = len(list)
        await ctx.send(f"**{system.title()}:**\nStars: {number_files_star}\nPlanets: {number_files_planet}\nMoons: {number_files_moon}")
    else:
        await ctx.send("Unable to find requested file.")

@client.command(description="Get a list of a type of system, such as:\nCore\nlogged")
async def list(ctx, system_type):
    system_type = system_type.lower()
    if system_type == "core":
        await ctx.send(core)
    elif system_type in ["archived", "archive", "logged", 'log']
        await ctx.send(archived)
    else:
        await ctx.send("Could not find!")

@client.command()
async def devinfo(ctx):
    await ctx.send("We have logged the 7 main Core systems and plan to log more, to keep up to date on logged systems do ***.list logged***\nDo ***.help info*** to learn how to use the bot")

client.run('ODcyMzE0NjIwNjQyMTk3NTc1.YQoETA.tY3jIvldnbAUHFyfEp31OXc0lQI')

input('Press ENTER to exit')