def is_palindrome(s):
    return s == s[::-1]

def palindromic_date(date):
    day, month, year = date.split('/')    
    ddmmyyyy = day + month + year
    mmddyyyy = month + day + year
    return is_palindrome(ddmmyyyy) and is_palindrome(mmddyyyy)