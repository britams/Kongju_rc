import datetime

def main():
    list_a = []
    list_b = list()
    print(type(list_a))
    print(type(list_b))
    ptime = datetime.datetime.now()
    list_c = [1, 2, 3.3, "Lee", ptime, True]
    print(f"{list_c}")
    list_c[3] = "Kim"
    print(f"{list_c}")
    
if __name__ == "__main__":
    main()