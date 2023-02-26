def who_wins_tonight(coins, space, price, size):
    if int(space/size) == int(coins/price):
        return "Tie"
    elif int(space/size) < int(coins/price):
        return "Bill"
    else:
        return "Will"

print(who_wins_tonight(20, 20, 5, 10)) #➞ "Bill"