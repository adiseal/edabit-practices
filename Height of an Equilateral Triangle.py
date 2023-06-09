def height(side):
    # Calculate the height of the equilateral triangle
    height_mm = str(round(side * 10 * 0.866, 1))

    return height_mm + " mm"
    
print(height(2)) # 17.3 mm