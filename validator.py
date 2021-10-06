
# Determines if (input) string is acceptable. Returns True if yes, otherwise False.
def validate_string(string: str):
    # Length
    if len(string) > 100:
        return False
    if len(string) < 1:
        return False
    return True
