import re

# This is a regular expression that matches an email address
email_pattern = r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$"

def validateEmail(email):
    if not email:
        return False
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return False
    return True