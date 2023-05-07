def find_nemo(sentence):
	a = sentence.split(" ")
	if "Nemo" in a:
		return "I found Nemo at " + str(a.index("Nemo")+1) + "!"
	else:
		return "I can't find Nemo :("
        
print(find_nemo("Nemo is me")) # "I found Nemo at 1!"