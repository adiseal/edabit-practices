def temp_conversion(celsius):
    fahrenheit = round(celsius * 9/5 + 32, 2)
    kelvin = round(celsius + 273.15, 2)
    if kelvin < 0:
        return "Invalid"
    else:
        return [fahrenheit, kelvin]

print(temp_conversion(0)) # [32, 273.15]
print(temp_conversion(100)) # [212, 373.15]