import webview
import os

NOTE_FILE = os.path.join(os.path.dirname(__file__), "note.txt")

class NoteApi:
    def save(self, text):
        with open(NOTE_FILE, "w", encoding="utf-8") as f:
            f.write(text)

    def load(self):
        if not os.path.exists(NOTE_FILE):
            return ""
        with open(NOTE_FILE, "r", encoding="utf-8") as f:
            return f.read()

def main():
    html_path = os.path.join(os.path.dirname(__file__), "front", "index.html")
    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()

    api = NoteApi()
    window = webview.create_window(
        title="메모장",
        html=html,
        js_api=api,
        width=750,
        height=550,
    )
    webview.start()

if __name__ == "__main__":
    main()
