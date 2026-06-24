from collections.abc import Iterable


class SimpleIter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value


def main():
    iter = SimpleIter(0, 10)
    print(isinstance(iter, Iterable))
    print(isinstance("aa", str))
    print(isinstance("aa", object))
    for v in iter:
        print(v)


if __name__ == "__main__":
    main()


# 제너레이터는 이터레이터를 직접 만들 때 사용하는 코드
# 이터레이터는 반복하는 것.
# yield는 return 이랑 쓰임새 비슷. 
# 제너레이터는 for문과 같이 사용될수도 있다.
# 제너레이터는 함수의 실행이 매번 다른 결과를 요구할때 사용한다.
# 일련의 과정이 결정되어서 연속적으로 일을 수행할때. 
# 딕셔너리 컨테이너, 리스트 컨테이너 전부 이터레이터라고 말할 수 있음.
# __iter__-> 스페셜 메소드.
# 이터레이터와 데코레이터 같이 배운다.
