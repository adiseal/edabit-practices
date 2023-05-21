def format_date(date):
	return date[-4:]+date[3:5]+date[0:2]
    
print(format_date("12/31/2019")) # "20193112"