from re import search, IGNORECASE

VOWELS = 'aeiou'
PYTHON = 'python'


def contains_only_vowels(input_str: str) -> bool:
   """Receives input string and checks if all chars are
      VOWELS. Match is case insensitive."""
   
   return search(fr'[^{VOWELS}]', input_str, IGNORECASE) == None


def contains_any_py_chars(input_str: str) -> bool:
   """Receives input string and checks if any of the PYTHON
       chars are in it. Match is case insensitive."""
   
   return search('[{PYTHON}]', input_str, IGNORECASE) != None


def contains_digits(input_str: str) -> bool:
   """Receives input string and checks if it contains
       one or more digits."""
   return search(r'\d', input_str) != None