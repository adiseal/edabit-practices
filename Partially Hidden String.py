def partially_hide(phrase):
    words = phrase.split()
    for i in range(len(words)):
        if len(words[i]) > 2:
            words[i] = words[i][0] + '-'*(len(words[i])-2) + words[i][-1]
    return ' '.join(words)
