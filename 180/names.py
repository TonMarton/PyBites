from collections import defaultdict
from itertools import count

from more_itertools import first

# fake data from https://www.mockaroo.com
data = """last_name,first_name,country_code
Watsham,Husain,ID
Harrold,Alphonso,BR
Apdell,Margo,CN
Tomblings,Deerdre,RU
Wasielewski,Sula,ID
Jeffry,Rudolph,TD
Brenston,Luke,SE
Parrett,Ines,CN
Braunle,Kermit,PL
Halbard,Davie,CN"""


def group_names_by_country(data: str = data) -> defaultdict:
    countries = defaultdict(list)
    # your code
    for line in data.splitlines()[1:]:
        last_name, first_name, key = line.split(',')
        countries[key].append(first_name + ' ' + last_name)
    return countries