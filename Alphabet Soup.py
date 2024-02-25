def alphabet_soup(text):
    return ''.join(sorted(text))

print(alphabet_soup("hello")) # "ehllo"
print(alphabet_soup("edabit")) # "abdeit"