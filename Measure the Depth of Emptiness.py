def measure_the_depth(lst):
	return str(lst).count("[")



assert measure_the_depth([]) == 1

assert measure_the_depth([[]]) == 2

assert measure_the_depth([[[]]]) == 3

assert measure_the_depth([[[[[[[[[[[]]]]]]]]]]]) == 11