def reverse_psychology(s):
    a = "Do Not"
    if a in s:
        return s[7:len(s)]
    else:
        return "Do not " + s[:] + "."
        
print(reverse_psychology("eat your lunch")) # "Do not eat your lunch."