import math

def impedance_calculator(Dd, Dc, er):
    Z0 = 138 / math.sqrt(er) * math.log10(Dd / Dc)
    return round(Z0, 1)