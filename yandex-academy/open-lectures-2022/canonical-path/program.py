def canonical_path(path: str) -> str:
    stack = []
    path_parts = path.split('/')
    for part in path_parts:
        if part == '..':
            if stack:
                stack.pop()
        elif part and part != '.':
            stack.append(part)
    return '/' + '/'.join(stack)


if __name__ == '__main__':
    input_path = input('Enter path: ')
    print(f'Canonical path: {canonical_path(input_path)}')