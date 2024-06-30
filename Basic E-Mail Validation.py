import re

def validate_email(email):
    if "@" not in email:
        return False
    
    local_part, domain = email.split("@", 1)
    
    if "." not in domain:
        return False
    
    if not local_part:
        return False
    
    if domain.startswith(".") or domain.endswith(".") or domain.startswith("@") or domain.endswith("@"):
        return False
    
    return True