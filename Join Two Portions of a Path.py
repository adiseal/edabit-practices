def join_path(portion1, portion2):
	return portion1.strip("/") + "/" + portion2.strip("/")
    
    
print(join_path("portion1/", "/portion2"))