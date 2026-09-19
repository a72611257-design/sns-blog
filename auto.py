이 글은 Python을 이용한 SNS 자동화 테스트입니다.
"""

with open("blog_post.md", "w", encoding="utf-8") as f:
f.write(blog_post)

html_content = escape(content).replace("\n", "<br>\n")
html_title = escape(title)

html_page = f"""<!DOCTYPE html>

<html lang="ko"> <head> <meta charset="UTF-8"> <meta name="viewport" content="width=device-width, initial-scale=1.0"> <title>{html_title}</title> <style> body {{ max-width: 800px; margin: 40px auto; padding: 20px; font-family: Arial, sans-serif; line-height: 1.8; }} h1 {{ border-bottom: 2px solid #333; padding-bottom: 10px; }} .date {{ color: #777; margin-bottom: 30px; }} .content {{ font-size: 18px; }} </style> </head> <body> <h1>{html_title}</h1> <div class="date">작성일: {today}</div> <h2>본문</h2> <div class="content"> {html_content} </div> <hr> <p>이 글은 Python을 이용한 SNS 자동화 테스트입니다.</p> </body> </html> """

with open("index.html", "w", encoding="utf-8") as f:
f.write(html_page)

print("========================================")
print("블로그 글 생성 완료!")
print("제목:", title)
print("파일명: blog_post.md")
print("파일명: index.html")
print("========================================")