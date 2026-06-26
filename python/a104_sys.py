import sys


def main():
    print(sys.argv, len(sys.argv))
    print("-----")
    print(sys.copyright)
    print(sys.version)
    print(sys.version_info)
    print(sys.flags)


if __name__ == "__main__":
    main()


    # 실무에선 쪽지인 sys.argv 보단 정리된 서류인 argparse 