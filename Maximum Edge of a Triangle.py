def next_edge(side1, side2):
  maximum_range = (side1 + side2) - 1
  return maximum_range
  
print(next_edge(8, 10)) # 17
print(next_edge(5, 7)) # 11
print(next_edge(9, 2)) # 10
print(next_edge(10, 4)) # 13 