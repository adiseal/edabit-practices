def leap_year(year):
    return year % 4 == 0 and year % 100 != 0

 

assert leap_year(1900) == False 

assert leap_year(2024) == True 

assert leap_year(1968) == True 

assert leap_year(2020) == True  
