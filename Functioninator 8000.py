def inator_inator(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if word[-1].lower() in vowels:
        return word + '-inator ' + str(len(word)*1000)
    else:
        return word + 'inator ' + str(len(word)*1000)

print(inator_inator("Shrink")) # "Shrinkinator 6000"
print(inator_inator("Doom")) # "Doominator 4000"