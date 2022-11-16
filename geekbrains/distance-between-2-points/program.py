def get_int_input():
    while True:
        try:
            return list(map(int, input().split()))
        except ValueError:
            print("Input value is not integer. Please try again ...")


if __name__ == '__main__':
    a = get_int_input()
    b = get_int_input()
