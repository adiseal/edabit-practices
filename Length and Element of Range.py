def length_element(r, i):
	return [len(r), r[i]]


assert length_element(range(2, 4), 0) == [2, 2]

assert length_element(range(12, 15, 2), 1) == [2, 14]

assert length_element(range(40, 50, 3), 2) == [4, 46]