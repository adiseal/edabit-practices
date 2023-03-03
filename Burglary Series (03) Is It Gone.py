def find_it(items, name):
    for x, y in items.items():
        if x == name:
            return name + " is gone..."
    else:
        return name + " is here!"
        
print(find_it({"tv": 30, "timmy": 20, "stereo": 50,},"timmy"))