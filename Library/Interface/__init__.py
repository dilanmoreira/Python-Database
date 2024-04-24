def readInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERROR! PLEASE, ENTER AN AVAILABLE INTEGRAL NUMBER.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mThe user did not enter a number.\033[m')
            return 0
        else:
            return n


def line(size=42):
    return '-' * size


def header(txt):
    print(line())
    print(txt.center(42))
    print(line())


def menu(list):
    header('MAIN MENU')
    c = 1
    for item in list:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(line())
    opt = readInt('\033[32mYour option: \033[m')
    return opt
