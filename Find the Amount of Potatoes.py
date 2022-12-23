def potatoes(potato):
    return potato.count("potato")
    
assert potatoes("potato") == 1

assert potatoes("potatopotato") == 2

assert potatoes("potatoapple") == 1