def n_sided_shape(n):
    thisdict = {
        1:"circle",
        2:"semi-circle",
        3:"triangle",
        4:"square",
        5:"pentagon",
        6:"hexagon", 
        7:"heptagon", 
        8:"octagon",
        9:"nonagon",
        10:"decagon"
    }
    return thisdict[n]
    
    
assert n_sided_shape(3) == "triangle"

assert n_sided_shape(1) == "circle"

assert n_sided_shape(9) == "nonagon"