def century_from_year(year):
    return (year + 99) // 100
    
print(century_from_year(2005)) # 21
print(century_from_year(1950)) # 20
print(century_from_year(1900)) # 19