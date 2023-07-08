def add(n1, n2):
	if n1 == "" or n2 == "":
		return "Invalid Operation"
	return int(n1)+int(n2)
    
print(add("10", "80")) # "90"
print(add("111", "111")) # "222
print(add("", "20")) # "Invalid Operation"