# Windows 실행 설정

프로젝트 폴더: `C:\Users\user\sns-auto\sns-blog`

## 최초 1회 설정

```bat
cd /d C:\Users\user\sns-auto\sns-blog
python -m pip install -r requirements.txt
setx OPENAI_API_KEY "발급받은_OpenAI_API_키"
setx OPENAI_MODEL "gpt-5-mini"
```

`setx` 실행 후 현재 명령 프롬프트를 닫고 새로 여세요. API 키는 코드나 GitHub에 넣지 마세요.

## 진단과 실행

```bat
cd /d C:\Users\user\sns-auto\sns-blog
python diagnose.py
blog_auto.bat
```

오류가 나면 `automation.log` 마지막 부분에 원인이 한글로 남습니다.

## 결과 위치

- GitHub Pages용 글: `posts`
- 인스타그램·Threads·X·YouTube 문안: `sns_output`
- 티스토리 붙여넣기용 HTML: `tistory_output\latest.html`

티스토리 Open API가 종료되어 공식 API 자동 발행은 지원되지 않습니다. HTML 초안을 확인한 후 티스토리 에디터에 붙여넣어 발행합니다.
