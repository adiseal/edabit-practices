# Author    : Adi Nugroho
# Date      : Jun/14/2022
# a function that takes a list of numbers lst and returns an inverted list

def invert_list(lst):
	return [ -i for i in lst ]

# print(invert_list([1, -2, 3, -4, 5])) ➞ [-1, 2, -3, 4, -5]