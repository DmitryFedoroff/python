import math


def get_coordinate_list(prompt="Enter coordinates: ") -> list:
    while True:
        user_input = input(prompt).strip()
        try:
            return list(map(int, user_input.split()))
        except ValueError:
            print("Invalid input. Please enter valid integers.")


def calculate_euclidean_distance(point1: list, point2: list) -> float:
    return round(math.sqrt(sum((x - y) ** 2 for x, y in zip(point1, point2))), 2)


if __name__ == '__main__':
    first_point = get_coordinate_list("Enter the x and y coordinates of the point a: ")
    second_point = get_coordinate_list("Enter the x and y coordinates of the point b: ")
    print(calculate_euclidean_distance(first_point, second_point))
