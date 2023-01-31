def after_n_months(year, month):
    if year == None:
        return "year missing"
    elif month == None:
        return "month missing"
    elif month / 12 > 0:
        return year + int((month / 12))
    elif month / 12 < 0:
        return year + round(month / 12)
    


assert after_n_months(2020, 24) == 2022

assert after_n_months(1832, 2) == 1832

assert after_n_months(1444, 60) == 1449    

