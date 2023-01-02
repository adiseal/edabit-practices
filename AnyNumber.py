def numbers(n):
    myDict = {
        "one" : 1,
        "two" : 2,
        "three" : 3,
        "four" : 4,
        "five" : 5,
        "six" : 6,
        "seven" : 7,
        "eight" : 8,
        "nine" : 9, 
        "zero" : 0
    }
    
    for key, value in myDict.items():
        if n == value:
            return key
    


assert numbers(1) == "one"

assert numbers(2) == "two"

assert numbers(9) == "nine"