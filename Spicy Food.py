def bill_split(spicy, prices):
  your_pay = 0
  friend_pay = 0
  for i in range(len(spicy)):
    if spicy[i] == "S":
      your_pay += prices[i]
    else:
      your_pay += prices[i] / 2
      friend_pay += prices[i] / 2
  return [int(your_pay), int(friend_pay)]