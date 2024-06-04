def right_triangle(x, y, z):
  if (x <= 0 or y <= 0 or z <= 0 or
      x + y <= z or x + z <= y or y + z <= x):
    return False

  sides = [x, y, z]
  sides.sort()

  return (sides[0] * sides[0]) + (sides[1] * sides[1]) == sides[2] * sides[2]