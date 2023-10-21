from collections import Counter
import random


def get_integer_input(prompt="Enter an integer: ") -> int:
    while True:
        user_input = input(prompt).strip()
        try:
            return int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def find_unique_values(nums):
    num_counts = Counter(nums)
    return [num for num, count in num_counts.items() if count == 1]


if __name__ == '__main__':
    num_elements = get_integer_input()
    random_nums = [random.randint(1, 10) for _ in range(num_elements)]
    print(*random_nums)
    print(*find_unique_values(random_nums))
