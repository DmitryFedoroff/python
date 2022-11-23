def get_int_input():
    while True:
        try:
            s = input()
            return int(s)
        except ValueError:
            print("Input value is not integer. Please try again ...")


def dec_to_bin(n):
    return n if n in {0, 1} else n % 2 + 10 * dec_to_bin(n // 2)


if __name__ == '__main__':
    num = get_int_input()
    print(dec_to_bin(num))
