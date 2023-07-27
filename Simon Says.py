def simon_says(lst1, lst2):
    return lst1[:-1] == lst2[1:]

print(simon_says([
  "Simon says add 4",
  "Simon says add 6",
  "Then add 5"
])) # 10

print(simon_says([
  "Susan says add 10",
  "Simon says add 3",
  "Simon says multiply by 8"
])) # 24