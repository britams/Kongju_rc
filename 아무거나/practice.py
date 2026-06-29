def main():
    number = int(input("정수를 입력하세요:"))

    print( f"{number}는 홀수입니다." if number % 2 else "{number}는 짝수입니다." )


if __name__ == "__main__":
    main()