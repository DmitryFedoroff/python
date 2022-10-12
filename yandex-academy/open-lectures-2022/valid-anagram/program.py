is_anagram = lambda s, t: sorted(s) == sorted(t)

s = input('Enter 1st string: ')
t = input('Enter 2nd string: ')

if is_anagram:
    print('Yes')
else:
    print('No')
