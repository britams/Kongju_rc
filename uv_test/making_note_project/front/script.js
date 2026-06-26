function showStatus(msg) {
    const status = document.getElementById('status');
    status.textContent = msg;
    setTimeout(() => { status.textContent = ''; }, 2000);
}

function load() {
    pywebview.api.load().then(function (text) {
        document.getElementById('memo').value = text;
        showStatus('불러왔어요!');
    });
}

function save() {
    const text = document.getElementById('memo').value;
    pywebview.api.save(text).then(function () {
        showStatus('저장됐어요!');
    });
}

// 앱 시작할 때 자동으로 불러오기
window.addEventListener('pywebviewready', load);
