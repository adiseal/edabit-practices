def should_serve_drinks(age, on_break):
    is_allowed = age >= 18 and not on_break
    return is_allowed    
            
assert should_serve_drinks(17, True) == False

assert should_serve_drinks(18, False) == True

assert should_serve_drinks(30, True) == False