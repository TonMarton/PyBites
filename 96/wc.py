
def wc(file_: str):
    """Takes an absolute file path/name, calculates the number of
       lines/words/chars, and returns a string of these numbers + file, e.g.:
       3 12 60 /tmp/somefile
       (both tabs and spaces are allowed as separator)"""
    read_data: str
    with open(file_, 'r') as f:
        read_data = f.read()
    
    return f'{len(read_data.splitlines())}\t{len(read_data.split())}\t{len(read_data)}\t{file_}'


if __name__ == '__main__':
    # make it work from cli like original unix wc
    import sys
    print(wc(sys.argv[1]))