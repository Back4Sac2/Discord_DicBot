"""
Conversation history related Discord bot commands
"""
from discord.ext import commands
from src.services.database_service import DatabaseService
import datetime

def setup_history_commands(bot):
    """Setup conversation history commands for the bot"""
    db = DatabaseService()
    
    @bot.command(name='history')
    async def show_history(ctx, limit: int = 5):
        """최근 대화 내역을 보여줍니다."""
        if limit > 20:
            limit = 20  # 최대 20개로 제한
        
        history = db.get_user_history(str(ctx.author.id), limit)
        
        if not history:
            await ctx.send("💬 대화 내역이 없습니다.")
            return
        
        history_text = f"📚 **{ctx.author.name}님의 최근 대화 내역 (최대 {limit}개)**\n\n"
        
        for i, (command, user_input, bot_response, timestamp, tokens) in enumerate(history, 1):
            # 타임스탬프 포맷
            dt = datetime.datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
            time_str = dt.strftime('%m/%d %H:%M')
            
            # 텍스트 길이 제한
            short_input = user_input[:50] + "..." if len(user_input) > 50 else user_input
            short_response = bot_response[:100] + "..." if len(bot_response) > 100 else bot_response
            
            history_text += f"**{i}. !{command}** ({time_str})\n"
            history_text += f"   👤 {short_input}\n"
            history_text += f"   🤖 {short_response}\n\n"
        
        # Discord 메시지 길이 제한 확인
        if len(history_text) > 1900:
            history_text = history_text[:1900] + "... (내역이 길어서 잘렸습니다)"
        
        await ctx.send(history_text)
    
    @bot.command(name='mystats')
    async def show_my_stats(ctx):
        """내 사용 통계를 보여줍니다."""
        stats = db.get_user_stats(str(ctx.author.id))
        
        if not stats:
            await ctx.send("📊 사용 통계가 없습니다.")
            return
        
        username, total_commands, total_tokens, last_activity = stats
        
        # 마지막 활동 시간 포맷
        dt = datetime.datetime.fromisoformat(last_activity.replace('Z', '+00:00'))
        last_time = dt.strftime('%Y년 %m월 %d일 %H:%M')
        
        stats_text = f"""
📊 **{username}님의 사용 통계**

🔢 **총 명령어 사용**: {total_commands}회
🪙 **총 토큰 사용**: {total_tokens}개
⏰ **마지막 활동**: {last_time}

💡 **참고**: 음악 명령어는 토큰을 사용하지 않습니다!
        """
        
        await ctx.send(stats_text)
    
    @bot.command(name='search')
    async def search_history(ctx, *, keyword):
        """대화 내역에서 키워드를 검색합니다."""
        results = db.search_conversations(str(ctx.author.id), keyword, 5)
        
        if not results:
            await ctx.send(f"🔍 '{keyword}' 관련 대화를 찾을 수 없습니다.")
            return
        
        search_text = f"🔍 **'{keyword}' 검색 결과**\n\n"
        
        for i, (command, user_input, bot_response, timestamp) in enumerate(results, 1):
            dt = datetime.datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
            time_str = dt.strftime('%m/%d %H:%M')
            
            # 키워드 하이라이트 (Discord는 실제 하이라이트가 안되므로 **로 강조)
            highlighted_input = user_input.replace(keyword, f"**{keyword}**")
            highlighted_response = bot_response.replace(keyword, f"**{keyword}**")
            
            search_text += f"**{i}. !{command}** ({time_str})\n"
            search_text += f"   👤 {highlighted_input[:100]}{'...' if len(highlighted_input) > 100 else ''}\n"
            search_text += f"   🤖 {highlighted_response[:150]}{'...' if len(highlighted_response) > 150 else ''}\n\n"
        
        if len(search_text) > 1900:
            search_text = search_text[:1900] + "... (결과가 길어서 잘렸습니다)"
        
        await ctx.send(search_text)
    
    @bot.command(name='serverstats')
    async def show_server_stats(ctx):
        """서버의 봇 사용 통계를 보여줍니다."""
        if not ctx.guild:
            await ctx.send("DM에서는 서버 통계를 볼 수 없습니다.")
            return
        
        stats = db.get_server_stats(str(ctx.guild.id))
        
        if not stats:
            await ctx.send("📊 서버 사용 통계가 없습니다.")
            return
        
        stats_text = f"📊 **{ctx.guild.name} 서버 통계**\n\n"
        stats_text += "👑 **상위 사용자들:**\n"
        
        for i, (username, command_count, total_tokens) in enumerate(stats, 1):
            medal = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else f"{i}."
            tokens_display = total_tokens if total_tokens else 0
            stats_text += f"{medal} **{username}**: {command_count}회 (토큰: {tokens_display}개)\n"
        
        await ctx.send(stats_text)
    
    @bot.command(name='clearhistory')
    async def clear_my_history(ctx):
        """내 대화 내역을 모두 삭제합니다."""
        try:
            db.clear_user_history(str(ctx.author.id))
            await ctx.send("🗑️ 대화 내역이 모두 삭제되었습니다.")
        except Exception as e:
            await ctx.send(f"❌ 내역 삭제 중 오류가 발생했습니다: {str(e)}")
    
    @bot.command(name='dbstats')
    async def show_db_stats(ctx):
        """전체 데이터베이스 통계를 보여줍니다."""
        try:
            stats = db.get_database_stats()
            
            stats_text = f"""
📈 **전체 봇 사용 통계**

💬 **총 대화**: {stats['total_conversations']:,}회
👥 **총 사용자**: {stats['total_users']:,}명
🪙 **총 토큰 사용**: {stats['total_tokens']:,}개

🔥 **인기 명령어 TOP 5:**
"""
            
            for i, (command, count) in enumerate(stats['popular_commands'], 1):
                stats_text += f"{i}. !{command}: {count:,}회\n"
            
            await ctx.send(stats_text)
        except Exception as e:
            await ctx.send(f"❌ 통계 조회 중 오류가 발생했습니다: {str(e)}") 