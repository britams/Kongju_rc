def power(item):
    return item * item

def under_3(item):
    return item < 3


def main():
    li = [1, 2, 3, 4, 5]
    output_map = map(power, li)
    print(list(output_map))
    output_map = map(lambda x: x * x, li)
    print(list(output_map))
    output_under_3 = filter(under_3, li)
    print(list(output_under_3))
    output_under_3 = filter(lambda x: x < 3, li)
    print(list(output_under_3))


if __name__ == "__main__":
    main()



#람다함수 코드 중간에 보이면 함수들어가는 자리를 대신한거.
#lambda(람다)는 한마디로 "이름 없는 일회용 미니 함수"예요.
