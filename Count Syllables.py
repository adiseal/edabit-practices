def number_syllables(word):
	return len(word.split("-"))
    

assert number_syllables("buf-fet") == 2

assert number_syllables("beau-ti-ful") == 3

assert number_syllables("mon-u-men-tal") == 4

assert number_syllables("on-o-mat-o-poe-ia") == 6