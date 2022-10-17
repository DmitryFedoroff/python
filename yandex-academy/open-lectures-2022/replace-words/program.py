def replace_words(dict_set):
    result = []
    for word in input('Enter words of text: ').split():
        for i in range(1, min(101, len(word))):
            part = word[:i]
            if part in dict_set:
                result.append(part)
                break
        else:
            result.append(word)
    return result

dict_set = set(input('Enter words from dictionary: ').split())