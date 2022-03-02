from calendar import c


names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
countries = 'Australia Spain Global Argentina USA Mexico'.split()


def enumerate_names_countries():
   """Outputs:
       1. Julian     Australia
       2. Bob        Spain
       3. PyBites    Global
       4. Dante      Argentina
       5. Martin     USA
       6. Rodolfo    Mexico"""
   FIRSTNAME_COL_WIDTH = 11
   for i, (name, country) in enumerate(zip(names, countries)):
      buffer_spaces = ' ' * (FIRSTNAME_COL_WIDTH - len(name))
      print(f'{i + 1}. {name}{buffer_spaces}{country}')
   pass