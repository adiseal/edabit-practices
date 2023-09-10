def halflife_calculator(mass, halflife_years, num_halflives):
    final_mass = mass * (0.5 ** num_halflives)
    total_years = halflife_years * num_halflives
    return [round(final_mass, 3), total_years]
