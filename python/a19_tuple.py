def main():
    # 1. 빈 튜플을 만듭니다. tuple()은 빈 금고인 ()를 만들어내요.
    tu = tuple()
    # 화면에 ()와 이 친구의 종류인 <class 'tuple'>을 출력합니다.
    print(tu, type(tu))

    # 2. 튜플을 만들 때는 대괄호 `[]` 대신 소괄호 `()`를 사용해요!
    # 우리 코린이가 주석에 쓴 대로, 튜플은 한 번 만들면 원소 추가, 제거, 변경이 절대 안 됩니다!
    tu = (1, 2) 
    # 화면에 (1, 2)와 종류를 출력합니다.
    print(tu, type(tu))

    # 3. 변경은 안 되지만, 리스트처럼 몇 번째에 뭐가 들었는지 '구경'하는 것은 가능해요!
    # 0번째 자리에 있는 숫자 1을 꺼내서 보여줍니다.
    print(tu[0])

    # [수정 포인트] 에러가 나지 않도록 for문을 main() 함수 안쪽으로 들여쓰기 해줬어요!
    # 튜플도 리스트와 똑같이 안에 든 알맹이들(`ele`)을 하나씩 꺼내서 반복문을 돌릴 수 있어요.
    for ele in tu:
        print(ele)  # list 하고 같은 기능을 가진 컨테이너(저장소)
# system 내부적으로 안정적으로 데이터를 전달하기 위해서 tuple 사용 list 대신
    tu_1 = 1, 2 # 튜플 적용시 소괄호 생략하기도 함. 
    print(tu_1, type(tu_1))
    a = 10
    b = 20
    # swap C 스타일
    tmp = a
    a = b
    b = tmp
    print(a, b)
    # swap python 스타일
    a,b = b,a
    print (a, b)

if __name__ == "__main__":
    main()