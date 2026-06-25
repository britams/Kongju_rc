def simple_rapper(func):
    def wrapper():
        print("func 실행 전 코드..")
        func()
        print("func 실행 후 코드..")
    return wrapper


@simple_rapper
def print_hello():
    print("print_hello 함수가 실행됨")


def main():
    # wrapper = simple_rapper(print_hello)
    # wrapper()
    # wrapper()
    # wrapper()
    print_hello()

if __name__ == "__main__":
    main()

# wrapper 함수 만들면 decorator 함수 쓸 수 있음
# @simple_rapper

# 데코레이터는 복잡한 코드를 안만들때만 사용함.