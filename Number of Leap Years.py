def is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False

def num_of_leapyears(years):
    start, end = map(int, years.split("-"))
    count = sum(1 for year in range(start, end + 1) if is_leap_year(year))
    return count