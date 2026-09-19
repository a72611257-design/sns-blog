import os
from datetime import date
from html import escape

from openai import OpenAI


# 오늘 날짜
today = date.today().strftime("%Y-%m-%d")

# OpenAI 연결
client = OpenAI()

# 블로그 주제
topic = input("블로그 주제를 입력하세요: ")

# AI에게 블로그 글 작성 요청
response = client.responses.create(
    model="gpt-5.6-luna",
    input=f"""
당신은 한국어 블로그 전문 작가입니다.

다음 주제로 블로그 글을 작성해주세요.

주제: {topic}

조건:
- 자연스러운 한국어로 작성
- 제목을 먼저 작성
- 본문은 이해하기 쉽게 작성
- 초보자도 읽기 쉽게 작성
- 적당한 소제목을 포함
- 광고성 표현은 과하지 않게 작성
"""
)

# AI가 작성한 글
content = response.output_text.strip()

# 첫 번째 줄을 제목으로 사용
lines = content.splitlines()

if lines:
    title = lines[0].replace("#", "").strip()
else:
    title = topic

# Markdown용 블로그 글
blog_post = f"""# {title}

작성일: {today}

{content}
"""

# Markdown 파일 저장
with open("blog_post.md", "w", encoding="utf-8") as f:
    f.write(blog_post)

# HTML용 내용
html_content = escape(content).replace("\n", "<br>\n")
html_title = escape(title)

html_page = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html_title}</title>

<style>
body {{
    max-width: 800px;
    margin: 40px auto;
    padding: 20px;
    font-family: Arial, sans-serif;
    line-height: 1.8;
}}

h1 {{
    border-bottom: 2px solid #333;
    padding-bottom: 10px;
}}

.date {{
    color: #777;
    margin-bottom: 30px;
}}

.content {{
    font-size: 18px;
}}
</style>
</head>

<body>

<h1>{html_title}</h1>

<div class="date">
작성일: {today}
</div>

<h2>본문</h2>

<div class="content">
{html_content}
</div>

<hr>

<p>이 글은 Python과 OpenAI를 이용한 블로그 자동화 테스트입니다.</p>

</body>
</html>
"""

# HTML 파일 저장
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_page)

print("========================================")
print("블로그 글 생성 완료!")
print("제목:", title)
print("파일명: blog_post.md")
print("파일명: index.html")
print("========================================")