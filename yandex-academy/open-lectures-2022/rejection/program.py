def unvovel(s):
     s = s.lower()
     for vovel in 'aeuio':
         s = s.replace(vovel, '#')
     return s

dct_len = int(input('Enter number of substances in list of desirable substances: '))
dct = list(input('Enter list of desirable substances: ').split())
txt_len = int(input('Enter number of substances obtained in the reactor: '))
txt = list(input('Enter list of substances obtained in the reactor: ').split())