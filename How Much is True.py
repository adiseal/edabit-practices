def count_true(lst):
	return lst.count(True)
    

assert count_true([True, False, False, True, False]) == 2

assert count_true([False, False, False, False]) == 0

assert count_true([]) == 0