let timerInterval = null;
let elapsedSeconds = 0;
let prevState = {};
let historyMode = false;   // 예전 로그 보기 모드
const MAX_LOG_LINES = 15;

// 시계
function updateClock() {
    const now = new Date();
    const h = String(now.getHours()).padStart(2, '0');
    const m = String(now.getMinutes()).padStart(2, '0');
    const s = String(now.getSeconds()).padStart(2, '0');
    document.getElementById('clock').textContent = `${h}:${m}:${s}`;
}
setInterval(updateClock, 1000);
updateClock();

function formatTime(sec) {
    const h = String(Math.floor(sec / 3600)).padStart(2, '0');
    const m = String(Math.floor((sec % 3600) / 60)).padStart(2, '0');
    const s = String(sec % 60).padStart(2, '0');
    return `${h}:${m}:${s}`;
}

function formatCumulative(sec) {
    const d = Math.floor(sec / 86400);
    const h = Math.floor((sec % 86400) / 3600);
    const m = Math.floor((sec % 3600) / 60);
    const s = sec % 60;
    if (d > 0) return `${d}일 ${h}시간 ${m}분 ${s}초`;
    if (h > 0) return `${h}시간 ${m}분 ${s}초`;
    if (m > 0) return `${m}분 ${s}초`;
    return `${s}초`;
}

function trimLogBox() {
    const box = document.getElementById('log-box');
    while (box.children.length > MAX_LOG_LINES) {
        box.removeChild(box.firstChild);
    }
}

function addLog(msg, type = 'info') {
    // 예전 로그 모드면 새 동작시 초기화
    if (historyMode) {
        document.getElementById('log-box').innerHTML = '';
        historyMode = false;
    }

    const box = document.getElementById('log-box');
    const now = new Date();
    const time = `${String(now.getHours()).padStart(2,'0')}:${String(now.getMinutes()).padStart(2,'0')}:${String(now.getSeconds()).padStart(2,'0')}`;
    const entry = document.createElement('div');
    entry.className = 'log-entry';
    entry.innerHTML = `<span class="log-time">[${time}]</span><span class="log-msg ${type}">${msg}</span>`;
    box.appendChild(entry);
    trimLogBox();
    box.scrollTop = box.scrollHeight;

    // 서버에 저장
    fetch('/api/log', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ time, msg, type }),
    });
}

let selectedDay = null;   // 0=오늘, 1=1일전, 2=2일전
let selectedAmPm = null;  // 'am' or 'pm'

function selectDay(d) {
    selectedDay = d;
    [0, 1, 2].forEach(n => {
        document.getElementById(`btn-day-${n}`).classList.toggle('selected', n === d);
    });
}

function selectAmPm(val) {
    selectedAmPm = val;
    document.getElementById('btn-am').classList.toggle('selected', val === 'am');
    document.getElementById('btn-pm').classList.toggle('selected', val === 'pm');
}

function clearLog() {
    document.getElementById('log-box').innerHTML = '';
    historyMode = false;

    // 날짜/AM PM 선택 초기화
    selectedDay = null;
    selectedAmPm = null;
    [0, 1, 2].forEach(n => document.getElementById(`btn-day-${n}`).classList.remove('selected'));
    document.getElementById('btn-am').classList.remove('selected');
    document.getElementById('btn-pm').classList.remove('selected');
    document.getElementById('filter-hour').value = '';
    document.getElementById('filter-minute').value = '';

    addLog('로그 지워짐', 'info');
}

function renderLogs(logs) {
    const box = document.getElementById('log-box');
    box.innerHTML = '';
    historyMode = true;
    const show = logs.slice(-MAX_LOG_LINES);
    show.forEach(l => {
        const entry = document.createElement('div');
        entry.className = 'log-entry';
        entry.innerHTML = `<span class="log-time">(${l.time})</span><span class="log-msg ${l.type}">${l.msg}</span>`;
        box.appendChild(entry);
    });
    box.scrollTop = box.scrollHeight;
    if (logs.length === 0) {
        historyMode = false;
        addLog('해당 시간대 로그 없음', 'info');
    }
}

function loadLogsTime() {
    if (prevState.drive) {
        addLog('구동 중에는 예전 로그를 불러올 수 없어요!', 'off');
        return;
    }

    // 날짜 선택 확인
    if (selectedDay === null) {
        addLog('다시 입력하세요 (날짜 선택 필요)', 'off');
        return;
    }

    // 시간 검증
    const hourVal = document.getElementById('filter-hour').value;
    const minuteVal = document.getElementById('filter-minute').value;
    const hour = parseInt(hourVal);
    const minute = parseInt(minuteVal);

    if (hourVal === '' || isNaN(hour) || hour < 1 || hour > 12) {
        addLog('다시 입력하세요 (시: 1~12)', 'off');
        return;
    }
    if (selectedAmPm === null) {
        addLog('다시 입력하세요 (AM/PM 선택 필요)', 'off');
        return;
    }
    if (minuteVal === '' || isNaN(minute) || minute < 0 || minute > 59) {
        addLog('다시 입력하세요 (분: 0~59)', 'off');
        return;
    }

    // 12h → 24h 변환
    let hour24 = hour;
    if (selectedAmPm === 'am' && hour === 12) hour24 = 0;
    else if (selectedAmPm === 'pm' && hour !== 12) hour24 = hour + 12;

    const url = `/api/logs?days=${selectedDay}&hour=${hour24}&minute=${minute}`;
    fetch(url)
        .then(r => r.json())
        .then(logs => renderLogs(logs))
        .catch(() => addLog('로그 불러오기 실패', 'off'));
}

