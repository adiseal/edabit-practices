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

print(eda_bit(0, 10)) # ["EdaBit", 1, 2, "Eda", 4, "Bit", "Eda", 7, 8, "Eda", "Bit" ]
print(eda_bit(14, 20)) # [14,  "EdaBit", 16, 17,  "Eda", 19, "Bit" ]
print(eda_bit(99, 106)) # ["Eda", "Bit", 101, "Eda", 103, 104, "EdaBit", 106 ]