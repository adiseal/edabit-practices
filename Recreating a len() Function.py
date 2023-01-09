def length(s):
    strlen = 0
    for x in s:
        strlen += 1
    return strlen


assert length("Hello World") == 11

assert length("Edabit") == 6

assert length("wash your hands!") == 16