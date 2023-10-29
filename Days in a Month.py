import calendar

def day_amount(month, year):
    return calendar.monthrange(year, month)[1]
    
print(day_amount(2, 2018)) # 28