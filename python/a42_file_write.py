from pathlib import Path


def main():
    # print(Path(__file__).parent)
    # f = open(Path(__file__).parent.parent / "data" / "text.txt", "w")
    # f.write("안녕하세요\n")
    # f.close()
    url = Path(__file__).parent.parent / "data" / "text.txt"
    with open(url, "a", encoding='utf-8') as f:
        f.write("안녕하세요\n")


if __name__ == "__main__":
    main()
#실행하면 텍스트 파일 생김. 
#w 모드 a 모드 구별해서. w 모드는 사라짐 조심해서
# a 모드는 실행시 안사라짐 안전.
#f는 파일포인터
# 파일 위치 지정하려면 Path 클래스 지정
# with는 context 파일 블록 끝나면 context 해제
# binary 저장 - 010101

