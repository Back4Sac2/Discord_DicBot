# 🤖 East Incheon GPT Discord Bot

한국어 AI 기능과 음악 재생이 가능한 다기능 Discord 봇입니다.

## ✨ 주요 기능

### 🧠 AI 기능 (OpenAI GPT-3.5-turbo)
- **질문 답변**: 사용자의 말투(존댓말/반말)에 맞춰 답변
- **농담**: 재미있는 한국어 농담 생성
- **번역**: 다양한 언어로 텍스트 번역
- **스토리**: 주제 기반 짧은 이야기 생성
- **설명**: 복잡한 개념을 쉽게 설명
- **코딩**: 프로그래밍 문제 해결 코드 생성

### 🎵 음악 기능 (YouTube)
- **음성 채널 관리**: 봇이 음성 채널 참가/퇴장
- **음악 재생**: YouTube에서 음악 검색 및 재생
- **대기열 시스템**: 플레이리스트처럼 곡 대기열 관리
- **재생 제어**: 곡 건너뛰기, 정지, 대기열 확인

## 🚀 설치 및 실행

### 1. 저장소 클론
```bash
git clone https://github.com/your-username/discord_dicBot.git
cd discord_dicBot
```

### 2. 가상환경 설정
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### 3. 패키지 설치
```bash
pip install -r requirements.txt
```

### 4. 환경 변수 설정
`.env` 파일을 생성하고 다음 내용을 추가하세요:
```env
DISCORD_TOKEN=your_discord_bot_token
OPENAI_API_KEY=your_openai_api_key
```

### 5. 봇 실행
```bash
python main_new.py
```

## 📋 명령어 목록

### 기본 명령어
- `!hello` - 봇이 인사합니다
- `!commands` - 사용 가능한 명령어 목록 표시

### 🤖 AI 명령어 (토큰 사용)
- `!ask [질문]` - AI에게 질문 (말투 자동 매칭)
- `!joke` - 재미있는 농담
- `!translate [언어] [텍스트]` - 텍스트 번역
- `!story [주제]` - 짧은 이야기 생성
- `!explain [개념]` - 복잡한 개념 설명
- `!code [언어] [문제]` - 코딩 문제 해결
- `!usage` - OpenAI API 사용량 확인

### 🎵 음악 명령어 (무료)
- `!join` - 봇이 음성 채널에 참가
- `!leave` - 봇이 음성 채널에서 퇴장
- `!song [노래명]` - 음악 재생 또는 대기열에 추가
- `!skip` - 다음 곡으로 건너뛰기
- `!playlist` - 현재 대기열 확인
- `!clear` - 대기열 비우기
- `!stop` - 음악 정지 및 대기열 비우기

## 🏗️ 프로젝트 구조

```
discord_dicBot/
├── src/                          # 소스 코드 패키지
│   ├── __init__.py
│   ├── config.py                 # 설정 및 환경변수
│   ├── bot.py                    # 봇 인스턴스 생성
│   ├── services/                 # 서비스 레이어
│   │   ├── __init__.py
│   │   ├── openai_service.py     # OpenAI API 서비스
│   │   └── music_service.py      # 음악 재생 서비스
│   └── commands/                 # 명령어 모듈
│       ├── __init__.py
│       ├── basic_commands.py     # 기본 명령어
│       ├── ai_commands.py        # AI 명령어
│       └── music_commands.py     # 음악 명령어
├── main_new.py                   # 메인 진입점 (새 버전)
├── main.py                       # 기존 모놀리식 버전
├── requirements.txt              # 패키지 의존성
├── .env                         # 환경 변수 (비공개)
├── .gitignore                   # Git 무시 파일
└── README.md                    # 프로젝트 문서
```

## 💰 토큰 사용량

### 무료 기능
- 모든 음악 관련 명령어 (`!song`, `!skip`, `!playlist` 등)
- 기본 명령어 (`!hello`, `!commands`)

### 토큰 사용 기능
- AI 관련 명령어 (`!ask`, `!joke`, `!translate`, `!story`, `!explain`, `!code`)
- 사용량은 OpenAI 웹사이트에서 확인: https://platform.openai.com/usage

## 🔧 기술 스택

- **Python 3.8+**
- **discord.py** - Discord API 라이브러리
- **OpenAI API** - GPT-3.5-turbo 모델
- **yt-dlp** - YouTube 다운로드/스트리밍
- **FFmpeg** - 오디오 처리 (자동 설치)

## 🚦 특징

### 🎯 말투 매칭
봇이 사용자의 말투를 분석해서 동일한 톤으로 답변합니다:
- **존댓말 질문** → **존댓말 답변**
- **반말 질문** → **반말 답변**

### 🎶 스마트 음악 대기열
- 서버별 독립적인 대기열 관리
- 자동 다음 곡 재생
- 에러 발생시 자동으로 다음 곡 시도

### 📱 Discord 메시지 최적화
- 2000자 길이 제한 자동 처리
- 긴 응답 자동 잘라내기
- 사용자 친화적 에러 메시지

## 🤝 기여하기

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 `LICENSE` 파일을 확인하세요.

## 🙋‍♂️ 지원

문제가 발생하거나 질문이 있으시면 이슈를 생성해 주세요!

---

**⭐ 이 프로젝트가 도움이 되었다면 별표를 눌러주세요!** 