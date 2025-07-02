"""
Configuration module for Discord Bot
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Discord settings
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
COMMAND_PREFIX = '!'

# OpenAI settings
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Music settings
YTDL_FORMAT_OPTIONS = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'
}

FFMPEG_OPTIONS = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': '-vn'
}

# Validation
if not DISCORD_TOKEN:
    raise ValueError("DISCORD_TOKEN is not set in environment variables")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set in environment variables") 