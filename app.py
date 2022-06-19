from code import interact
from dotenv import load_dotenv
import os 
import nextcord
from nextcord.ext import commands
import dalle

load_dotenv()

bot = commands.Bot()

test_guild_id = None

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    await bot.change_presence(activity=nextcord.Game(name="with your perception of art!"))

@bot.slash_command(description="I'm trying to test here", guild_ids=[test_guild_id])
async def hello(interaction: nextcord.Interaction):
    await interaction.send("Hello!")

@bot.slash_command(description="Asynchronously generates 4 Dall-E images from a given prompt (very alpha)",
                   guild_ids=[test_guild_id])
async def generate(interaction: nextcord.Interaction, arg: str):
    await interaction.send("Generating some art for '{}', please wait...".format(arg))
    try:
        await dalle.asyncDiscordEntry(4, arg)
        await interaction.send(file=nextcord.File('result.jpg'))
    except:
        await interaction.send("I wasn't able to do that, I might be a bit too busy! Try again in a few seconds!")
    
bot.run(os.getenv('DISCORD_TOKEN'))
