import re


def get_float_input(prompt: str = "Enter the precision (e.g., 0.001): ") -> float:
    float_pattern = re.compile(r'^0\.0*1$')
    while True:
        user_input = input(prompt).strip()
        if float_pattern.fullmatch(user_input):
            return float(user_input)
        print("Invalid input. Please enter a valid precision (e.g., 0.001).")


def calculate_pi_to_precision(precision):
    pi_estimate = 0
    k = 1
    for i in range(int(1 / precision)**2):
        if i % 2 == 0:
            pi_estimate += 4 / k
        else:
            pi_estimate -= 4 / k
        k += 2
    return pi_estimate