function setAllDisabled(disabled) {
    ['btn-connected', 'btn-drive', 'btn-charging'].forEach(id => {
        const btn = document.getElementById(id);
        if (btn) btn.disabled = disabled;
    });
}

function applyState(data) {
    const connActive = data.connected;
    document.getElementById('card-connected').classList.toggle('active', connActive);
    document.getElementById('status-connected').textContent = connActive ? '연결됨' : '끊김';
    document.getElementById('btn-connected').textContent = connActive ? 'Stop' : 'Start';

    const driveActive = data.drive;
    document.getElementById('card-drive').classList.toggle('active', driveActive);
    document.getElementById('status-drive').textContent = driveActive ? '작동중' : '멈춤';
    document.getElementById('btn-drive').textContent = driveActive ? 'Stop' : 'Start';

    const chargingActive = data.charging;
    document.getElementById('btn-charging').textContent = chargingActive ? '충전 Stop' : '충전 Start';

    const bat = data.battery;
    document.getElementById('status-battery').textContent = `${bat.toFixed(1)}%`;
    const bar = document.getElementById('battery-bar');
    bar.style.width = `${bat}%`;
    bar.style.background = bat > 50 ? '#22c55e' : bat > 20 ? '#f59e0b' : '#ef4444';

    const chargeEl = document.getElementById('charge-remaining');
    if (chargingActive && bat < 100) {
        const remainingSec = Math.ceil((100 - bat) / 5) * 5;
        chargeEl.textContent = `충전 잔여: ${formatTime(remainingSec)}`;
        chargeEl.style.display = 'block';
    } else {
        chargeEl.style.display = 'none';
    }

    const driveEl = document.getElementById('drive-remaining');
    if (data.drive && bat > 0) {
        const estSec = Math.floor(bat / 10 * 5);
        driveEl.textContent = `예상 구동: ${formatTime(estSec)}`;
        driveEl.style.display = 'block';
    } else {
        driveEl.style.display = 'none';
    }

    if (bat <= 0) {
        setAllDisabled(true);
        document.getElementById('btn-charging').disabled = false;
    } else {
        setAllDisabled(false);
    }

    elapsedSeconds = data.elapsed;
    document.getElementById('timer').textContent = formatTime(elapsedSeconds);
document.getElementById('timer-cumulative').textContent = formatCumulative(data.cumulative_drive);
    const totalM = Math.floor(data.distance * 1000);
    const distText = totalM >= 1000
        ? `${Math.floor(totalM / 1000)}km ${totalM % 1000}m`
        : `${totalM}m`;
    document.getElementById('distance').textContent = distText;

    if (data.connected && data.drive) {
        if (!timerInterval) {
            timerInterval = setInterval(() => {
                elapsedSeconds++;
                document.getElementById('timer').textContent = formatTime(elapsedSeconds);
            }, 1000);
        }
    } else {
        clearInterval(timerInterval);
        timerInterval = null;
    }

    prevState = data;
}

function toggle(key) {
    if (prevState.battery <= 0 && key !== 'charging') {
        addLog('Low Battery!', 'off');
        return;
    }
    if (key === 'drive' && !prevState.connected) {
        addLog('Check Connection!', 'off');
        return;
    }
    if (key === 'drive' && prevState.charging) {
        addLog('Currently Charging!', 'off');
        return;
    }
    if (key === 'charging' && prevState.drive) {
        addLog("Battery can't be Charged!", 'off');
        return;
    }
    if (key === 'charging' && prevState.battery >= 100) {
        addLog('Battery Full!', 'info');
        return;
    }

    fetch(`/api/toggle/${key}`, { method: 'POST' })
        .then(r => r.json())
        .then(data => {
            applyState(data);
            if (key === 'connected') {
                if (!data.connected && prevState.drive) {
                    addLog('Connection Loss!', 'off');
                } else {
                    addLog(data.connected ? '접속 연결됨' : '접속 끊김', data.connected ? 'on' : 'off');
                }
            } else if (key === 'drive') {
                addLog(data.drive ? '구동 작동 시작' : '구동 멈춤', data.drive ? 'on' : 'off');
                if (data.drive) {
                    const estSec = Math.floor(data.battery / 10 * 5);
                    addLog(`예상 구동 가능시간: ${formatTime(estSec)} (배터리 ${data.battery.toFixed(1)}%)`, 'info');
                }
            } else if (key === 'charging') {
                addLog(data.charging ? '배터리 충전 시작' : '배터리 충전 중지', data.charging ? 'on' : 'off');
            }
        })
        .catch(err => addLog(`오류: ${err}`, 'off'));
}

// SSE
const events = new EventSource('/api/events');
events.addEventListener('message', e => {
    const data = JSON.parse(e.data);

    if (prevState.battery !== undefined && data.battery !== prevState.battery) {
        const diff = (data.battery - prevState.battery).toFixed(1);
        const sign = diff > 0 ? '+' : '';
        addLog(`배터리 ${data.battery.toFixed(1)}% (${sign}${diff}%)`, diff > 0 ? 'on' : 'off');
    }

    if (data.alert === 'fully_charged') {
        addLog('Fully Charged!', 'on');
    } else if (data.alert === 'battery_low') {
        addLog('Battery should be Charged! (20%)', 'off');
    } else if (data.alert === 'battery_dead') {
        addLog('Low Battery!', 'off');
    }

    applyState(data);
});
events.addEventListener('error', () => {
    addLog('서버 연결 오류', 'off');
});

addLog('Autocar Dashboard 시작됨', 'info');
