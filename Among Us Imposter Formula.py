import math 

def imposter_formula(i, p):
    if i <= 3 and p <= 10:
        being_imposter = math.ceil((100 * (i / p)))
        rounded_number = str(being_imposter)
        return rounded_number + "%"
    else:
        return "The player limit is 10 and the imposter count can only go up to 3"
        
        
assert imposter_formula(1, 10) == "10%"
#print(imposter_formula(1, 10))

assert imposter_formula(2, 5) == "40%"
#print(imposter_formula(2, 5))

assert imposter_formula(1, 8) == "13%"
#print(imposter_formula(1, 8))