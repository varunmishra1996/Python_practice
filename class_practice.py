# name = input("Enter String")
# count = 0
# for i in name.lower():
#     if i in ('a','e','i','o','u') :
#         count = count+1
# print(count)



# name = input("Enter the string:")
# name = name.strip().lower()
#
# if name == name[::-1]:
#      print('palindrome')
# else:
#     # print('not a palidrome')


word_1 = input('Enter a word 1: ').lower()
word_2 = input('Enter a word 2: ').lower()
word_1= sorted(word_1)
word_2 = sorted(word_2)

if (word_1 == word_2):
    print('anagram')
else:
    print('not anagram')











