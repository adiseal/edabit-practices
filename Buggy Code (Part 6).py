def remove_numbers(string):
    str1 = ""
    for i in string:
        if i.isalpha():
            str1 = str1 + i
        
    return str1
    


assert remove_numbers("mubashir1") == "mubashir"

assert remove_numbers("12ma23tt") == "matt"

assert remove_numbers("e1d2a3b4i5t6") == "edabit"