import math 

dot_decimal = [".4", ".5", ".6", ".7", ".8", ".9"] 
 
def imposter_formula(i, p):
    if i <= 3 and p <= 10:
        being_imposter = str(100 * (i / p))
        split_it = being_imposter[2:4] 
        if split_it in dot_decimal:
            being_imposter = float(being_imposter)
            return str(math.ceil(being_imposter)) + "%"            
        else:
            being_imposter = float(being_imposter)
            return str(math.floor(being_imposter)) + "%"
            
    else:
        return "The player limit is 10 and the imposter count can only go up to 3"
        
        
#assert imposter_formula(1, 10) == "10%"
print(imposter_formula(1, 10))

#assert imposter_formula(2, 5) == "40%"
print(imposter_formula(2, 5))

#assert imposter_formula(1, 8) == "13%"
print(imposter_formula(1, 8))

#assert imposter_formula(3, 7) == "43%"
print(imposter_formula(3,7))
