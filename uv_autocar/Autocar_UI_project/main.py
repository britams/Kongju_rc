from pathlib import Path

import webview
from backend.server import AutocarServer

BASE_DIR = Path(__file__).resolve().parent
FRONTEND_DIR = BASE_DIR / "frontend"


def main() -> None:
    server = AutocarServer(FRONTEND_DIR)
    server.start()

    try:
        webview.create_window(
            "Autocar Dashboard",
            url=server.base_url,
            width=900,
            height=600,
            resizable=True,
        )
        webview.start()
    finally:
        server.stop()


if __name__ == "__main__":
    main()
