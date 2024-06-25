def initialize(names):
    initials = []
    for name in names:
        parts = name.split()  
        if len(parts) == 2:  
            first_initial = parts[0][0].upper()  
            last_initial = parts[1][0].upper()  
            initials.append("%s. %s." % (first_initial, last_initial))
    return initials