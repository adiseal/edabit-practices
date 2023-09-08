def first_non_repeated_character(s):
    for c in s:
        if s.count(c) == 1:
            return c
    return False

print(first_non_repeated_character("g")) # "g"
print(first_non_repeated_character("it was then the frothy word met the round night")) # "a"
print(first_non_repeated_character("the quick brown fox jumps then quickly blows air")) # "f"