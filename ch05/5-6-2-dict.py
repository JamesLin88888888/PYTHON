word = 'elephant'

word_count = {letter : word.count(letter) for letter in set(word)}
for w in word_count:
    print(w,word_count[w])
print(word_count)
    
my_dict = {}
for letter in set(word):
    my_dict[letter] = word.count(letter)
print(my_dict)