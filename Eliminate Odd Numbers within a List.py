def no_odds(lst):
    return [num for num in lst if num % 2 == 0]
    
print(no_odds([1, 2, 3, 4, 5, 6, 7, 8])) # [2, 4, 6, 8]