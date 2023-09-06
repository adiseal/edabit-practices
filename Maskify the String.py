def maskify(string: str) -> str:
    if len(string) <= 4:
        return string
    else:
        return "#" * (len(string) - 4) + string[-4:]

print(maskify("4556364607935616")) # "############5616"
print(maskify("64607935616")) # "#######5616"
print(maskify("1")) # "1"