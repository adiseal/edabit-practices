def years_in_one_house(age, moves):
    nb_houses = moves + 1 
	avg_years = round(age / nb_houses)
    return avg_years

assert years_in_one_house(30,1) == 15
assert years_in_one_house(15,2) == 5
assert years_in_one_house(80,0) == 80 
assert years_in_one_house(15,3) == 4
