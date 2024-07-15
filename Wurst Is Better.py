import re

def wurst_is_better(text):
    # List of German Wursts (all contain 'wurst')
    german_wursts = ["Bratwurst", "Kochwurst", "Leberwurst", "Mettwurst", "Rostbratwurst"]
    
    # List of sausages to be replaced with "Wurst"
    non_german_sausages = ["Kielbasa", "Chorizo", "Moronga", "Salami", "Sausage", "Andouille", "Naem", "Merguez", "Gurka", "Snorkers", "Pepperoni"]
    
    # Function to replace non-German sausages with 'Wurst'
    def replace_sausages(match):
        sausage = match.group()
        if sausage in german_wursts:
            return sausage
        else:
            return "Wurst"
    
    # Create a regex pattern that matches any sausage from the lists
    pattern = re.compile(r'\b(?:' + '|'.join(re.escape(s) for s in german_wursts + non_german_sausages) + r')\b', re.IGNORECASE)
    
    # Use the pattern to substitute non-German sausages with 'Wurst'
    result = pattern.sub(replace_sausages, text)
    
    return result