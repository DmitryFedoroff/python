def remove_words_with_abc(text):
    return ' '.join(word for word in text.split() if 'abc' not in word)


if __name__ == '__main__':
    my_text = 'Write abc program thabct removes abcll words contabcining'
    result = remove_words_with_abc(my_text)
    print(result)
