s = input('Etner a string')
words = s.split()
for word in words:
 print(word[0].upper() + word[1:], end = ' ')