def build(n):
    now_in_step = 1
    steps = 0
    while n >= now_in_step:
        n -= now_in_step
        steps += 1
        now_in_step += 1
    return steps

n = int(input('Enter number of blocks: '))
print(f'Maximum number of steps in staircase: {build(n)}')
print('\n'.join('□ ' * i for i in range(1, build(n) + 1)))