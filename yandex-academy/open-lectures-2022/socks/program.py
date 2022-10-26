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

l, n, m = map(int, input('Enter L M N numbers: ').split())
