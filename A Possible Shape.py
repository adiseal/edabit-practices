def is_shape_possible(n, angles):
  # Check if n is less than 3
  if n < 3:
    return False

  # Check if any angle is greater than 180 degrees
  for angle in angles:
    if angle >= 180:
      return False

  # Calculate the sum of interior angles
  total_angles = (n - 2) * 180

  # Check if the sum of given angles matches the calculated sum
  if sum(angles) == total_angles:
    return True
  else:
    return False