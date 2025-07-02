"""
Music service for YouTube playback and queue management
"""
import discord
import yt_dlp
import asyncio
import imageio_ffmpeg as ffmpeg
from collections import deque
from src.config import YTDL_FORMAT_OPTIONS, FFMPEG_OPTIONS

class MusicService:
    def __init__(self):
        self.music_queues = {}
        self.ytdl = yt_dlp.YoutubeDL(YTDL_FORMAT_OPTIONS)
    
    def get_queue(self, guild_id: int) -> deque:
        """Get or create music queue for a guild"""
        if guild_id not in self.music_queues:
            self.music_queues[guild_id] = deque()
        return self.music_queues[guild_id]
    
    async def search_and_play(self, ctx, search: str):
        """Search for music and play or add to queue"""
        if not ctx.voice_client:
            await ctx.send("먼저 음성 채널에 참가해주세요! (!join 명령어 사용)")
            return
        
        try:
            # Create audio source
            player = await YTDLSource.from_url(search, loop=ctx.bot.loop, stream=True)
            
            guild_id = ctx.guild.id
            queue = self.get_queue(guild_id)
            
            if ctx.voice_client.is_playing():
                # Add to queue if something is playing
                queue.append((player, ctx))
                await ctx.send(f'🎵 **대기열에 추가됨:** {player.title}\n📋 **대기열 위치:** {len(queue)}번째')
            else:
                # Play immediately if nothing is playing
                ctx.voice_client.play(player, after=lambda e: asyncio.run_coroutine_threadsafe(self.play_next(ctx), ctx.bot.loop) if e is None else print(f'Player error: {e}'))
                await ctx.send(f'🎵 **재생 중:** {player.title}')
                
        except Exception as e:
            await ctx.send(f'음악을 재생할 수 없습니다: {str(e)}')
    
    async def skip_song(self, ctx):
        """Skip current song and play next in queue"""
        if ctx.voice_client and ctx.voice_client.is_playing():
            ctx.voice_client.stop()
            await ctx.send("⏭️ 다음 곡으로 넘어갑니다!")
        else:
            await ctx.send("현재 재생 중인 음악이 없습니다.")
    
    async def show_queue(self, ctx):
        """Display current music queue"""
        guild_id = ctx.guild.id
        queue = self.get_queue(guild_id)
        
        if not queue:
            await ctx.send("🎵 대기열이 비어있습니다.")
            return
        
        queue_list = []
        for i, (player, _) in enumerate(queue, 1):
            queue_list.append(f"{i}. {player.title}")
            if i >= 10:  # Limit to 10 songs for display
                queue_list.append(f"... 그리고 {len(queue) - 10}곡 더")
                break
        
        queue_text = "\n".join(queue_list)
        await ctx.send(f"🎵 **현재 대기열:**\n```\n{queue_text}\n```")
    
    async def clear_queue(self, ctx):
        """Clear the music queue"""
        guild_id = ctx.guild.id
        queue = self.get_queue(guild_id)
        queue.clear()
        await ctx.send("🧹 대기열이 모두 지워졌습니다.")
    
    async def stop_music(self, ctx):
        """Stop music and clear queue"""
        guild_id = ctx.guild.id
        queue = self.get_queue(guild_id)
        queue.clear()
        
        if ctx.voice_client:
            if ctx.voice_client.is_playing():
                ctx.voice_client.stop()
            await ctx.send("⏹️ 음악이 정지되고 대기열이 지워졌습니다.")
        else:
            await ctx.send("현재 재생 중인 음악이 없습니다.")
    
    async def play_next(self, ctx):
        """Play next song in queue"""
        guild_id = ctx.guild.id
        queue = self.get_queue(guild_id)
        
        if queue and ctx.voice_client:
            try:
                player, original_ctx = queue.popleft()
                ctx.voice_client.play(player, after=lambda e: asyncio.run_coroutine_threadsafe(self.play_next(ctx), ctx.bot.loop) if e is None else print(f'Player error: {e}'))
                await ctx.send(f'🎵 **다음 곡 재생:** {player.title}')
            except Exception as e:
                await ctx.send(f'다음 곡 재생 중 오류 발생: {str(e)}')
                # Try to play the next song in queue
                if queue:
                    await self.play_next(ctx)


class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        ytdl = yt_dlp.YoutubeDL(YTDL_FORMAT_OPTIONS)
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        
        if data is None:
            raise ValueError("Could not extract video information")
            
        if 'entries' in data:
            data = data['entries'][0]
        
        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, executable=ffmpeg.get_ffmpeg_exe(), before_options=FFMPEG_OPTIONS['before_options'], options=FFMPEG_OPTIONS['options']), data=data) 