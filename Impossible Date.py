import datetime

def is_valid_date(day, month, year):
    try:
        datetime.datetime(year, month, day)
        return True  
    except ValueError:
        return False  