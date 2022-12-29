def accept_into_movie(age, is_supervised):
	return age >= 15 or is_supervised == True
    

assert accept_into_movie(14, True) == True

assert accept_into_movie(14, False) == False

assert accept_into_movie(16, False) == True