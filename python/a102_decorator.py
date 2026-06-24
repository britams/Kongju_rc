from functools import wraps


def simple_rapper(value):
    def simple_rapper_inner(func):
        @wraps(func)
        def wrapper(*args, **kargs):
            print(f"func 실행 전 코드.. {value}")
            result = func(*args, **kargs)
            print("func 실행 후 코드..")
            return result
        return wrapper
    return simple_rapper_inner


@simple_rapper("hi")
def print_hello(n, v):
    for _ in range(n):
        print(v)
    return 123


def main():
    print(print_hello(3, "hi, hello"))
    print(print_hello.__name__)


if __name__ == "__main__":
    main()




# from functools import wraps -> decorator 이름 문제 해결
# @ wraps -> decorator 문제는 decorator로
# 가변인자와 키워드가변인자 * **