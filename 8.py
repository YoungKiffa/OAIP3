def main():


    a = input().split()
    b = a[0]
    c = len(a) - 1
    d = 0
    while d != c:
        if len(b) > len(a[d]):
            b = a[d]
        else:
            pass
        d += 1
    print(b)


if __name__ == "__main__":
    main()