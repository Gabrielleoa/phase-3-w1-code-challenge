def constant_value(word):
    return sum(ord(char) - ord('a') + 1 for char in word)

consonants = []
current_word=''

for char in word :
    if char not in 'aeiou':
        current_word += char
    else:
        if current_word:
            consonants.append(constant_value(current_word))
            current_word=''

if current_word:
    consonants.append(constant_value(current_word))

print(max(current_word, defualt=0))

