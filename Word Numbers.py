def word(s):
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
    
    return myDict.get(s)


   
assert word("one") == 1

assert word("two") == 2

assert word("nine") == 9