def reverse_odd(s):
    words = s.split(' ')
    for i in range(len(words)):
        if len(words[i]) % 2 != 0:
            words[i] = words[i][::-1]
    return ' '.join(words)