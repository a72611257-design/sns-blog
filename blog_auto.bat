@echo off
chcp 65001 >nul
setlocal
cd /d "%~dp0"
call :run >> "%~dp0automation.log" 2>&1
set "RESULT=%ERRORLEVEL%"
type "%~dp0automation.log"
exit /b %RESULT%

:run
echo [%date% %time%] AI 블로그 + SNS 자동화 시작
python diagnose.py
if errorlevel 1 exit /b 1
python auto_to_multi.py
if errorlevel 1 exit /b 1
python auto_multi.py
if errorlevel 1 exit /b 1
python sns_multi.py
if errorlevel 1 exit /b 1
git add index.html posts auto_to_multi.py auto_multi.py sns_multi.py blog_auto.bat diagnose.py requirements.txt .gitignore
if errorlevel 1 exit /b 1
git diff --cached --quiet
if errorlevel 1 (
    git commit -m "AI 블로그 및 SNS 자동 업데이트"
    if errorlevel 1 exit /b 1
    git push origin main
    if errorlevel 1 exit /b 1
) else (
    echo 변경된 GitHub 파일이 없습니다.
)
echo [%date% %time%] 자동화 완료
echo 티스토리 초안: tistory_output\latest.html
echo SNS 결과: sns_output
exit /b 0
