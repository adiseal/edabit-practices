# Author        -> Adi Nugroho
# Date created  -> May/30/2022

# Python 3 code to demonstrate 
# check if two lists are identical
# using collections.Counter()
# as an alternative of using "identical operator (==)"

import collections

def check_equals(lst1, lst2):
	return collections.Counter(lst1) == collections.Counter(lst2)
	
# print(check_equals([4, 5, 6], [4, 5])) --> False