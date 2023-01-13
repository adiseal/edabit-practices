def get_fillings(sandwich):
	return sandwich[1:-1]
    
    
assert get_fillings(["bread", "ham", "cheese", "ham", "bread"]) == ["ham", "cheese", "ham"]

assert get_fillings(["bread", "sausage", "tomato", "bread"]) == ["sausage", "tomato"]

assert get_fillings(["bread", "lettuce", "bacon", "tomato", "bread"]) == ["lettuce", "bacon", "tomato"]