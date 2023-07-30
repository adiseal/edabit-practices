def is_anagram(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    s1 = ''.join(sorted(s1))
    s2 = ''.join(sorted(s2))
    return s1 == s2
