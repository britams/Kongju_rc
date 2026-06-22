class Person:
    def __init__(self, name):
        self.name = name

    # 짠! 여기에 마법의 함수를 추가합니다.
    def __repr__(self):
        return f"Person(이름: {self.name})"


import keyword

def main():
    print(12324)
    print(123, "choi", "sun", "woo")
    print(3.12415)
    p = Person("철수")
    print(p)

    print("this is", "a", "test", sep="_", end="!!! ")
    print("this is", "a", "test", sep="-")

if __name__ == "__main__":
    main()
