import re


def get_int_input(prompt="Enter a natural number: "):
    int_pattern = re.compile(r'^[1-9]\d*$')
    while True:
        user_input = input(prompt).strip()
        if int_pattern.fullmatch(user_input):
            return int(user_input)
        print("Invalid input. Please enter a natural number.")


def find_prime_factors(number):
    factors = []
    divisor = 2
    while number >= divisor:
        while number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        divisor += 1
    return factors


if __name__ == '__main__':
    num = get_int_input("Enter a number to find its prime factors: ")
    prime_factors = find_prime_factors(num)
    print(f'Prime factors of the number {num}: {prime_factors}')
