def back_to_home(directions):
	return len(directions) >= 8
    
    
assert back_to_home("EEWE") == False

assert back_to_home("NENESSWW")  == True

assert back_to_home("NEESSW") == False

