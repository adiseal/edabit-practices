def create_id(firstname, lastname):
    first_letter = firstname[0]
    three_first_lettter = lastname[0:3]
    capitalize = three_first_lettter.capitalize()
    lower = first_letter.lower()
    ids = lower + capitalize
    return ids    
	

print(create_id("John", "SMITH"))    
assert create_id("mary", "lamb") == "mLam"
assert create_id("John", "SMITH") == "jSmi"
assert create_id("mary", "smith") == "mSmi"