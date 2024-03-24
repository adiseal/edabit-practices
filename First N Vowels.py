def first_n_vowels(s, n):
    vowels = 'aeiou'
    result = [char for char in s if char in vowels][:n]
    return ''.join(result) if len(result) == n else 'invalid'