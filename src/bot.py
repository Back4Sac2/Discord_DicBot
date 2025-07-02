"""
Main Discord Bot setup
"""
import discord
from discord.ext import commands
from src.config import COMMAND_PREFIX

def create_bot():
    """Create and configure the Discord bot"""
    intents = discord.Intents.default()
    intents.message_content = True
    intents.voice_states = True
    
    bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=intents)
    
    @bot.event
    async def on_ready():
        print(f'{bot.user} has connected to Discord!')
    
    return bot 