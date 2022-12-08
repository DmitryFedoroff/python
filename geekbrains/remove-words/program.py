def rem_words(text):
    return list(filter(lambda x: 'abc' not in x, text.split()))


my_text = 'Write abc program thabct removes abcll words contabcining'
print(*rem_words(my_text))
