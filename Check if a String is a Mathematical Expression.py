import re

def math_expr(input_str):
    # Define the regex pattern
    pattern = re.compile(r'^\d\s*[\+\-\*/%]\s*\d$')
    # Check if the input string matches the pattern
    return bool(pattern.match(input_str))