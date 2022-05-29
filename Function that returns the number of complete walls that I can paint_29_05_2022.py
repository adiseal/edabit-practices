# a function that returns the number of complete walls that I can paint
# n is the number of square meters I can paint
# w and h are the widths and heights of a single wall in meters
# how_many_walls(100, 4, 5) ➞ 5

def how_many_walls(n, w, h):
	return int(n / (w * h))