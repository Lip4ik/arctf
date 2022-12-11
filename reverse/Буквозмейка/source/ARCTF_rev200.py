def get_char_code_at_position(symbol, position):
    return symbol[position - 1]

def main():
    flag = input('Enter flag to check: ')
    if len(flag) != 16:
        print("Wrong length!\n")
        return 0
    if get_char_code_at_position(flag, 6) != chr(123):
        print('Wrong check 1!\n"')
        return 0
    if get_char_code_at_position(flag, 4) != chr(116):
        print('Wrong check 2!\n"')
        return 0
    if get_char_code_at_position(flag, 1) != chr(97):
        print('Wrong check 3!\n"')
        return 0
    if get_char_code_at_position(flag, 13) != chr(97):
        print('Wrong check 4!\n"')
        return 0
    if get_char_code_at_position(flag, 7) != chr(103):
        print('Wrong check 5!\n"')
        return 0
    if get_char_code_at_position(flag, 9) != chr(111):
        print('Wrong check 6!\n"')
        return 0
    if get_char_code_at_position(flag, 2) != chr(114):
        print('Wrong check 7!\n"')
        return 0
    if get_char_code_at_position(flag, 5) != chr(102):
        print('Wrong check 8!\n"')
        return 0
    if get_char_code_at_position(flag, 16) != chr(125):
        print('Wrong check 9!\n"')
        return 0
    if get_char_code_at_position(flag, 11) != chr(95):
        print('Wrong check 10!\n"')
        return 0
    if get_char_code_at_position(flag, 14) != chr(115):
        print('Wrong check 11!\n"')
        return 0
    if get_char_code_at_position(flag, 3) != chr(99):
        print('Wrong check 12!\n"')
        return 0
    if get_char_code_at_position(flag, 15) != chr(101):
        print('Wrong check 13!\n"')
        return 0
    if get_char_code_at_position(flag, 12) != chr(99):
        print('Wrong check 14!\n"')
        return 0
    if get_char_code_at_position(flag, 8) != chr(111):
        print('Wrong check 15!\n"')
        return 0
    if get_char_code_at_position(flag, 10) != chr(100):
        print('Wrong check 16!\n"')
        return 0
    print(f"Yes! Correct flag is {flag}\n")
    return 0
if __name__ == "__main__":
    main()