import re

def assignment(date_string):
    # Regular expression for yyyy/mm/dd format
    pattern = r'^\d{4}/(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])$'
    
    # Use re.match to check if the date_string matches the pattern
    return bool(re.match(pattern, date_string))