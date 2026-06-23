def main():
    print(10==100)#False
    print(10 != 100)#True
    print(10 < 100)#True
    print(10 <= 100)#True
    print(type(True))#<class 'bool'>

    print(not True)#False
    print(not False)#True
    print(True and True)#True
    print(False and False)#False
    print(True and False)#False

    a = int(input("100보다 큰 수를 입력하세요: "))
    if a > 100:
        print("입력하신 수는 100보다 큽니다.")
    print("프로그램을 종료합니다.")

if __name__ == "__main__":
    main()
    #python True, False 대문자로 시작. 0은 False, 0이 아닌 수는 True.
    #  0.0은 False, 0.1은 True. ""은 False, "a"는 True. []은 False, [1]은 True. None은 False.
    # c에서 !, &&, || 연산자. 파이썬에서는 not, and, or 연산자.
