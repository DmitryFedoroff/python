import re


def get_num_input():
    s = input()
    if re.match('^-?\\d*(\\.\\d+)?$', s) is None:
        raise ValueError("Input is not numerical. Please try again ...")
    return float(s)


if __name__ == '__main__':
    px = get_num_input()
    py = get_num_input()

