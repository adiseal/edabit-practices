import re

txt = "**^&$Regular#$%Expressions$%$$%^**"
pattern = r'\w+'

result = " ".join(re.findall(pattern, txt))