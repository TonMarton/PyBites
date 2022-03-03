import secrets
import string

def gen_key(parts: int = 4, chars_per_part: int = 8):
    chars = string.ascii_uppercase + string.digits
    return '-'.join(''.join(secrets.choice(chars) for _ in range(chars_per_part)) for _ in range(parts))
    