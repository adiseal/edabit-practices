def is_boiling(temp):            
        if temp[-1] == "C":
            celcius = int(temp[0:-1])
            return celcius >= 100
        elif temp[-1] == "F":
            fahrenheit = int(temp[0:-1])
            return fahrenheit >= 212




assert is_boiling("212F") == True

assert is_boiling("100C") == True

assert is_boiling("0F") == False

assert is_boiling("212F") == True

assert is_boiling("100C") == True

assert is_boiling("0F") == False

assert is_boiling("-1F") == False

assert is_boiling("213F") == True

assert is_boiling("104C") == True

assert is_boiling("-10F") == False

assert is_boiling("120F") == False