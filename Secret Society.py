def society_name(friends):
    return ''.join(sorted([name[0] for name in friends]))

print(society_name(["Adam", "Sarah", "Malcolm"])) # "AMS"