def odd_sum_list(arr):
  result = []
  for i in range(len(arr) - 1):
    result.append((arr[i] + arr[i + 1]) % 2 == 0)
  return result