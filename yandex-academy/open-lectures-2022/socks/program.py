import os.path

def read_file(file):
    if not os.path.isfile(file):
        print(f'File {file} does not exist')
    elif os.path.getsize(file) == 0:
        print(f'File {file} is empty')
    else:
        with open(file, 'r', encoding='utf-8') as f:
            contents = f.read().split('\n')
            print(f'File "{file}" read successfully')
        return contents

def count_occur(s):
    balance = [0] * (l + 1)
    result = [0] * (l + 1)
    for i in range(n):
        left, right = map(int, s[i].split())
        balance[left - 1] += 1
        balance[right] -= 1
    return balance, result

def calc_thickness(s):
    balance, _ = count_occur(s)
    now = 0
    result = [0] * l
    for i in range(l):
        now = now + balance[i]
        result[i] = now
    for i in range(m):
        query = int(input('Enter point number: ')) - 1
        print(f'Thickness of sock coating: {result[query]}')


l, n, m = map(int, input('Enter L M N numbers: ').split())
data = read_file('socks_ends_data.txt')
calc_thickness(data)