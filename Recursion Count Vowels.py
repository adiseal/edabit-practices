def vowels(s):
    if s == '':
        return 0
    else:
        return (s[0] in 'aeiou') + vowels(s[1:])
