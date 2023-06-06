def possible_bonus(a, b):
    if b > a:
        a = a + 6
        if a == b:
          return None
        elif a >= b :
            return True
        else:
            return False

 print(possible_bonus(1, 9)) # False