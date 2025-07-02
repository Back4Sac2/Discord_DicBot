"""
Basic Discord bot commands
"""
from discord.ext import commands

def setup_basic_commands(bot):
    """Setup basic commands for the bot"""
    
    @bot.command(name='hello')
    async def hello(ctx):
        """간단한 인사 명령어"""
        await ctx.send(f'안녕하세요, {ctx.author.name}님!')
    
    @bot.command(name='commands')
    async def help_commands(ctx):
        """사용 가능한 명령어 목록을 출력합니다."""
        command_list = """
**🤖 사용 가능한 명령어:**
• `!hello` - 봇이 인사합니다
• `!ask [질문]` - AI에게 질문합니다
• `!joke` - 재미있는 농담을 해줍니다
• `!translate [언어] [텍스트]` - 텍스트를 번역합니다
• `!story [주제]` - 짧은 이야기를 만들어줍니다
• `!explain [개념]` - 복잡한 개념을 쉽게 설명해줍니다
• `!code [언어] [문제]` - 간단한 코드를 작성해줍니다
• `!usage` - OpenAI API 사용량을 확인합니다
• `!join` - 봇이 음성 채널에 참가합니다
• `!leave` - 봇이 음성 채널에서 나갑니다
• `!song [노래명]` - 유튜브에서 노래를 재생하거나 대기열에 추가합니다
• `!skip` - 현재 곡을 건너뛰고 다음 곡을 재생합니다
• `!playlist` - 현재 대기열을 확인합니다
• `!clear` - 대기열을 모두 지웁니다
• `!stop` - 음악 재생을 중지합니다
• `!commands` - 이 명령어 목록을 보여줍니다
        """
        await ctx.send(command_list) 