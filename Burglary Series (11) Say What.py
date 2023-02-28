def say_what(obj):
	val = ""
	for x, y in obj.items():
		val = val + y + " "
	return val + obj[2]
    
print(say_what({ 1: "Mommy", 2: "please", 3: "help" })) # ➞ "Mommy please help please"