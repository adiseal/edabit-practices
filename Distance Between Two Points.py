def get_distance(a, b):
    aq = []
    aw = []
    for k,v in a.items():
        aq = aq + [v]
    for k,v in b.items():
        aw =aw + [v]
    return round(((aq[0]-aw[0])**2+ (aq[1]-aw[1])**2)**(1/2),3)
    
print(get_distance({"x": 10, "y": -5}, {"x": 8, "y": 16})) # 21.095