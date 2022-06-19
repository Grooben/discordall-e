from code import interact
from dotenv import load_dotenv
import os 
import nextcord
from nextcord.ext import commands
import dalle
from print.BrotherQL import BrotherQLPrinter

load_dotenv()

bot = commands.Bot()

@bot.slash_command(description="Asynchronously generates 4 Dall-E images from a given prompt (very alpha)")
async def generate(interaction: nextcord.Interaction, arg: str):
    await interaction.send("Generating some art for '{}', please wait...".format(arg))
    try:
        await dalle.asyncDiscordEntry(4, arg)
        await interaction.send(file=nextcord.File('result.jpg'))
    except:
        await interaction.send("I wasn't able to do that, I might be a bit too busy! Try again in a few seconds!")
        
@bot.slash_command(description="Asynchronously generates 4 Dall-E images from a given prompt (very alpha)")
async def print(interaction: nextcord.Interaction, arg: str):
    await interaction.send("Generating some art for '{}', please wait...".format(arg))
    try:
        await dalle.asyncDiscordEntry(4, arg)
        await interaction.send(file=nextcord.File('result.jpg'))
    except:
        await interaction.send("I wasn't able to do that, I might be a bit too busy! Try again in a few seconds!")
    
bot.run(os.getenv('DISCORD_TOKEN'))
