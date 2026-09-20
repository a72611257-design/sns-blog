from datetime import date
import os
import sys

from openai import APIConnectionError, APIStatusError, AuthenticationError, OpenAI, RateLimitError

MODEL = os.getenv("OPENAI_MODEL", "gpt-5-mini").strip()

def fail(message):
    print("\n[오류] " + message)
    sys.exit(1)

api_key = os.getenv("OPENAI_API_KEY", "").strip()
if not api_key:
    fail('OPENAI_API_KEY가 없습니다. setx OPENAI_API_KEY "발급받은_키" 실행 후 명령 프롬프트를 다시 여세요.')

client = OpenAI(api_key=api_key, timeout=60.0, max_retries=2)

print("========================================")
print("AI 블로그 → 여러 글 저장")
print("사용 모델:", MODEL)
print("========================================")
print()

try:
    topic_response = client.responses.create(
        model=MODEL,
        input="""
오늘 작성할 한국어 블로그 주제를 하나 정해주세요.

조건:
- 한국 사람들이 관심을 가질 만한 주제
- 여행, 맛집, 생활정보, AI, IT, 건강 등에서 자유롭게 선택
- 블로그로 작성하기 좋은 주제
- 너무 전문적이지 않은 주제
- 제목만 한 줄로 출력
""",
    )
    topic = topic_response.output_text.strip()
    print("오늘의 AI 추천 주제:")
    print(topic)
    print()

    response = client.responses.create(
        model=MODEL,
        input=f"""
다음 주제로 한국어 블로그 글을 작성해주세요.

주제:
{topic}

조건:
- 읽기 쉬운 자연스러운 한국어
- 제목 포함
- 소제목 사용
- 유용한 정보 제공
- 과장된 표현 사용하지 않기
- 마크다운 형식
""",
    )
    content = response.output_text.strip()
except AuthenticationError:
    fail("OpenAI API 키가 올바르지 않습니다.")
except RateLimitError:
    fail("OpenAI API 사용 한도 또는 결제 한도에 걸렸습니다.")
except APIConnectionError:
    fail("OpenAI 서버에 연결하지 못했습니다. 인터넷·방화벽·VPN을 확인하세요.")
except APIStatusError as exc:
    if exc.status_code == 404:
        fail(f"모델 '{MODEL}'을 사용할 수 없습니다. OPENAI_MODEL 설정을 확인하세요.")
    fail(f"OpenAI API 오류입니다. 상태 코드: {exc.status_code}")
except Exception as exc:
    fail(f"예상하지 못한 오류: {type(exc).__name__}: {exc}")

# 3. 날짜
today = date.today().isoformat()

# 4. post.txt에 저장
with open("post.txt", "w", encoding="utf-8-sig") as f:
    f.write("제목: " + topic + "\n\n")
    f.write("본문:\n")
    f.write(content)

print("========================================")
print("AI 블로그 글 생성 완료!")
print("post.txt에 저장했습니다.")
print("날짜:", today)
print("========================================")
