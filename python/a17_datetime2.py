import datetime
from a01_hello import main as hello_main
#1. 현재위치(우선권) 2. PYTHON_PATH 환경변수 중요

def main():
    hello_main()
    now = datetime.datetime.now()
    print(f"현재 날짜와 시간: {now}")

    input_var = input("몇월인지 입력하세요")
    if input_var.isdigit():
        month = int(input_var)
        if month in [3, 4, 5]:
            print(f"{month}월은 봄입니다.")
        elif month in [6, 7, 8]:
            print(f"{month}월은 여름입니다.")
        elif month in [9, 10, 11]:
            print(f"{month}월은 가을입니다.")
        elif month in [12, 1, 2]:
            print(f"{month}월은 겨울입니다.")
        else:
            print("1월부터 12월까지 입력해주세요.")
    else:
        print("숫자로 입력해주세요.")

if __name__ == "__main__":
    main()  
    # c에서  #include <stdio.h> 이런 전처리 지시자는 파이썬에서는 import로 대체된다.  