def main():
    # 1. 빈 튜플
    tu = tuple()
    print(tu, type(tu))

    # 2. 튜플: () 사용, 한 번 만들면 변경 불가
    tu = (1, 2)
    print(tu, type(tu))

    # 3. 인덱스로 조회는 가능
    print(tu[0])

    # 4. for문으로 순회 가능 (list와 동일)
    for ele in tu:
        print(ele)

    # 5. 소괄호 생략 가능 / system 내부 데이터 전달 시 주로 사용
    tu_1 = 1, 2
    print(tu_1, type(tu_1))

    a = 10
    b = 20
    # swap C 스타일
    tmp = a
    a = b
    b = tmp
    print(a, b)
    # swap python 스타일
    a, b = b, a
    print(a, b)

if __name__ == "__main__":
    main()
