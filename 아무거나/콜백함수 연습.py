import threading
import time



def read_file_async(on_complete):
    def worker():
        time.sleep(2)
        data = "파일 내용"
        on_complete(data)
    thread = threading.Thread(target=worker)
    thread.start()


    
def on_complete(data):
    print("3. 파일 읽기 완료:", data)

print("1. 시작")
read_file_async(on_complete)
print("2. 파일 읽기 요청만 하고 바로 다음 코드 실행")