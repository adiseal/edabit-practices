import re

pattern = "^/users/edabit/.*"

print(bool(re.search(pattern, "/users/edabit/python/regex.py"))) # True