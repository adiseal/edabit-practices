def anti_divisors(n):
  if n <= 1:
    return []

  anti_divisors = []
  for i in range(2, n):
    if n % i != 0:
      if i % 2 == 0 and (n * 2) % i == 0:
        anti_divisors.append(i)
      elif i % 2 == 1 and ((n * 2 - 1) % i == 0 or (n * 2 + 1) % i == 0):
        anti_divisors.append(i)

  return sorted(anti_divisors)