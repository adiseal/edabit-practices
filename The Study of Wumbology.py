def wumbo(words):
	return words.replace("M","W")
    

assert wumbo("I LOVE MAKING CHALLENGES") == "I LOVE WAKING CHALLENGES"

assert wumbo("MEET ME IN WARSAW") == "WEET WE IN WARSAW"

assert wumbo("WUMBOLOGY") == "WUWBOLOGY"