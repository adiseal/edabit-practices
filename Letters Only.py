def letters_only(txt):
	a = ""
	for i in txt:
		if i.isupper() or i.islower():
			a = a + i
		else:
			continue
	return a
    
print(letters_only("R!=:~0o0./c&}9k`60=y")) # "Rocky"