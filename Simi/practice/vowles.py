input_file = open("temp.txt", "w")
print("facetious", file=input_file)
print("acedious", file=input_file)
print("Simex", file=input_file)
input_file.close()

# input_file = open("temp.txt", "r")
# vowels = "aeiou"
# words_vowel = ""
# for char in input_file:
#     if char in vowels:
#         words_vowel += char
#
#     for words in input_file:
#         word = words.strip()
#         if vowels == words_vowel:
#             print(words)
vowels = ["a", "e", "i", "o", "u"]


def vowels_test(word):
    global word_vowels
    word_vowels = []
    wordly = word.strip().lower()
    for letters in wordly:
        if letters in vowels:
            word_vowels.append(letters)
    return word_vowels


input_file = open("temp.txt", "r")
for words in input_file:
    word_vowels = vowels_test(words)
    if word_vowels == vowels:
        print(f"The word {words.strip()} has it's vowel letters arranged")
    else:
        print(f"The word {words.strip()} does not have it's vowel letters arranged")
input_file.close()