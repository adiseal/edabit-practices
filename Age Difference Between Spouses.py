def age_difference(ages):
    ages = sorted(ages)
    result = ages[-1] - ages[-2] 
    if result > 1:
        return str(result) + " years"
    elif result == 0:
        return "No age difference between spouses."
    else:
        return str(result) + " year"
        


assert age_difference([29, 1, 6, 8, 28]) == "1 year"

assert age_difference([43, 86, 49, 86]) == "No age difference between spouses."

assert age_difference([2, 4, 6, 32, 27]) == "5 years"    