word_1 = input('Enter a word 1: ').lower()
word_2 = input('Enter a word 2: ').lower()
word_1= sorted(word_1)
word_2 = sorted(word_2)

if (word_1 == word_2):
    print('anagram')
else:
    print('not anagram')