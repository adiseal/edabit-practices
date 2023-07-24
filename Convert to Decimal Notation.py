def convert_to_decimal(percentages):
    return [float(p.strip('%'))/100 for p in percentages]
