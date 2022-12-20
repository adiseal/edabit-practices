def amazing_edabit(s):
    if "edabit" in s:
        return s
    else:
        return s.replace("amazing", "not amazing")
        
assert amazing_edabit("edabit is amazing.") == "edabit is amazing."

assert amazing_edabit("Mubashir is amazing.") == "Mubashir is not amazing."

assert amazing_edabit("Infinity is amazing.") == "Infinity is not amazing."