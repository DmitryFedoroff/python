def get_canonical_path(path: str) -> str:
    flag = True
    path += '/'
    while flag:
        if '/./' in path:
            path = path.replace('/./', '/')
        elif '//' in path:
            path = path.replace('//', '/')
        elif '/../' in path:
            pos = path.find('/../')
            if pos == 0:
                path = path[3:]
            else:
                prev_slash_pos = path.rfind('/', 0, pos - 1)
                path = path[:prev_slash_pos] + path[pos + 3:]
        else:
            flag = False
    if path.endswith('/') and path != '/':
        path = path[:-1]
    return path

s = input('Enter path: ')