def get_missing_letters(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return ''.join(sorted(set(alphabet) - set(s)))