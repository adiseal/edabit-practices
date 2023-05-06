def grab_city(txt):
    a = txt[::-1]
    return a[a.index("[")-1:a.index("]"):-1]
    
print(grab_city("[Last Day!] Beer Festival [Munich]")) # "Munich"