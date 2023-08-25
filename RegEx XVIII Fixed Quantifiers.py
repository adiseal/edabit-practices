import re

txt = "Hello!... Wait. How goes?..... GoodBye!.."
pattern = r"\.{3,}"  # Using the {3,} fixed quantifier to match 3 or more dots
result = re.findall(pattern, txt)
print(result)  # Output: ['...', '.....']
