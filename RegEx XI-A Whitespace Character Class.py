import re

txt = "best buy best car best friend best-boy bestguest best dressed best bet best man best deal best boyfriend"
pattern = r"best\s+b\w+"

matches = re.findall(pattern, txt)