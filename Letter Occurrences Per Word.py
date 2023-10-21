def find_occurrences(txt, ch):
    txt = txt.lower()
    ch = ch.lower()
    words = txt.split()
    return {word: word.count(ch) for word in words}
