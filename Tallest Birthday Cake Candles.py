# Author    : Adi Nugroho
# Date      : Jun/13/2022
# Count how many candles are tallest

def birthday_cake_candles(candles):
    tallest = max(candles)
    return candles.count(tallest)
	
# print(birthday_cake_candles([3, 2, 1, 3])) ➞ 2
# print(birthday_cake_candles([82, 49, 82, 82, 41, 82, 15, 63, 38, 25])) ➞ 4