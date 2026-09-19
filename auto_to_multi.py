from datetime import date
from openai import OpenAI

client = OpenAI()

print("========================================")
print("AI 블로그 → 여러 글 저장 테스트")
print("========================================")
print()

# 1. AI가 오늘의 주제를 선택
topic_response = client.responses.create(
    model="gpt-5.6-luna",
    input="""
오늘 작성할 한국어 블로그 주제를 하나 정해주세요.

조건:
- 한국 사람들이 관심을 가질 만한 주제
- 여행, 맛집, 생활정보, AI, IT, 건강 등에서 자유롭게 선택
- 블로그로 작성하기 좋은 주제
- 너무 전문적이지 않은 주제
- 제목만 한 줄로 출력
"""
)

topic = topic_response.output_text.strip()

print("오늘의 AI 추천 주제:")
print(topic)
print()

# 2. AI가 블로그 글 작성
response = client.responses.create(
    model="gpt-5.6-luna",
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
"""
)

content = response.output_text.strip()

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