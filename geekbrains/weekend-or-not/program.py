def get_int_input(value):
    while True:
        try:
            s = input(f"{value}")
            return int(s)
        except ValueError:
            print("Input value is not integer. Please try again ...")



if __name__ == '__main__':
    day_num = get_int_input("Enter day number: ")
