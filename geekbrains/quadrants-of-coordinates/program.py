import re


def get_num_input():
    s = input()
    if re.match('^-?\\d*(\\.\\d+)?$', s) is None:
        raise ValueError("Input is not numerical. Please try again ...")
    return float(s)


def get_coord_quadrant(x, y):
    if x != 0 and y != 0:
        if x * y > 0:
            q = 'I' if x > 0 else 'III'
        else:
            q = 'II' if x < 0 else 'IV'
    else:
        q = 'OY' if x == 0 else 'OX'
    return q


if __name__ == '__main__':
    px = get_num_input()
    py = get_num_input()

