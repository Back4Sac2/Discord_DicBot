# 🤖 East Incheon GPT Discord Bot

한국어 AI 기능과 음악 재생, 대화 내역 관리가 가능한 다기능 Discord 봇입니다.

## ✨ 주요 기능

### 🧠 AI 기능 (OpenAI GPT)
- **질문 답변**: 자연스러운 한국어로 모든 질문에 답변
- **농담 생성**: 재미있는 한국어 농담 생성
- **번역**: 다양한 언어 간 번역 서비스
- **이야기 창작**: 주제를 바탕으로 한 창의적인 단편 소설
- **개념 설명**: 복잡한 개념을 쉽고 이해하기 쉽게 설명
- **코딩 도움**: 다양한 프로그래밍 언어로 코드 작성 지원
- **사용량 확인**: OpenAI API 연결 상태 및 사용량 모니터링

### 🎵 음악 기능
- **음성 채널 관리**: 봇의 음성 채널 입장/퇴장
- **YouTube 음악 재생**: 유튜브에서 음악 검색 및 재생
- **재생 대기열**: 스마트한 음악 대기열 관리
- **재생 제어**: 건너뛰기, 중지, 대기열 확인 등

### 📊 대화 내역 관리 (NEW!)
- **개인 대화 내역**: 최근 AI 대화 기록 조회
- **사용 통계**: 개인별 명령어 사용량 및 토큰 소모량 확인
- **키워드 검색**: 대화 내역에서 특정 키워드로 검색
- **서버 통계**: 서버 내 사용자 순위 및 활동 현황
- **데이터 관리**: 개인 대화 내역 삭제 기능
- **전체 통계**: 봇의 전반적인 사용 현황 확인

## 🚀 설치 및 실행

### 1. 레포지토리 클론
```bash
git clone <repository-url>
cd discord_dicBot
```

### 2. 가상환경 설정 (권장)
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. 패키지 설치
```bash
pip install -r requirements.txt
```

### 4. 환경 변수 설정
`.env` 파일을 프로젝트 루트에 생성하고 다음 내용을 추가하세요:
```env
DISCORD_TOKEN=your_discord_bot_token_here
OPENAI_API_KEY=your_openai_api_key_here
```

### 5. 봇 실행
```bash
python main.py
```

## 📋 명령어 목록

### 📋 기본 명령어
- `!hello` - 봇이 인사합니다
- `!commands` - 사용 가능한 모든 명령어 목록 표시

### 🧠 AI 명령어 (토큰 사용)
- `!ask [질문]` - AI에게 질문하기
- `!joke` - 재미있는 농담 들려주기
- `!translate [언어] [텍스트]` - 텍스트 번역
- `!story [주제]` - 짧은 이야기 창작
- `!explain [개념]` - 복잡한 개념을 쉽게 설명
- `!code [언어] [문제]` - 프로그래밍 코드 작성
- `!usage` - OpenAI API 사용량 확인

### 🎵 음악 명령어 (무료)
- `!join` - 봇이 음성 채널에 참가
- `!leave` - 봇이 음성 채널에서 나가기
- `!song [노래명]` - YouTube에서 노래 재생/대기열 추가
- `!skip` - 현재 곡 건너뛰기
- `!playlist` - 현재 재생 대기열 확인
- `!clear` - 재생 대기열 모두 지우기
- `!stop` - 음악 재생 중지

### 📊 대화 내역 명령어 (NEW!)
- `!history [개수]` - 최근 대화 내역 보기 (기본 5개, 최대 20개)
- `!mystats` - 개인 사용 통계 확인
- `!search [키워드]` - 대화 내역에서 키워드 검색
- `!serverstats` - 서버 사용 통계 및 순위 보기
- `!clearhistory` - 개인 대화 내역 완전 삭제
- `!dbstats` - 전체 봇 사용 통계 확인

## 📁 프로젝트 구조

