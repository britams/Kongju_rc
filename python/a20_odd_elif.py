def main():
    number = int(input("정수를 입력하세요: "))

    # if number % 2 == 0: # 0 1 -> 0이면 false
    #     print(f"{number}는 짝수입니다.")
    # else:
    #     print(f"{number}는 홀수입니다.")   

    print("홀수" if number % 2 else "짝수", "입니다.") # 조건문 ? true : false -> 파이썬에서는 조건문 
    #? true : false 대신에 true if 조건문 else false 형태로 사용한다. 
    # number % 2가 0이면 false, 0이 아니면 true이므로 홀수인지 짝수인지 판별할 수 있다.


if __name__ == "__main__":
    main()