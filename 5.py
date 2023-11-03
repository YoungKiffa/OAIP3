def main():


    while True:
        se = int(input())
        if se == 0:
            break
        if not se % 7 and not se % 3:
            print('Караул!')
        elif not se % 3:
            print('Несчастливое')
        elif not se % 7:
            print('Опасное')
        else:
            print(se)


if __name__ == "__main__":
    main()