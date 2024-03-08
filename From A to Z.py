def gimme_the_letters(s):
    start, end = s.split('-')
    return ''.join(chr(i) for i in range(ord(start), ord(end)+1))