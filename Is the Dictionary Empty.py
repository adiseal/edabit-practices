def is_empty(dictionary):
	return len(dictionary) == 0
    

assert is_empty({}) == True

assert is_empty({ "a": 1 }) == False
