import math

def standard_deviation(lst):    
    mean = sum(lst) / len(lst)
    variance = sum((x - mean) ** 2 for x in lst) / len(lst)    
    std_dev = math.sqrt(variance)    
    return round(std_dev, 2)