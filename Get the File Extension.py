def get_extension(lst):
    ext = []
    for x in lst:
        x = x.split(".")
        ext.append(x[1])
    return ext 

print(get_extension(["code.html", "code.css"])) #➞ ["html", "css"]
        
        
        