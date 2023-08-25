def first_arg(*args):
    if len(args) == 0:
        return None
    else:
        return args[0]

def last_arg(*args):
    if len(args) == 0:
        return None
    else:
        return args[-1]

print(first_arg(1, 2, 3)) # 1
print(last_arg(1, 2, 3)) # 3