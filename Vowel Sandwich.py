def is_vowel_sandwich(s):
    vowels = 'aeiou'
    if len(s) != 3:
        return False
    if s[0] not in vowels and s[2] not in vowels and s[1] in vowels:
        return True
    else:
        return False
