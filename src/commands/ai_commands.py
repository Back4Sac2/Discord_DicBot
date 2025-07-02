"""
AI-powered Discord bot commands using OpenAI
"""
from discord.ext import commands
from src.services.openai_service import OpenAIService

def setup_ai_commands(bot):
    """Setup AI-powered commands for the bot"""
    ai_service = OpenAIService()
    
    @bot.command(name='ask')
    async def ask(ctx, *, question):
        """OpenAI를 사용한 질문 답변"""
        answer = await ai_service.ask_question(question)
        await ctx.send(answer)
    
    @bot.command(name='joke')
    async def joke(ctx):
        """재미있는 농담을 해줍니다."""
        joke_text = await ai_service.get_joke()
        await ctx.send(f"😄 {joke_text}")
    
    @bot.command(name='translate')
    async def translate(ctx, target_lang, *, text):
        """텍스트를 번역합니다. 사용법: !translate 영어 안녕하세요"""
        translation = await ai_service.translate_text(target_lang, text)
        await ctx.send(f"🌍 **번역 결과 ({target_lang}):** {translation}")
    
    @bot.command(name='story')
    async def story(ctx, *, topic):
        """주어진 주제로 짧은 이야기를 만들어줍니다."""
        story_text = await ai_service.create_story(topic)
        await ctx.send(f"📚 **{topic} 이야기:**\n{story_text}")
    
    @bot.command(name='explain')
    async def explain(ctx, *, concept):
        """복잡한 개념을 쉽게 설명해줍니다."""
        explanation = await ai_service.explain_concept(concept)
        await ctx.send(f"🧠 **{concept} 설명:**\n{explanation}")
    
    @bot.command(name='code')
    async def code(ctx, language, *, problem):
        """간단한 코딩 문제를 해결해줍니다."""
        code_solution = await ai_service.generate_code(language, problem)
        await ctx.send(f"💻 **{language} 코드:**\n```{language}\n{code_solution}\n```")
    
    @bot.command(name='usage')
    async def check_usage(ctx):
        """OpenAI API 사용량을 확인합니다."""
        usage_info = await ai_service.check_usage()
        await ctx.send(usage_info) 