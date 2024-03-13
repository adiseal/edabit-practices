def extend_vowels(word, num):
    if not isinstance(num, int) or num < 0:
        return "invalid"
    vowels = 'aeiouAEIOU'
    return ''.join([char * (num + 1) if char in vowels else char for char in word])
