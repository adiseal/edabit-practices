def sum_of_vowels(s):
    vowels = {'a': 4, 'e': 3, 'i': 1, 'o': 0, 'u': 0}
    return sum(vowels.get(i.lower(), 0) for i in s)