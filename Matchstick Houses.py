def match_houses(step):
    s = 6
    if step == 0:
        return 0
    else:
        s += (step - 1) * 5
        return s
      
    
print(match_houses(1)) 