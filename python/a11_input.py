def main():
    input_var = input("숫자를 입력하세요")
    print(type(input_var), input_var)
    # try:
    #     print(int(input_var) + 100)
    # except ValueError: # 에러가 나면 처리하는 방법 try except 구문. except ValueError: 에러가 나면 pass로 처리하겠다.
    #     print("숫자가 아닙니다.") 
    #     pass
    if input_var.isdigit(): # isdigit() 메서드는 문자열이 숫자로만 이루어져 있는지 확인하는 메서드입니다. 숫자로만 이루어져 있으면 True를 반환하고, 그렇지 않으면 False를 반환합니다.
        print(int(input_var) + 100)
    else:
        print("숫자가 아닙니다.")
# is 붙여져 있는거 사용하면 정밀하게 검사 가능.

if __name__ == "__main__":
    main()