def remove_first_last(txt):
	return txt[1:-1] if len(txt) >= 3 else txt


assert remove_first_last("hello") == "ell"

assert remove_first_last("maybe") == "ayb"

assert remove_first_last("benefit") == "enefi"

assert remove_first_last("a") == "a"