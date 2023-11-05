def get_integer_input(prompt="Enter an integer: ") -> int:
    while True:
        user_input = input(prompt).strip()
        try:
            return int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def check_day(day_number: int):
    if 1 <= day_number <= 5:
        print("No, it's a weekday.")
    elif day_number in (6, 7):
        print("Yes, it's the weekend.")
    else:
        print("The number is outside of a 7-day week.")


if __name__ == '__main__':
    day_num = get_integer_input()
    check_day(day_num)
