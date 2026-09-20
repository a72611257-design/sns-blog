import os
import shutil
import subprocess
import sys

def result(ok, name, detail):
    print(("[정상] " if ok else "[확인 필요] ") + f"{name}: {detail}")
    return ok

print("=== 블로그·SNS 자동화 진단 ===")
all_ok = result(sys.version_info >= (3, 10), "Python", sys.version.split()[0])
try:
    import openai
    all_ok &= result(True, "openai 패키지", getattr(openai, "__version__", "설치됨"))
except ImportError:
    all_ok &= result(False, "openai 패키지", "미설치 - python -m pip install -r requirements.txt 실행")

key = os.getenv("OPENAI_API_KEY", "").strip()
all_ok &= result(bool(key), "OPENAI_API_KEY", "등록됨" if key else "없음")
result(True, "OPENAI_MODEL", os.getenv("OPENAI_MODEL", "gpt-5-mini"))
git = shutil.which("git")
all_ok &= result(bool(git), "Git", git or "설치되어 있지 않거나 PATH에 없음")
if git:
    check = subprocess.run([git, "rev-parse", "--is-inside-work-tree"], capture_output=True, text=True)
    all_ok &= result(check.returncode == 0, "Git 저장소", "정상" if check.returncode == 0 else "현재 폴더가 저장소가 아님")
required = ["auto_to_multi.py", "auto_multi.py", "sns_multi.py", "blog_auto.bat", "post.txt"]
missing = [name for name in required if not os.path.exists(name)]
all_ok &= result(not missing, "필수 파일", "정상" if not missing else "누락: " + ", ".join(missing))
print("\n진단 결과:", "기본 실행 조건 정상" if all_ok else "위의 '확인 필요' 항목을 먼저 수정하세요.")
sys.exit(0 if all_ok else 1)
