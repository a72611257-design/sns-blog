from datetime import datetime
import os

# ==============================
# 11강 - SNS 콘텐츠 자동 생성
# ==============================

with open("post.txt", "r", encoding="utf-8-sig") as f:
    text = f.read()

lines = text.splitlines()

# 제목 가져오기
title = next(
    (
        x.replace("제목:", "", 1).strip()
        for x in lines
        if x.startswith("제목:")
    ),
    ""
)

# 본문 가져오기
content = "\n".join(
    x
    for x in lines
    if not x.startswith("제목:")
    and not x.startswith("본문:")
).strip()

today = datetime.now().strftime("%Y-%m-%d")

if not title:
    title = "SNS 자동화 글 - " + today

# 저장 폴더
os.makedirs("sns_output", exist_ok=True)


# ==============================
# Instagram
# ==============================

instagram = f"""📌 {title}

{content}

✨ 자세한 이야기는 블로그에서 확인해 보세요.

#SNS #블로그 #자동화 #콘텐츠
"""


# ==============================
# Threads
# ==============================

threads = f"""{title}

{content}

여러분은 어떻게 생각하시나요?
오늘의 이야기를 공유합니다.
"""


# ==============================
# X
# ==============================

x_post = f"""{title}

{content}
"""

if len(x_post) > 270:
    x_post = x_post[:267] + "..."


# ==============================
# YouTube
# ==============================

youtube = f"""[영상 제목]

{title}


[영상 설명]

{content}


구독과 좋아요는 큰 도움이 됩니다.

#유튜브 #콘텐츠 #SNS
"""


# ==============================
# 파일 저장
# ==============================

with open(
    os.path.join("sns_output", "instagram.txt"),
    "w",
    encoding="utf-8"
) as f:
    f.write(instagram)

with open(
    os.path.join("sns_output", "threads.txt"),
    "w",
    encoding="utf-8"
) as f:
    f.write(threads)

with open(
    os.path.join("sns_output", "x.txt"),
    "w",
    encoding="utf-8"
) as f:
    f.write(x_post)

with open(
    os.path.join("sns_output", "youtube.txt"),
    "w",
    encoding="utf-8"
) as f:
    f.write(youtube)


# ==============================
# 완료 메시지
# ==============================

print("========================================")
print("SNS 콘텐츠 생성 완료!")
print("제목:", title)
print("========================================")
print("생성 파일:")
print("sns_output\\instagram.txt")
print("sns_output\\threads.txt")
print("sns_output\\x.txt")
print("sns_output\\youtube.txt")
print("========================================")
