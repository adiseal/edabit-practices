def reverse(txt):
	a = ""
    for x in txt:
        a = x + a
    return a
    
print(reverse("The quick brown fox.")) # ".xof nworb kciuq ehT"