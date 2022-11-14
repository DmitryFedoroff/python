def get_int_input(value):
    while True:
        try:
            s = input(value)
            return int(s)
        except ValueError:
            print("Input value is not integer. Please try again ...")


def check_day(num):
    if 6 <= num <= 7:
        print("Yes, it's weekend")
    elif 0 < num < 6:
        print("No, it's weekday")
    else:
        print("Number is outside 7-day week")


if __name__ == '__main__':
    day_num = get_int_input()
    check_day(day_num)
