def neutralise(s1, s2):
    result = ''
    for c1, c2 in zip(s1, s2):
        if c1 == c2:
            result += c1
        else:
            result += '0'
    return result
