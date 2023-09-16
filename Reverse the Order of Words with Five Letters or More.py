def reverse(s):
    words = s.split()
    for i in range(len(words)):
        if len(words[i]) >= 5:
            words[i] = words[i][::-1]
    return ' '.join(words)

print(reverse("Reverse")) # "esreveR"
print(reverse("This is a typical sentence.")) # "This is a lacipyt .ecnetnes"