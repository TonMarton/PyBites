def tail(filepath, n):
   """Similate Unix' tail -n, read in filepath, parse it into a list,
       strip newlines and return a list of the last n lines"""
   with open(filepath, 'r', ) as f:
      last_n_lines = f.read().splitlines()[-n:]
      return [line.strip('\n') for line in last_n_lines]

