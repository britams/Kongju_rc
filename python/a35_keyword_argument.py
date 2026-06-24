# [정의부] 함수의 방들을 만드는 곳
# 방 순서 규칙: 일반 방(n) -> 보자기 방(*args) -> 기본값 방(abc, defg) -> 키워드 보자기 방(**keyargs)
def print_n_times(n, *args, abc="abc", defg="defg", **keyargs): 
    # positional, default, variable-length, keyword, variable-length-keyword
    
    # 1. n번 만큼 반복하며 *args 보자기 내용물 출력
    for i in range(n):
        print(args)
        
    # 2. 기본값 방들의 내용물 출력
    print(abc, defg)
    
    # 3. [새로운 치트키 ⭐] **keyargs는 이름표가 붙은 찌꺼기들을 '딕셔너리' 형태로 다 흡수해요!
    print(type(keyargs), keyargs)
    
    # 4. 딕셔너리에 담긴 이름표(k)와 내용물(v)을 하나씩 꺼내서 출력합니다.
    for k, v in keyargs.items():
        print(k, v)


# 래퍼(Wrapper) 함수: 들어오는 모든 재료를 다 받아내는 마법의 만능 함수 틀이에요!
def general_f(*args, **keyargs): 
     # pass를 지우고 내부를 채워보면 어떻게 받아 가는지 볼 수 있어요.
     print("만능 함수 args:", args)
     print("만능 함수 keyargs:", keyargs)


def main():
    print("--- 1번 실험 ---")
    print_n_times(3, "choi", "su", "gil", "is", "teacher")
    
    print("\n" + "="*40 + "\n--- 2번 실험 ---")
    # a=1, b="sdf", df="sdf" 처럼 기존 방 이름(abc, defg)에 없는 
    # 듣도 보도 못한 이름표 배달들은 전부 우측 끝에 있는 **keyargs 상자로 쏙 들어갑니다!
    print_n_times(3, "test", defg="마지막 문자", abc="첫 문자", a=1, b="sdf", df="sdf")
    
    print("\n" + "="*40 + "\n--- 3번 만능 함수 실험 ---")
    general_f(1, 2, 4, k="234")


if __name__ == "__main__":
    main()