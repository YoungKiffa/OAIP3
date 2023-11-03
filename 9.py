def main():


    sas = input()
    if sas == 'стоп':
        exit()
    sas = int(sas)
    kak = ''
    while True:
        sys = input()
        if sys == 'стоп':
            break
        if sys in '+-/*':
            kak = sys
            continue
        elif kak == '+':
            sas += int(sys)
        elif kak == '-':
            sas -= int(sys)
        elif kak == '/':
            sas /= int(sys)
        elif kak == '*':
            sas *= int(sys)
    print(int(sas))


if __name__ == "__main__":
    main()