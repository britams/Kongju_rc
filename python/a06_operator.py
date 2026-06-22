class Add_Test:
    def __add__(self, other):
        return "더하기 연산이 실행되었다."
# self 나 자신 의미. 무조건 들어감. other는 연산이 혼자서 되는게 아니니까 있는것. special method 따라 other 대신 다른게 들어간다.
# self는 모든 special method에 무조건 들어가는 매개변수.

def main():
    print(2 ** 4)
    print(2 ** 64)
    print(18/4)
    print(type(18/3))

    print(18//4)
    print(type(18//4))

    print(18%4)
    a = Add_Test()
    b = Add_Test()
    print(a + b)



if __name__ == "__main__":
    main()

# 클래스의 연산 -> +, -, *, /, //, % -> method 함수. 이들을 special method라고 부른다.빌트인클래스는 이미 이러한 special method가 정의되어 있다. 예를 들어 int 클래스에는 __add__, __sub__, __mul__, __truediv__, __floordiv__, __mod__ 등이 정의되어 있다.
# special method는 __add__, __sub__, __mul__, __truediv__, __floordiv__, __mod__, __repr__, __int__ 등으로 정의되어 있다.
# 오버라이딩 - 함수를 덮어씌워서 내맘대로 쓰는 것. 기존 값 버리고 새로운 값으로 덮어씌우기.
# 오버로딩 (Cpp 에서만 지원.) - 같은 이름의 함수를 여러개 만들어서 매개변수의 타입이나 개수에 따라 다른 동작을 하도록 하는 것. 파이썬에서는 오버로딩을 지원하지 않지만, 가변인자(*args, **kwargs)를 사용하여 비슷한 효과를 낼 수 있다.