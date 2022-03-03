from curses.ascii import isalnum

def get_index_different_char(chars: list):
    alnum_count: int = 0
    last_alnum_index: int = None
    last_non_alnum_index: int = None

    for i in range(3):
        if str(chars[i]).isalnum():
            alnum_count += 1
            last_alnum_index = i
        else:
            last_non_alnum_index = i

    if alnum_count > 1:
        if last_non_alnum_index != None:
            return last_non_alnum_index
        else:
            for i in range(3, len(chars)):
                if not str(chars[i]).isalnum():
                    return i
    elif alnum_count < 2:
        if last_alnum_index != None:
            return last_alnum_index
        else:
            for i in range(3, len(chars)):
                if str(chars[i]).isalnum():
                    return i

    import string 

    alphanumeric_chars = list(string.ascii_letters + string.digits)
    
    def get_index_different_char_official(chars):
        matches, no_matches = [], []
        for i, char in enumerate(chars):
            if str(char).lower() in alphanumeric_chars:
                matches.append(i)
        else:
                no_matches.append(i)
        return matches[0] if len(matches) == 1 else no_matches[0]

    def get_index_different_char_smart(chars):
        bools = [str(c).isalnum() for c in chars]
        return bools.index(True) if bools.count(True) == 1 else bools.index(False)
    
