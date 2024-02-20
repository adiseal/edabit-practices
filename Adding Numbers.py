def add(n1, n2):
	if (n1 == None or n1 == "") or (n2 == None or n2 == ""):
		return "Invalid Operation"
	return str(int(n1) + int(n2))
    
print(add("91", "19")) # "110"
print(add("123456789", "987654322")) # "1111111111"
print(add("9999999", "1")) # "10000000"
print(add("300", "3000")) # "3300"
print(add("1000", "6200")) # "7200"
print(add("-10", "-20")) # "-30"
print(add("-100", "100")) # "0"
print(add("0", "6200")) # "6200"
print((add("", "6")) # "Invalid Operation"
print(add("", None)) # "Invalid Operation"
print(add(None, "23")) # "Invalid Operation"