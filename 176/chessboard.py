WHITE, BLACK = ' ', '#'


def create_chessboard(size=8):
   """Create a chessboard with of the size passed in.
       Don't return anything, print the output to stdout"""
   raw_row = ' #' * int(size / 2)
   print((raw_row + '\n' + raw_row[::-1] + '\n') * int(size / 2))