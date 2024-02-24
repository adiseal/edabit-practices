def consonants(word):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    return sum(1 for char in word if char in consonants)

def vowels(word):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in word if char in vowels)
