def add_parity_bit(b):
    the_ones = b.count("1") 
    if the_ones % 2 == 0:
        return b + "0"
    return b + "1"


assert add_parity_bit("0010110") == "00101101"

assert add_parity_bit("1100000") == "11000000"

assert add_parity_bit("1111111") == "11111111"

print(add_parity_bit("0010110")) # "00101101"

print(add_parity_bit("1100000")) # "11000000"

print(add_parity_bit("1111111")) # "11111111"