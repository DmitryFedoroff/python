def replace_vowels(word):
    return word.lower().translate(str.maketrans("aeuio", "#####"))


def check_spelling(word_list, queries):
    word_set = set(word_list)
    word_lower_map = {word.lower(): word for word in reversed(word_list)}
    word_unvowel_map = {}
    for word in reversed(word_list):
        unvoweled_word = replace_vowels(word)
        word_unvowel_map[unvoweled_word] = word
    return [
        word if word in word_set else
        word_lower_map.get(word.lower(), '') or
        word_unvowel_map.get(replace_vowels(word), '')
        for word in queries
    ]


if __name__ == '__main__':
    num_words = int(input('Enter number of substances in list of desirable substances: '))
    word_list = input('Enter list of desirable substances: ').split()
    num_queries = int(input('Enter number of substances obtained in the reactor: '))
    queries = input('Enter list of substances obtained in the reactor: ').split()
    print('Result:', *check_spelling(word_list, queries))
