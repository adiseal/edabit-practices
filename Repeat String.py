# Author    : Adi Nugroho
# Date      : Jun/14/2022
# a function that takes a string txt and a number n and returns the repeated string n number of times

def repeat_string(txt, n):
    if type(txt) != str:
        return "Not A String !!"
    else:
        return txt * n    

# print(repeat_string(1990, 7)) ➞ "Not A String !!"
# print(repeat_string("Mubashir", 2))  ➞ "MubashirMubashir"