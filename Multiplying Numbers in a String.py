def multiply_nums(str1):
  numbers = str1.split(", ")
  product = 1
  for number in numbers:
    product *= int(number)
  return product
