def count_characters(shape):
    count = 0
    for row in shape:
        count += len(row)
    return count

print(count_characters([
  "###",
  "###",
  "###"
])) # 9

print(count_characters([
  "22222222",
  "22222222",
])) # 16

print(count_characters([
  "------------------"
])) # 18

print(count_characters([])) # 0