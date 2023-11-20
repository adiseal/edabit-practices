def fix_import(s):
    words = s.split()
    return 'from {} import {}'.format(words[3], words[1])
