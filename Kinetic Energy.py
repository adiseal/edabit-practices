def calc_kinetic_energy(m, v):
    return round(1 / 2 * m * v * v)



assert calc_kinetic_energy(60, 3) == 270

assert calc_kinetic_energy(45, 10) == 2250

assert calc_kinetic_energy(63.5, 7.35) == 1715