def dict_to_list(d):
    return sorted(d.items())

print(dict_to_list({
  "D": 1,
  "B": 2,
  "C": 3
})) # [("B", 2), ("C", 3), ("D", 1)]

print(dict_to_list({
  "likes": 2,
  "dislikes": 3,
  "followers": 10
})) # [("dislikes", 3), ("followers", 10), ("likes", 2)]