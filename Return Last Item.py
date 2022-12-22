def last_ind(lst):
	#not_empty = len(lst)
    if len(lst) != 0:
        return lst[-1]
    else:
        return None

assert last_ind([0, 4, 19, 34, 50, -9, 2]) == 2

assert last_ind("The quick brown fox jumped over the lazy dog") == "g"

assert last_ind([]) == None