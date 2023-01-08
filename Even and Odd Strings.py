def even_odd_string(txt):
    return str(txt[::2]) + " " + str(txt[1::2])
    
    
assert even_odd_string("edabit") == "eai dbt"

assert even_odd_string("airforce") == "aroc ifre"
