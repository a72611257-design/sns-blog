import os
from datetime import date
from html import escape
from openai import OpenAI

client = OpenAI()

print("========================================")
print("    AI 블로그 자동 생성 시작")
print("========================================")
print()

# AI가 오늘의 블로그 주제를 자동으로 선정
topic_response = client.responses.create(
    model="gpt-5.6-luna",
    input="""
오늘 작성할 블로그 주제를 하나 선정해주세요.

조건:
- 한국 사람들이 관심을 가질 만한 주제
- 블로그로 작성하기 좋은 주제
- 너무 전문적이지 않은 주제
- 여행, 맛집, 생활정보, AI, IT, 건강한 생활습관 등에서 자유롭게 선정
- 제목만 한 줄로 출력
- 설명은 출력하지 마세요.
"""
)

topic = topic_response.output_text.strip()

print("오늘의 AI 추천 주제:")
print(topic)
print()

# 선택된 주제로 블로그 글 생성
response = client.responses.create(
    model="gpt-5.6-luna",
    input=f"""
다음 주제로 한국어 블로그 글을 작성해주세요.

주제:
{topic}

작성 조건:
- 읽기 쉬운 한국어
- 블로그에 바로 사용할 수 있는 자연스러운 글
- 제목 포함
- 소제목을 적절히 사용
- 유용한 정보를 충분히 제공
- 과장된 표현은 피하기
- 마크다운 형식으로 작성
"""
)

content = response.output_text.strip()

# 제목 가져오기
lines = content.splitlines()
title = topic

for line in lines:
    clean = line.strip().lstrip("#").strip()
    if clean:
        title = clean
        break

# Markdown 파일 저장
with open("blog_post.md", "w", encoding="utf-8") as f:
    f.write(content)

# HTML 생성
today = date.today().isoformat()

html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{escape(title)}</title>
</head>
<body>
<article>
<h1>{escape(title)}</h1>
<p>작성일: {today}</p>
<hr>
<pre style="white-space: pre-wrap; font-family: sans-serif;">{escape(content)}</pre>
</article>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("========================================")
print("블로그 글 생성 완료!")
print("주제:", topic)
print("제목:", title)
print("파일명: blog_post.md")
print("파일명: index.html")
print("========================================")