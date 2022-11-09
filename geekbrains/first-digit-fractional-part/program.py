import re


def get_float_input(value):
    s = input(value)
    if re.match(r'[+-]?[0-9]+\.[0-9]+', s) is None:
        raise ValueError("Input is not floating point number. Please try again ...")
    return float(s)


if __name__ == '__main__':
    n = get_float_input("Enter decimal number: ")
