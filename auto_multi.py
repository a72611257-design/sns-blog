from datetime import datetime
from html import escape
import os
import re

# ==============================
# 1. post.txt 읽기
# ==============================

text = open(
    "post.txt",
    "r",
    encoding="utf-8-sig"
).read()

lines = text.splitlines()

title = next(
    (
        x.replace("제목:", "", 1).strip()
        for x in lines
        if x.startswith("제목:")
    ),
    ""
)

content = "\n".join(
    x
    for x in lines
    if not x.startswith("제목:")
    and not x.startswith("본문:")
).strip()

today = datetime.now().strftime("%Y-%m-%d")

if not title:
    title = "SNS 자동화 글 - " + today


# ==============================
# 2. posts 폴더 만들기
# ==============================

os.makedirs("posts", exist_ok=True)

# ==============================
# 3. 파일명 만들기
# 같은 날짜 + 같은 제목이면 기존 글 업데이트
# ==============================

safe = "".join(
    x for x in title
    if x.isalnum() or x in " -_"
).strip()

if not safe:
    safe = "blog-post"

name = today + "-" + safe

filename = os.path.join(
    "posts",
    name + ".html"
)



# ==============================
# 4. 개별 글 HTML 만들기
# ==============================

page = """<!DOCTYPE html>
<html lang="ko">

<head>

<meta charset="UTF-8">

<meta name="viewport"
content="width=device-width, initial-scale=1.0">

<title>""" + escape(title) + """</title>

<style>

body {
    margin: 0;
    background: #f5f7fa;
    font-family: Arial, sans-serif;
    color: #333;
}

.container {
    max-width: 800px;
    margin: 50px auto;
    background: white;
    padding: 40px;
    border-radius: 15px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.08);
}

h1 {
    font-size: 34px;
    margin-bottom: 10px;
}

.date {
    color: #888;
    margin-bottom: 35px;
}

.content {
    font-size: 18px;
    line-height: 2;
}

.back {
    display: inline-block;
    margin-top: 35px;
    text-decoration: none;
    color: #333;
}

</style>

</head>

<body>

<div class="container">

<h1>""" + escape(title) + """</h1>

<div class="date">
작성일: """ + today + """
</div>

<div class="content">
""" + escape(content).replace("\n", "<br>") + """
</div>

<a class="back" href="../index.html">
← 블로그 목록으로 돌아가기
</a>

</div>

</body>

</html>"""


open(
    filename,
    "w",
    encoding="utf-8"
).write(page)


# ==============================
# 5. 전체 글 목록
# ==============================

files = [
    x
    for x in os.listdir("posts")
    if x.endswith(".html")
]

files.sort(reverse=True)

# ==============================
# 6. 블로그 목록 만들기
# ==============================

links = ""

for x in files:
    filepath = os.path.join("posts", x)

    # 실제 HTML 파일에서 제목 가져오기
    with open(filepath, "r", encoding="utf-8") as f:
        html_text = f.read()

    title_match = re.search(
        r"<title>(.*?)</title>",
        html_text,
        re.DOTALL
    )

    if title_match:
        post_title = title_match.group(1).strip()
    else:
        post_title = x[:-5]

    # 날짜
    post_date = x[:10]

    links += """
<div class="post">

<div class="date">
""" + post_date + """
</div>

<h2>
<a href="posts/""" + escape(x) + """">
""" + escape(post_title) + """
</a>
</h2>

</div>
"""
# ==============================
# 7. 메인 블로그 페이지
# ==============================

index = """<!DOCTYPE html>

<html lang="ko">

<head>

<meta charset="UTF-8">

<meta name="viewport"
content="width=device-width, initial-scale=1.0">

<title>나의 자동화 블로그</title>

<style>

body {
    margin: 0;
    background: #f5f7fa;
    font-family: Arial, sans-serif;
    color: #333;
}

.container {
    max-width: 850px;
    margin: 50px auto;
    padding: 20px;
}

.header {
    background: white;
    padding: 40px;
    border-radius: 15px;
    margin-bottom: 25px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.08);
}

.header h1 {
    margin: 0 0 10px 0;
    font-size: 38px;
}

.header p {
    color: #777;
    font-size: 17px;
}

.post {
    background: white;
    padding: 25px 30px;
    margin-bottom: 18px;
    border-radius: 12px;
    box-shadow: 0 3px 15px rgba(0,0,0,0.06);
}

.post .date {
    color: #999;
    font-size: 14px;
}

.post h2 {
    margin: 8px 0 0 0;
}

.post a {
    color: #333;
    text-decoration: none;
}

.post a:hover {
    text-decoration: underline;
}

.footer {
    text-align: center;
    color: #999;
    margin-top: 40px;
}

</style>

</head>

<body>

<div class="container">

<div class="header">

<h1>
나의 자동화 블로그
</h1>

<p>
Python + GitHub로 자동 발행되는 블로그입니다.
</p>

</div>

""" + links + """

<div class="footer">

Python 자동화 시스템

</div>

</div>

</body>

</html>"""


open(
    "index.html",
    "w",
    encoding="utf-8"
).write(index)


# ==============================
# 8. 완료 메시지
# ==============================

print("========================================")
print("8강 블로그 디자인 생성 완료!")
print("제목:", title)
print("저장 파일:", filename)
print("현재 글 개수:", len(files))
print("========================================")