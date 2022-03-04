from re import match

def count_indents(text):
    """Takes a string and counts leading white spaces, return int count"""
    return len(match(r'( *)', text).group(1))