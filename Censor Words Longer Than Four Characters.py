def censor(s):
    return ' '.join(len(i) > 4 and '*' * len(i) or i for i in s.split())
