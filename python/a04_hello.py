class A_test:
    def __repr__(self):
        return "This is a test class"

import keyword

def main():
    print(12324)
    print(123, "choi", "sun", "woo")
    print(3.12415)
    a = A_test()
    print(a)

    print("this is", "a", "test", sep="_", end="!!! ")
    print("this is", "a", "test", sep="-")

if __name__ == "__main__":
    main()
