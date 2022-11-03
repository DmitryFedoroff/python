def unvovel(s):
     s = s.lower()
     for vovel in 'aeuio':
         s = s.replace(vovel, '#')
     return s
     
def check_spelling(wordlist, queries):
    dct = set()
    dct_lower = {}
    dct_unvovel = {}
    for word in wordlist:
        dct.add(word)
        if word.lower() not in dct_lower:
            dct_lower[word.lower()] = word
        unvoveled = unvovel(word)
        if unvoveled not in dct_unvovel:
            dct_unvovel[unvoveled] = word
    result = []
    for word in queries:
        if word in dct:
            result.append(word)
        elif word.lower() in dct_lower:
            result.append(dct_lower[word.lower()])
        elif unvovel(word) in dct_unvovel:
            result.append(dct_unvovel[unvovel(word)])
        else:
            result.append('')
    return result

dct_len = int(input('Enter number of substances in list of desirable substances: '))
dct = list(input('Enter list of desirable substances: ').split())
txt_len = int(input('Enter number of substances obtained in the reactor: '))
txt = list(input('Enter list of substances obtained in the reactor: ').split())
