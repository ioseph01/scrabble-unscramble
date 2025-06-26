from collections import Counter

letters = 'tabind'

word_dict = {}
char_dict = Counter(letters)

with open('words.txt') as f:
    for l in f:
        l = l.strip('\n')
        if len(l) not in word_dict:
            word_dict[len(l)] = [l]
        else:
            word_dict[len(l)].append(l)
            

for i in word_dict:
    if i <= len(letters):
        _ = True
        for word in word_dict[i]:
            if len(Counter(word) - char_dict) == 0:
                if _ :
                    print(i)
                print('\t',word)
                _ = False

    else:
        break
            
                
            
