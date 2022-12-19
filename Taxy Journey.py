def journey_distance(cost): 
    kms = cost - 3 
    distance = int((kms / 2) + 1)     
    return distance
    
assert journey_distance(3) == 1
# The first kilometer costs $3

assert journey_distance(9) == 4
# The first kilometer costs $3 plus the other three kilometers (costing $2 each)

assert journey_distance(7) == 3