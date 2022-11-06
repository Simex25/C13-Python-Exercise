s = "I want two things in life, loving you and to be loved by you"

print(s.find("you"))
print(s.index("you"))
print(s.rfind("you"))
print(s.rindex("you"))

import string

# word = input("Enter a word")
# key = int(input("Enter the key to code with"))
# abc = string.ascii_lowercase
# print(abc.replace("a","s",2))
b = "My name is simbi"
print(b.replace("m", "i", 1))
print(b[:5] + 'y' + b[6:])
river = 'mississippi'
target = input("Enter a character")
for index in range(len(river)):
    if river[index] == target:
        print("Letter found at index", index)

else:
    print('Letter', target, 'not found in', river)


def palindrome():
    palindromes = (input('Enter word: '))
    palin = palindromes[::-1]
    if palin == palindromes:
        print(palindromes, "is a palindrome")

    else:
        print(palindromes, "is not a palindrome")


palindrome()
