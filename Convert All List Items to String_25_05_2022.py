def parse_list(lst):
	list_string = []
	for i in lst:
	    i = str(i)
	    list_string.append(i)
	return list_string
    
# Example: parse_list(["abc", 123, "def", 456]) ➞ ["abc", "123", "def", "456"]