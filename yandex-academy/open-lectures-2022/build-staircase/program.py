def build(n):
    now_in_step = 1
    steps = 0
    while n >= now_in_step:
        n -= now_in_step
        steps += 1
        now_in_step += 1
    return steps


def print_staircase(n):
    now_in_step = 1
    blocks = 0
    for i in range(1, n + 1):
        print("\u25A1", end=" ")
        blocks += 1
        if blocks == now_in_step:
            print()
            now_in_step += 1
            blocks = 0


n = int(input('Enter number of blocks: '))
print(f'Maximum number of steps in staircase: {build(n)}')
print_staircase(n)