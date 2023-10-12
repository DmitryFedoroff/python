def find_path(target_file, num_entries):
    current_path = []
    for _ in range(num_entries):
        entry_with_spaces = input('Enter < filename.* > or < directory > name: ')
        num_spaces = len(entry_with_spaces) - len(entry_with_spaces.lstrip())
        entry = entry_with_spaces.strip()
        current_path = current_path[:num_spaces]
        current_path.append(entry)
        if entry == target_file:
            return '/' + '/'.join(current_path)


if __name__ == '__main__':
    query_file = input('Enter file name: ')
    total_entries = int(input('Enter total number of files and directories: '))
    result = find_path(query_file, total_entries)
    print(f'Path to file: {result}')
