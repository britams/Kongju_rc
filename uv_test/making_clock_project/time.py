import webview
import os

def main():
    # HTML 파일을 문자열로 직접 읽어서 넘기기 (인코딩 문제 해결)
    html_path = os.path.join(os.path.dirname(__file__), "index.html")
    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()

    window = webview.create_window(
        title="탁상시계",
        html=html,
        width=600,
        height=300,
    )
    webview.start()

if __name__ == "__main__":
    main()
