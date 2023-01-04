def match(s1, s2):
    return s1.casefold() == s2.casefold()


assert match("hello", "hELLo") == True

assert match("motive", "emotive") == False

assert match("venom", "VENOM") == True

assert match("mask", "mAskinG") == False    