def main():


    x, y, z = map(int, input().split())

    while True:
        a, b, c = map(int, input().split())
        if a == 0 and b == 0 and c == 0:
            break
        if a > x or b > y or c > z:
            print("Да")
        else:
            print("Нет")


if __name__ == "__main__":
    main()