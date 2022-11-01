def find_path(query, n):
    now_path = []
    for i in range(n):
        line = input('Enter <␣␣filename.*> or <␣directory> name: ')
        now_file = line.strip()
        spaces = 0
        while (spaces < len(line)) and (line[spaces] == ' '):
            spaces += 1
        now_path = now_path[:spaces]
        now_path.append(now_file)
        if now_file == query:
            return '/' + '/'.join(now_path)

query = input('Enter file name: ')
n = int(input('Enter total number of files and directories: '))
