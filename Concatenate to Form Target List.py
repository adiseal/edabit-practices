def canConcatenate(smaller, target):
  target_counts = {element: target.count(element) for element in set(target)}
  
  for sublist in smaller:
    for element in sublist:
      if element not in target_counts or target_counts[element] < sublist.count(element):
        return False
      target_counts[element] -= sublist.count(element)
  
  return all(count == 0 for count in target_counts.values())