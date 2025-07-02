"""
Music and voice-related Discord bot commands
"""
from discord.ext import commands
from src.services.music_service import MusicService

def setup_music_commands(bot):
    """Setup music and voice commands for the bot"""
    music_service = MusicService()
    
    @bot.command(name='join')
    async def join(ctx):
        """봇이 음성 채널에 참가합니다."""
        if ctx.author.voice:
            channel = ctx.author.voice.channel
            await channel.connect()
            await ctx.send(f'🔊 {channel} 음성 채널에 참가했습니다!')
        else:
            await ctx.send('먼저 음성 채널에 참가해주세요!')
    
    @bot.command(name='leave')
    async def leave(ctx):
        """봇이 음성 채널에서 나갑니다."""
        if ctx.voice_client:
            await ctx.voice_client.disconnect()
            await ctx.send('👋 음성 채널에서 나갔습니다!')
        else:
            await ctx.send('봇이 음성 채널에 연결되어 있지 않습니다.')
    
    @bot.command(name='song')
    async def song(ctx, *, search):
        """유튜브에서 음악을 검색하고 재생합니다."""
        await music_service.search_and_play(ctx, search)
    
    @bot.command(name='skip')
    async def skip(ctx):
        """현재 곡을 건너뛰고 다음 곡을 재생합니다."""
        await music_service.skip_song(ctx)
    
    @bot.command(name='playlist')
    async def show_queue(ctx):
        """현재 음악 대기열을 보여줍니다."""
        await music_service.show_queue(ctx)
    
    @bot.command(name='clear')
    async def clear_queue(ctx):
        """음악 대기열을 모두 지웁니다."""
        await music_service.clear_queue(ctx)
    
    @bot.command(name='stop')
    async def stop(ctx):
        """음악 재생을 중지하고 대기열을 지웁니다."""
        await music_service.stop_music(ctx) 