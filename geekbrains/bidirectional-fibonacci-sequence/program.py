import re


def get_int_input(prompt="Enter a non-negative integer: "):
    int_pattern = re.compile(r'\d+')
    while True:
        user_input = input(prompt).strip()
        if int_pattern.fullmatch(user_input):
            return int(user_input)
        print("Invalid input. Please enter a non-negative integer.")


def generate_fibonacci(n):
    fib_seq = [0, 1]
    for i in range(2, n + 1):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    negafib_seq = [(-1)**(i + 1) * fib for i, fib in enumerate(fib_seq)]
    return negafib_seq[::-1] + fib_seq[1:]


if __name__ == '__main__':
    num = get_int_input("Enter the number of Fibonacci elements: ")
    fibonacci_list = generate_fibonacci(num)
    print(f"Fibonacci sequence with positive and negative indices: {fibonacci_list}")
