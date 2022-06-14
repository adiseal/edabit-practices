# Author    : Adi Nugroho
# Date      : Jun/14/2022
# You will need to write three unfinished logic gates. Continue to write the three logic gates: AND, OR, and NOT

def NOT(num):
	if not(num):
	    return 1
	return 0
	
def AND(num,num2):
    if num == 1 and num2 == 1:
        return 1
    return 0

def OR(num,num2):
    if num == 0 and num2 == 0:
        return 0
    return 1

# print(AND(1, 1)) ➞ 1
# print(OR(1, 0)) ➞ 1