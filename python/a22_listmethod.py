class Mylist:
    def __init__(self): #생성자 메소드
        self.myVariable = "Lee" #인스턴스 변수
        self.myVariable2 = "Kim" #인스턴스 변수
        self.myList = list() #인스턴스 변수로 리스트를 초기화
    def append(self, element): # 인스턴스 메소드
        self.myList.append(element) #인스턴스 메소드에서 인스턴스 변수에 접근하여 리스트에 요소를 추가하는 예시입니다.

def main():
    list_a = [1, 2, 3, 4, 5]
    list_b = [5, 7, 8, 9, 10]
    print(list_a + list_b) # 리스트 합치기
    print(list_a)
    list_a.extend(list_b) # 리스트 확장
    print(list_a)

    list_b.append(11) # 리스트에 값 추가
    list_b.append(12)
    print(list_b)
    list_b.insert(1, 4.5) # 리스트에 값 삽입, type ignore
    print(list_b)

    myList_a = Mylist()
    myList_a.append("seohyunlee")
    print(myList_a.myVariable, myList_a.myVariable2, myList_a.myList)


if __name__ == "__main__":
    main()