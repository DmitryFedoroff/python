def is_anagram(string1, string2):
    return set(string1) == set(string2) and all(string1.count(char) == string2.count(char) for char in set(string1))


def main():
    str1 = input('Enter 1st string: ')
    str2 = input('Enter 2nd string: ')
    message = 'Yes' if is_anagram(str1, str2) else 'No'
    print(message)


if __name__ == '__main__':
    main()
