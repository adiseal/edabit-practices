def sort_by_last(s):
    return ' '.join(sorted(s.split(), key=lambda word: word[-1]))