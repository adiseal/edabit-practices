def count_identical(lst):
    count = 0
    for sub_list in lst:
        if len(set(sub_list)) == 1:
            count += 1
    return count
    
print(count_identical([
  [1],
  [2],
  [3],
  [4]
])) # 4