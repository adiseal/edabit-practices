# Author    : Adi Nugroho
# Date      : Jun/14/2022
# a function that takes a number n and returns the nth even number beginning with 0 as the first

def nth_even(n):
	max_even = 2 * n # max_even => 200
	num = 0 # num => 0
	while(num < max_even): # True
	    num += 2
	return num - 2
	    
# print(nth_even(1)) ➞ 0
# print(nth_even(100)) ➞ 198