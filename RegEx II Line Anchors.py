import re

pattern = "^/users/edabit/.*"

print(bool(re.search(pattern, "/users/edabit/python/regex.py"))) # True
print(bool(re.search(pattern, "/users/edabitt/python/file.txt"))) # False