def clone(lst):
	lst = lst +[lst]
	return lst
    
print(clone(["x", "y"])) # ["x", "y", ["x", "y"]] 