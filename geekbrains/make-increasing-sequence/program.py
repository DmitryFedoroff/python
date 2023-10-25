import random


def get_integer_input(prompt="Enter an integer: ") -> int:
    while True:
        user_input = input(prompt).strip()
        try:
            return int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def make_incr_seq(lst):
    max_val = float('-inf')
    for num in lst:
        if num > max_val:
            max_val = num
            yield num


if __name__ == '__main__':
    list_size = get_integer_input("Enter the size of the list: ")
    random_list = [random.randint(1, 10) for _ in range(list_size)]
    print("Original list:", *random_list)
    incr_seq = list(make_incr_seq(random_list))
    print("Increasing sequence:", *incr_seq)