```
discord_dicBot/
├── main.py                 # 봇 실행 진입점
├── requirements.txt        # Python 패키지 의존성
├── README.md              # 프로젝트 문서
├── .env                   # 환경 변수 (직접 생성 필요)
├── conversation_history.db # SQLite 데이터베이스 (자동 생성)
└── src/
    ├── bot.py             # 봇 인스턴스 생성
    ├── config.py          # 설정 및 환경 변수 관리
    ├── commands/
    │   ├── basic_commands.py    # 기본 명령어
    │   ├── ai_commands.py       # AI 기능 명령어
    │   ├── music_commands.py    # 음악 기능 명령어
    │   └── history_commands.py  # 대화 내역 관리 명령어
    └── services/
        ├── openai_service.py    # OpenAI API 연동
        ├── music_service.py     # 음악 재생 서비스
        └── database_service.py  # 대화 내역 데이터베이스 관리
```

## 💰 토큰 사용량

### 🆓 무료 기능
- 모든 음악 관련 명령어
- 기본 명령어 (`!hello`, `!commands`)
- 대화 내역 관리 명령어

### 💳 토큰 사용 기능
- AI 관련 명령어 (`!ask`, `!joke`, `!translate`, `!story`, `!explain`, `!code`)
- `!usage` 명령어 (소량의 테스트 토큰 사용)

## 🛠️ 기술 스택

- **Python 3.8+** - 메인 프로그래밍 언어
- **discord.py** - Discord API 라이브러리
- **OpenAI API** - GPT 모델 연동
- **yt-dlp** - YouTube 음원 다운로드
- **FFmpeg** - 오디오 처리
- **SQLite** - 대화 내역 로컬 데이터베이스
- **python-dotenv** - 환경 변수 관리

## 🌟 특별 기능

### 🎯 스마트한 톤 매칭
- 사용자의 말투(존댓말/반말)를 자동 감지하여 적절한 톤으로 응답
- 자연스러운 한국어 대화 경험 제공

### 🎵 지능적인 음악 대기열
- YouTube에서 자동 음악 검색
- 재생 대기열 스마트 관리
- 음성 채널 자동 연결

### 📊 포괄적인 데이터 추적
- 모든 AI 대화 자동 기록
- 사용자별 통계 및 토큰 사용량 추적
- 서버별 활동 현황 모니터링
- 키워드 기반 대화 검색 기능

### 💬 Discord 최적화
- 메시지 길이 제한 자동 처리 (2000자 제한)
- 긴 응답 자동 분할 및 요약
- 사용자 친화적인 에러 메시지

## 🔧 추가 설정

### FFmpeg 설치 (음악 기능용)
- **Windows**: [FFmpeg 공식 사이트](https://ffmpeg.org/download.html)에서 다운로드
- **macOS**: `brew install ffmpeg`
- **Linux**: `sudo apt install ffmpeg`

### OpenAI API 키 발급
1. [OpenAI 플랫폼](https://platform.openai.com/)에 가입
2. API 키 생성
3. `.env` 파일에 추가

### Discord Bot 토큰 발급
1. [Discord Developer Portal](https://discord.com/developers/applications)에서 애플리케이션 생성
2. Bot 탭에서 토큰 생성
3. 필요한 권한 설정 (메시지 읽기/쓰기, 음성 채널 연결 등)

## 🤝 기여하기

1. 이 레포지토리를 포크하세요
2. 새로운 기능 브랜치를 만드세요 (`git checkout -b feature/amazing-feature`)
3. 변경사항을 커밋하세요 (`git commit -m 'Add amazing feature'`)
4. 브랜치에 푸시하세요 (`git push origin feature/amazing-feature`)
5. Pull Request를 열어주세요

## 📄 라이선스

이 프로젝트는 MIT 라이선스 하에 있습니다. 자세한 내용은 `LICENSE` 파일을 참조하세요.

## 🆘 지원

문제가 발생하거나 질문이 있으시면 [Issues](https://github.com/your-username/discord_dicBot/issues)에서 문의해 주세요.

---

⭐ 이 프로젝트가 도움이 되었다면 별표를 눌러주세요! 