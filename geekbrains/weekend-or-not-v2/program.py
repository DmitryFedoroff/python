def get_integer_input(prompt="Enter an integer: ") -> int:
    while True:
        user_input = input(prompt).strip()
        try:
            return int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def check_day(day_number: int):
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    if 1 <= day_number <= 5:
        print(f"No, {weekdays[day_number - 1]} is a weekday")
    elif 6 <= day_number <= 7:
        print(f"Yes, {weekdays[day_number - 6]} is a weekend")
    else:
        print("Number is outside 7-day week")


if __name__ == '__main__':
    day_num = get_integer_input()
    check_day(day_num)
