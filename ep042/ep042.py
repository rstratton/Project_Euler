def t(n):
    return (n*(n+1))//2

def letter_num(letter):
    return ord(str.lower(letter)) - ord('a') + 1

def triang_dict(n):
    triang_dict = {}
    for i in range(1, n):
        triang_dict[t(i)] = 0
    return triang_dict

DICT = triang_dict(100000)

def is_triang(n, d):
    if n in d:
        return True
    else:
        return False

def word_to_num(word):
    total = 0
    for letter in word:
        total += letter_num(letter)
    return total

file = open("words.txt")
words = [word[1:-1] for word in file.read().split(',')]
count = 0
for word in words:
    if is_triang(word_to_num(word), DICT):
        count += 1
print(count)
    
