def break_palindrome(s):
    length = len(s)
    if length == 1:
        return ''
    middle_idx = length // 2
    for idx in range(middle_idx):
        if s[idx] != 'a':
            return s[:idx] + 'a' + s[idx + 1:]
    return s[:-1] + 'b'


if __name__ == '__main__':
    s = input('Enter palindrome: ')
    print(f'Broken palindrome: {break_palindrome(s)}')
