def tallest_building_height(lst):
    height_per_line = 20
    num_lines = sum(1 for line in lst if '#' in line)
    total_height = num_lines * height_per_line
    return str(total_height) + 'm'