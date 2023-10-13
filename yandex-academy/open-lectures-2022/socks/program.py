def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read().strip().split('\n')
    except FileNotFoundError:
        print(f'File {file_path} does not exist')
        return []
    except OSError:
        print(f'An error occurred while reading {file_path}')
        return []


def calculate_thickness(socks_data, length, num_queries):
    balance = [0] * (length + 1)
    for left, right in socks_data:
        balance[left] += 1
        balance[right] -= 1
    thickness = 0
    result = [0] * length
    for i in range(length):
        thickness += balance[i]
        result[i] = thickness
    for _ in range(num_queries):
        query = int(input('Enter point number: ')) - 1
        print(f'Thickness of sock coating: {result[query]}')


if __name__ == '__main__':
    length, num_segments, num_queries = map(int, input('Enter L, N, M: ').split())
    socks_data = [(int(x.split()[0]) - 1, int(x.split()[1])) for x in read_file('socks_ends_data.txt')]
    calculate_thickness(socks_data, length, num_queries)
