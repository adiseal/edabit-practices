def multiply_nums(str1):
  numbers = str1.split(", ")
  product = 1
  for number in numbers:
    product *= int(number)
  return product

print(multiply_nums("2, 3")) # 6
print(multiply_nums("1, 2, 3, 4")) # 24
print(multiply_nums("54, 75, 453, 0")) # 0
print(multiply_nums("10, -2")) # -20

