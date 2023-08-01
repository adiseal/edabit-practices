def convert_to_decimal(percentages):
    return [float(p.strip('%'))/100 for p in percentages]

print(convert_to_decimal(["1%", "2%", "3%"])) # [0.01, 0.02, 0.03]