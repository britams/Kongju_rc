# sudo apt update 터미널에서
# sudo apt install python3-pip 터미널에서
# pip install pywebview 터미널에서

from pathlib import Path

import webview

BASE_PATH = Path(__file__).resolve().parent
NOTE_PATH = BASE_PATH / "note.txt"


class MemoApi:
    def __init__(self):
        pass

    def save_note(self, text):
        NOTE_PATH.write_text(text, encoding="utf-8")  # 수정: NOTE_Path → NOTE_PATH
        return {"status": "saved", "path": str(NOTE_PATH)}

    def load_note(self):  # 수정: load_mote → load_note
        if not NOTE_PATH.exists():  # 추가: 파일 없을 때 빈 문자열 반환
            return {"text": ""}
        return {"text": NOTE_PATH.read_text(encoding="utf-8")}


def main():
    html_path = Path(__file__).resolve().parent / "text.html"

    api = MemoApi()  # 추가: API 인스턴스 생성

    webview.create_window(
        "simple memo",
        url=html_path.as_uri(),
        width=640,
        height=520,
        resizable=True,
        js_api=api,  # 수정: js_api 추가해야 HTML에서 Python 함수 호출 가능
    )

    webview.start()


if __name__ == "__main__":
    main()