def add_parity_bit(b):
    the_ones = b.count("1") 
    if the_ones % 2 == 0:
        return b + "0"
    return b + "1"

print(add_parity_bit("0010110")) # "00101101"