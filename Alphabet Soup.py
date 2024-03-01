def alphabet_soup(text):
    return ''.join(sorted(text))

print(alphabet_soup("hello")) # "ehllo"
print(alphabet_soup("edabit")) # "abdeit"
print(alphabet_soup("hacker")) # "acehkr"
print(alphabet_soup("geek")) # "eegk"
print(alphabet_soup("javascript")) # "aacijprstv"
print(alphabet_soup("credibility")) # "bcdeiiilrty"
print(alphabet_soup("apostrophe")) # "aehoopprst"
print(alphabet_soup("determination")) # "adeeiimnnortt"
print(alphabet_soup("win")) # "inw"
print(alphabet_soup("synthesis")) # "ehinsssty"