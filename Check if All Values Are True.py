# Author    : Adi Nugroho
# Date      : Jun/13/2022
# a function that returns True if all parameters are truthy, and False otherwise

def all_truthy(*args):
	return all(args)
	
# print(all_truthy(True, False, True)) ➞ False
# print(all_truthy(5, 4, 3, 2, 1, 0)) ➞ False