# Author    : Adi Nugroho
# Date      : Jun/14/2022
# a function that can turn JPY (Japanese yen) to USD (American dollar)

def yen_to_usd(yen):
    return round(yen / 107.5, 2)
    
print(yen_to_usd(500)) #➞ 4.65