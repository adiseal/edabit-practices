def dashed(text):
    vowels = 'aeiouAEIOU'
    result = ''
    for char in text:
        if char in vowels:
            result += '-' + char + '-'
        else:
            result += char
    return result