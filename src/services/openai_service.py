"""
OpenAI API service for AI-powered features
"""
from openai import OpenAI
from src.config import OPENAI_API_KEY

class OpenAIService:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
    
    async def ask_question(self, question: str) -> str:
        """Ask a question to GPT and get response matching user's tone"""
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant. Answer in Korean matching the user's tone - if they use formal speech (존댓말), respond formally; if they use informal speech (반말), respond informally. Keep your response under 500 characters to fit Discord message limits."},
                    {"role": "user", "content": question}
                ],
                max_tokens=200
            )
            answer = response.choices[0].message.content
            
            # Check Discord message length limit
            if answer and len(answer) > 1900:
                answer = answer[:1900] + "... (답변이 길어서 잘렸습니다)"
                
            return answer or "응답을 받지 못했습니다."
        except Exception as e:
            return f'오류가 발생했습니다: {str(e)}'
    
    async def get_joke(self) -> str:
        """Get a funny joke"""
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a funny comedian. Tell short, clean jokes in Korean. Use a friendly, casual tone. Keep it under 300 characters."},
                    {"role": "user", "content": "재미있는 농담 하나 해줘"}
                ],
                max_tokens=100
            )
            return response.choices[0].message.content or "농담을 준비하지 못했어요."
        except Exception as e:
            return f'농담을 준비하지 못했어요... 오류: {str(e)}'
    
    async def translate_text(self, target_lang: str, text: str) -> str:
        """Translate text to target language"""
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": f"Translate the following text to {target_lang}. Only provide the translation without additional explanation. Keep it concise."},
                    {"role": "user", "content": text}
                ],
                max_tokens=150
            )
            return response.choices[0].message.content or "번역을 생성하지 못했습니다."
        except Exception as e:
            return f'번역에 실패했어요: {str(e)}'
    
    async def create_story(self, topic: str) -> str:
        """Create a short story based on topic"""
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Write a short, engaging story in Korean (maximum 3 short paragraphs, under 800 characters) based on the given topic. Use a natural, storytelling tone."},
                    {"role": "user", "content": f"{topic}에 대한 짧은 이야기를 써줘"}
                ],
                max_tokens=300
            )
            story_text = response.choices[0].message.content
            
            if story_text and len(story_text) > 1900:
                story_text = story_text[:1900] + "... (이야기가 길어서 잘렸습니다)"
                
            return story_text or '이야기를 생성하지 못했습니다.'
        except Exception as e:
            return f'이야기를 만들지 못했어요: {str(e)}'
    
    async def explain_concept(self, concept: str) -> str:
        """Explain a complex concept in simple terms"""
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Explain complex concepts in simple, easy-to-understand Korean language. Use analogies and examples. Match the user's tone (formal/informal). Keep explanation under 600 characters for Discord limits."},
                    {"role": "user", "content": f"{concept}을 쉽게 설명해줘"}
                ],
                max_tokens=250
            )
            explanation = response.choices[0].message.content
            
            if explanation and len(explanation) > 1900:
                explanation = explanation[:1900] + "... (설명이 길어서 잘렸습니다)"
                
            return explanation or '설명을 생성하지 못했습니다.'
        except Exception as e:
            return f'설명을 준비하지 못했어요: {str(e)}'
    
    async def generate_code(self, language: str, problem: str) -> str:
        """Generate code solution for a given problem"""
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": f"Write clean, simple {language} code to solve the given problem. Provide brief comments in Korean using a natural tone. Keep code concise and under 1500 characters for Discord limits."},
                    {"role": "user", "content": f"{language}로 {problem}을 해결하는 코드를 써줘"}
                ],
                max_tokens=400
            )
            code_solution = response.choices[0].message.content
            
            if code_solution and len(code_solution) > 1500:
                code_solution = code_solution[:1500] + "\n# ... (코드가 길어서 잘렸습니다)"
                
            return code_solution or '# 코드를 생성하지 못했습니다.'
        except Exception as e:
            return f'코드를 작성하지 못했어요: {str(e)}'
    
    async def check_usage(self) -> str:
        """Check OpenAI API status and usage"""
        try:
            # Simple test request to check API status
            test_response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": "Hi"}],
                max_tokens=1
            )
            
            return """
🔍 **OpenAI API 상태 확인**

✅ **API 연결**: 정상 작동
🤖 **모델**: gpt-3.5-turbo
💰 **현재 요청**: 성공

📊 **사용량 정보**:
• 이 테스트 요청으로 약 1-2 토큰 사용됨
• 더 자세한 사용량은 OpenAI 웹사이트에서 확인하세요
• 링크: https://platform.openai.com/usage

💡 **팁**: 
• `!ask`, `!joke`, `!translate` 등만 토큰을 사용해요
• 음악 기능들(`!song`, `!skip` 등)은 완전 무료입니다!
            """
            
        except Exception as e:
            return f"""
❌ **OpenAI API 오류**

🔧 **문제**: {str(e)}

💡 **가능한 원인**:
• API 키가 잘못되었거나 만료됨
• 사용량 한도 초과
• OpenAI 서버 문제

🌐 **확인 방법**:
OpenAI 웹사이트에서 직접 확인하세요:
https://platform.openai.com/usage
            """ 