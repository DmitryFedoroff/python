import random


def get_integer_input(prompt="Enter an integer: ") -> int:
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def sum_odd_indices_elements(numbers) -> int:
    return sum(numbers[i] for i in range(1, len(numbers), 2))


if __name__ == '__main__':
    num_elements = get_integer_input("Enter the number of elements: ")
    elements = (random.randint(1, 10) for _ in range(num_elements))
    elements_list = list(elements)
    print(*elements_list)
    print(sum_odd_indices_elements(elements_list))
