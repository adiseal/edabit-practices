def eda_bit(start, end):
    result = []
    for i in range(start, end + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("EdaBit")
        elif i % 3 == 0:
            result.append("Eda")
        elif i % 5 == 0:
            result.append("Bit")
        else:
            result.append(i)
    return result
