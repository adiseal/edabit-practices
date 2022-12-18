def create_id(firstname, lastname):
	return firstname[0].lower() + lastname[0:3].capitalize()
    

print(create_id("John", "SMITH"))    
assert create_id("mary", "lamb") == "mLam"
assert create_id("John", "SMITH") == "jSmi"
assert create_id("mary", "smith") == "mSmi"