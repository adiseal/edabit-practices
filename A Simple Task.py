def decimal_part(n):
  number_str = str(n)
  parts = number_str.split(".")
  if len(parts) == 1:
    return 0
  return float("0." + parts[1])