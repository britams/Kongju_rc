import json


def main():
    # api 전송 보낼때 dictionary
    # yaml, toml, xml, json 의 파이썬 데이터 형태에 모두 쓰임
    dict_a = dict()
    dict_a = {"a": "aa"}
    print(type(dict_a))
    # 원소 추가
    dict_a["b"] = "bbb"
    print(dict_a)
    print(dict_a["a"], dict_a["b"], dict_a.get("c"))

    print(dict_a.pop("a"))
    print(dict_a)

    dict_a["a"] = "aa"
    dict_a["b"] = "bbb"
    dict_a["c"] = "cccc"
    dict_a["d"] = "ddddd"

    for key in dict_a:
        print(key, dict_a[key])

    for key, value in dict_a.items():
        print(key, value)

    print(dict_a.keys())
    print(dict_a.values())

    with open("data/dict_a.json", "w", encoding='utf-8') as f:
        json.dump(dict_a, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main()

# dic 키값에 대해서 해시테이블 바로 자료 연결. 키값으로 인덱싱을 한다는 것은 큰 장점.
# hash 함수 한번 실행하고 바로 저장하고. 따라서 dic 을 list 보다 더 사용한다는 것을 알고 있길. 모르면 AI.