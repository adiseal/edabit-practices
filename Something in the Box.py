def in_box(lst):
    for row in lst[1:-1]:
        if '*' in row[1:-1]:
            return True
    return False

print(in_box([
  "###",
  "#*#",
  "###"
])) # True