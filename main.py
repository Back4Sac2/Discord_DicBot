"""
Discord Bot Main Entry Point
"""
import sys
import os

# Add src directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.bot import create_bot
from src.config import DISCORD_TOKEN
from src.commands.basic_commands import setup_basic_commands
from src.commands.ai_commands import setup_ai_commands
from src.commands.music_commands import setup_music_commands

def main():
    """Main function to start the Discord bot"""
    # Create bot instance
    bot = create_bot()
    
    # Setup all command modules
    setup_basic_commands(bot)
    setup_ai_commands(bot)
    setup_music_commands(bot)
    
    # Start the bot
    if not DISCORD_TOKEN:
        raise ValueError("DISCORD_TOKEN is not set in environment variables")
    bot.run(DISCORD_TOKEN)

if __name__ == "__main__":
    main() 