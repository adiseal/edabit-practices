import math

def darts_scoring(x, y):
    # Calculate the distance from the origin (0, 0) using the Pythagorean theorem
    distance = math.sqrt(x**2 + y**2)
    
    if distance > 10:
        return 0
    elif distance > 5:
        return 1
    elif distance > 1:
        return 5
    else:
        return 10
        
print(darts_scoring(0, 0)) # 10
