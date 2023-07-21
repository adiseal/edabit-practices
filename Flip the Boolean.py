def reverse(value):
    if type(value) == bool:
        return not value
    else:
        return "boolean expected"

print(flip_bool(True)) # 0
print(flip_bool(False)) # 1