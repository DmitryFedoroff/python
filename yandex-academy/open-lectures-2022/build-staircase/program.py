def calculate_steps(block_count):
    step, remaining_blocks = 1, block_count
    while remaining_blocks >= step:
        remaining_blocks -= step
        step += 1
    return step - 1


def print_staircase(block_count):
    step, blocks_in_step = 1, 0
    for _ in range(block_count):
        print("\u25A1", end=" ")
        blocks_in_step += 1
        if blocks_in_step == step:
            print()
            step += 1
            blocks_in_step = 0


if __name__ == '__main__':
    block_count = int(input('Enter number of blocks: '))
    print(f'Maximum number of steps in staircase: {calculate_steps(block_count)}')
    print_staircase(block_count)
