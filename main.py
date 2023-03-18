import os
import discord
import random
from discord.ext import commands
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
#bot = discord.bot(intents = intents)
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if "bruh" in message.content.lower():
        await message.channel.send("My brother in Christ")

    await bot.process_commands(message)
    
@bot.command(name="8ball")
async def _8ball(ctx):
    responses = ["yes", "no", "piss off"]
    response = random.choice(responses)
    embed = discord.Embed(title="Dude's decision", description=f'answer: {response}')
    await ctx.send(embed=embed)

bot.run(TOKEN)

