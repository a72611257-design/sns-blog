@echo off
cd /d "%~dp0"

echo ========================================
echo AI 블로그 + SNS 자동화 시작
echo ========================================

echo.
echo [1단계] AI 블로그 글 생성 중...
python auto_to_multi.py

if errorlevel 1 (
    echo.
    echo AI 블로그 글 생성 중 오류가 발생했습니다.
    exit /b 1
)

echo.
echo [2단계] 블로그 글 저장 및 목록 업데이트 중...
python auto_multi.py

if errorlevel 1 (
    echo.
    echo 블로그 글 저장 중 오류가 발생했습니다.
    exit /b 1
)

echo.
echo [3단계] SNS 글 생성 중...
python sns_multi.py

if errorlevel 1 (
    echo.
    echo SNS 글 생성 중 오류가 발생했습니다.
    exit /b 1
)

echo.
echo [4단계] GitHub 업데이트 중...

git add index.html posts auto_to_multi.py auto_multi.py sns_multi.py blog_auto.bat .gitignore

git diff --cached --quiet
if errorlevel 1 (
    git commit -m "AI 블로그 및 SNS 자동 업데이트"
    git push origin main
) else (
    echo 변경된 GitHub 파일이 없습니다.
)

echo.
echo ========================================
echo AI 블로그 + SNS 자동화 완료!
echo ========================================
echo.
echo SNS 생성 파일:
echo sns_output\instagram.txt
echo sns_output\threads.txt
echo sns_output\x.txt
echo ========================================