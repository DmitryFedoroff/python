def get_int_input(value):
    while True:
        try:
            s = input(f'{value}')
            return int(s)
        except ValueError:
            print("Input value is not integer. Please try again ...")


def check_day(lst, num):
    if 6 <= num <= 7:
        print(f"Yes, {lst[num - 1]} is weekend")
    elif 0 < num < 6:
        print(f"No, {lst[num - 1]} is weekday")
    else:
        print("Number is outside 7-day week")


if __name__ == '__main__':
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day_num = get_int_input("Enter day number: ")
