def flip(txt, spec):
    if spec == "word":
        return ' '.join(word[::-1] for word in txt.split(' '))
    elif spec == "sentence":
        return ' '.join(txt.split(' ')[::-1])
    else:
        return txt
