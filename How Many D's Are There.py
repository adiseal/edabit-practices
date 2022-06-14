# Author    : Adi Nugroho
# Date      : Jun/14/2022
# a function that counts how many D's are in a sentence

def count_d(sentence):
    substring = sentence.lower()
    count = substring.count("d")
    return count

# print(("My friend Dylan got distracted in school.")) ➞ 4