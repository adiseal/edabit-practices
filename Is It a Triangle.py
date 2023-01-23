def is_triangle(a, b, c):
	return a + b > c and a + c > b and b + c > a
    
    
assert is_triangle(2, 3, 4) == True

assert is_triangle(3, 4, 5) == True

assert is_triangle(4, 3, 8) == False