import json
import queue
import time
from datetime import datetime, timedelta
from pathlib import Path
from threading import Lock, Thread

from flask import Flask, Response, jsonify, request, send_from_directory
from werkzeug.serving import make_server

PORT = 49400
SPEED_KMH = 4.0


class AutocarServer:
    def __init__(self, frontend_dir: Path) -> None:
        self.frontend_dir = Path(frontend_dir).resolve()
        self.port = PORT
        self._lock = Lock()
        self._event_clients: list[queue.Queue] = []
        self._server = None
        self._thread = None
        self._owns_server = False

        self._state = {
            "connected": False,
            "drive": False,
            "charging": False,
            "battery": 87.0,
            "start_time": None,
            "cumulative_drive": 0,   # 누적 구동시간 (초)
            "session_start": None,   # 현재 구동 세션 시작
        }

        # 로그 파일 경로
        self._log_file = Path(__file__).resolve().parent.parent / "logs.json"
        self._logs: list[dict] = self._load_log_file()

        self._battery_thread = Thread(target=self._battery_loop, daemon=True)
        self._battery_thread.start()

        self.app = Flask(__name__, static_folder=str(self.frontend_dir), static_url_path="")
        self.app.add_url_rule("/", "index", self._serve_index)
        self.app.add_url_rule("/api/status", "status", self._get_status)
        self.app.add_url_rule("/api/toggle/<key>", "toggle", self._toggle, methods=["POST"])
        self.app.add_url_rule("/api/events", "events", self._stream_events)
        self.app.add_url_rule("/api/log", "log", self._save_log, methods=["POST"])
        self.app.add_url_rule("/api/logs", "logs", self._get_logs)

    def _load_log_file(self) -> list:
        if not self._log_file.exists():
            return []
        try:
            with open(self._log_file, "r", encoding="utf-8") as f:
                logs = json.load(f)
            # 2일 이전 로그 버리기
            cutoff = (datetime.now() - timedelta(days=2)).timestamp()
            return [l for l in logs if l["ts"] >= cutoff]
        except Exception:
            return []

    def _save_log_file(self):
        with open(self._log_file, "w", encoding="utf-8") as f:
            json.dump(self._logs, f, ensure_ascii=False)

    def _save_log(self):
        data = request.get_json()
        entry = {
            "ts": time.time(),
            "time": data.get("time", ""),
            "msg": data.get("msg", ""),
            "type": data.get("type", "info"),
        }
        with self._lock:
            self._logs.append(entry)
            # 2일 이전 로그 정리
            cutoff = (datetime.now() - timedelta(days=2)).timestamp()
            self._logs = [l for l in self._logs if l["ts"] >= cutoff]
            self._save_log_file()
        return jsonify({"ok": True})

    def _get_logs(self):
        days_ago = request.args.get("days", type=int)
        hour = request.args.get("hour", type=int)
        minute = request.args.get("minute", type=int)

        with self._lock:
            logs = list(self._logs)

        now = datetime.now()

        if days_ago is not None:
            target_date = (now - timedelta(days=days_ago)).date()
            logs = [l for l in logs if datetime.fromtimestamp(l["ts"]).date() == target_date]

        if hour is not None:
            logs = [l for l in logs if datetime.fromtimestamp(l["ts"]).hour == hour]

        if minute is not None:
            logs = [l for l in logs if datetime.fromtimestamp(l["ts"]).minute == minute]

        return jsonify(logs)

    def _battery_loop(self):
        prev_battery = self._state["battery"]
        while True:
            time.sleep(5)
            alert = None
            with self._lock:
                if self._state["charging"] and self._state["battery"] < 100.0:
                    self._state["battery"] = round(min(100.0, self._state["battery"] + 5.0), 1)
                    if self._state["battery"] >= 100.0:
                        self._state["charging"] = False
                        alert = "fully_charged"

                if self._state["drive"] and self._state["battery"] > 0.0:
                    self._state["battery"] = round(max(0.0, self._state["battery"] - 10.0), 1)
                    if prev_battery > 20.0 and self._state["battery"] <= 20.0:
                        alert = "battery_low"
                    if self._state["battery"] <= 0.0:
                        # 누적 구동시간 저장 후 초기화
                        if self._state["session_start"]:
                            self._state["cumulative_drive"] += int(time.time() - self._state["session_start"])
                        self._state["drive"] = False
                        self._state["connected"] = False
                        self._state["start_time"] = None
                        self._state["session_start"] = None
                        alert = "battery_dead"

                prev_battery = self._state["battery"]

            payload = self._build_payload()
            if alert:
                payload["alert"] = alert
            self._broadcast(payload)

    def _serve_index(self):
        return send_from_directory(self.frontend_dir, "index.html")

    def _get_status(self):
        return jsonify(self._build_payload())

    def _build_payload(self):
        with self._lock:
            # 현재 세션 구동시간
            current_drive = 0
            if self._state["session_start"] and self._state["drive"]:
                current_drive = int(time.time() - self._state["session_start"])

            # 누적 구동시간
            cumulative = self._state["cumulative_drive"] + current_drive

            # 총 주행거리 (km) = 누적구동시간(h) * 4km/h
            distance = round(cumulative / 3600 * SPEED_KMH, 3)

            # 작동시간 (접속+구동 둘 다일 때)
            elapsed = 0
            if self._state["start_time"] and self._state["connected"] and self._state["drive"]:
                elapsed = int(time.time() - self._state["start_time"])

            return {
                "connected": self._state["connected"],
                "drive": self._state["drive"],
                "charging": self._state["charging"],
                "battery": self._state["battery"],
                "elapsed": elapsed,
                "current_drive": current_drive,
                "cumulative_drive": cumulative,
                "distance": distance,
            }

    def _toggle(self, key):
        with self._lock:
            if key == "connected":
                self._state["connected"] = not self._state["connected"]
                if not self._state["connected"]:
                    # 접속 끊기면 구동도 종료 + 누적 저장
                    if self._state["drive"] and self._state["session_start"]:
                        self._state["cumulative_drive"] += int(time.time() - self._state["session_start"])
                    self._state["drive"] = False
                    self._state["start_time"] = None
                    self._state["session_start"] = None

            elif key == "drive":
                self._state["drive"] = not self._state["drive"]
                if self._state["drive"]:
                    self._state["session_start"] = time.time()
                else:
                    # 구동 종료 시 누적 저장
                    if self._state["session_start"]:
                        self._state["cumulative_drive"] += int(time.time() - self._state["session_start"])
                    self._state["session_start"] = None

            elif key == "charging":
                self._state["charging"] = not self._state["charging"]

            # 작동시간: 접속+구동 둘 다 켜질 때 시작
            if self._state["connected"] and self._state["drive"]:
                if self._state["start_time"] is None:
                    self._state["start_time"] = time.time()
            else:
                self._state["start_time"] = None

        payload = self._build_payload()
        self._broadcast(payload)
        return jsonify(payload)

    def _broadcast(self, payload):
        for q in list(self._event_clients):
            q.put(payload)

    def _stream_events(self):
        client_queue = queue.Queue()
        with self._lock:
            self._event_clients.append(client_queue)
        client_queue.put(self._build_payload())

        def stream():
            try:
                while True:
                    payload = client_queue.get()
                    yield f"data: {json.dumps(payload)}\n\n"
            finally:
                with self._lock:
                    if client_queue in self._event_clients:
                        self._event_clients.remove(client_queue)

        return Response(stream(), mimetype="text/event-stream")

    @property
    def base_url(self):
        return f"http://127.0.0.1:{self.port}"

    def start(self):
        try:
            self._server = make_server("127.0.0.1", self.port, self.app, threaded=True)
            self._thread = Thread(target=self._server.serve_forever, daemon=True)
            self._thread.start()
            self._owns_server = True
        except OSError:
            pass

    def stop(self):
        if self._owns_server and self._server:
            self._server.shutdown()
