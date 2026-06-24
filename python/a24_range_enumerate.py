def main():
    # 1. range 기능 확인
    print(range(10)) # 0..9
    print(range(0, 10, 1)) # 0..9
    a = range(10)
    print(list(a))
    print(list(range(5, 10, 3)))
    
    # 2. for문을 이용한 일반적인 리스트 채우기
    a = []
    for i in range(0, 100, 2):
        a.append(i + 1)  # 그냥 단순반복, append는 리스트라는 주머니에 데이터를 '추가(Append)'하는 기능을 담당하는 함수(메소드)
    print(a)  # <-- for문 밖으로 빼서 최종 결과만 한 번 출력합니다.

    # 3. List Comprehension (리스트 컴프리헨션)
    a = [i + 1 for i in range(100)]
    print(a)

    # 4. Enumerate 활용
    list_b = ["a", "b", "c", "d", "e", "f"]
    for idx, ele in enumerate(list_b):  # 변수명을 a 대신 idx로 변경 # for 에 괄호 없이 , -> 튜플
        print(ele + "원소", idx)
        
    # 5. 두 리스트 동시에 순회하기 (인덱스 vs zip)
    list_c = ["a", "b", "c", "d", "e", "f"]
    
    for i in range(6):
        print(list_b[i], list_c[i]) 
        
    for b, c in zip(list_b, list_c): # 강사님 말씀대로 아래(zip)가 훨씬 파이썬다운(Pythonic) 코드입니다!
        print(b, c, end="  ") 

        #enumerate()는 리스트를 돌 때 "몇 번째(인덱스)인지 번호표"를 함께 붙여주는 것이고,
        #zip()은 여러 개의 리스트를 "같은 순서끼리 바지 지퍼 올리듯 세트로" 묶어주는 것입니다.


if __name__ == "__main__":
    main()