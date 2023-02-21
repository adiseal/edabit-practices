# Fix this incorrect code!
def check_all_even(lst):
  return all(n % 2 == 0 for n in lst)
  
print(check_all_even([5, 6, 8, 10])) # False