from datetime import date

def get_days(date1, date2):
    delta = date2 - date1
    return delta.days