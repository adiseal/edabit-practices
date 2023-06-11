def is_between(first, last, word):
    words = [first, last, word]
    words.sort()
    return words[1] == word
	
print(is_between("apple", "banana", "azure")) # True