def split_and_delimit(string, n, delimiter):

  # Check if the string is empty or if n is 0
  if not string or n == 0:
    return string

  # Split the string into substrings of size n
  substrings = [string[i:i+n] for i in range(0, len(string), n)]

  # Join the substrings with the delimiter
  return delimiter.join(substrings)