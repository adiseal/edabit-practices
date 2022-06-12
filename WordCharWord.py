# Author    : Adi Nugroho
# Date      : Jun/12/2022
# a function that will put the first argument, a character, 
# between every word in the second argument, a string.

def add(char, txt):
	if txt == "":
		return char
	return txt.replace(" ", char)