def break_palindrome(s):
    if len(s) == 1:
        return ''
    middle = len(s) // 2
    flag = False
    for i in range(middle):
        if s[i] != 'a':
            ans = s[:i] + 'a' + s[i+1:]
            flag = True
            break
    if flag:
        return ans
    else:
        return s[:-1] + 'b'

s = input('Enter palindrome: ')