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

    

        
