def replace_words(dictionary, text):
    words = text.split()
    for index, word in enumerate(words):
        for i in range(1, min(101, len(word) + 1)):
            if word[:i] in dictionary:
                words[index] = word[:i]
                break
    return words


if __name__ == '__main__':
    dictionary = set(input('Enter words from dictionary: ').split())
    text = input('Enter words of text: ')
    print('Text with replacements:', ' '.join(replace_words(dictionary, text)))
