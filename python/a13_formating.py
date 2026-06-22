def main():
    string = "abc"
    string2 = "this is format test : {}".format(10)
    print(string)
    print(string2)

    string3 = "this is format test : {2}, {0}, {1}".format(10, 20, 30)
    print(string3)

    string4 = "this is format test : {2:d}, {1:5d}, {0:05d}".format(-10, -20, -30) #d는 decimal, 5d는 5자리로 맞추고, 
    #05d는 5자리로 맞추고 빈자리는 0으로 채우겠다. -10은 -10으로 출력됨. -20은 -20으로 출력됨. -30은 -30으로 출력됨.
    print(string4)

    string5 = "this is format test : {2:+.2f}, {1:+5.2f}, {0:+05.2f}".format(10.1263, -20.456, -30)#f는 float, 
    #+는 양수일때 +를 붙이겠다. .2f는 소수점 2자리까지 출력하겠다. 5.2f는 전체 5자리로 맞추고 소수점 2자리까지 출력하겠다. 
    # #05.2f는 전체 5자리로 맞추고 빈자리는 0으로 채우고 소수점 2자리까지 출력하겠다.
    print(string5)

    string6 = 10.126
    print(f"this is format test : {string6:+10.2f}")
    print(f"this is format test : {3.141592:+10.2f}")

if __name__ == "__main__":
    main()
# string 가시성 안좋아서 대부분 fstring 사용.