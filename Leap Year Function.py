def leap_year(year):
	return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    

assert leap_year(1990) == False

assert leap_year(1924) == True

assert leap_year(2021) == False