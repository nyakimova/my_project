from itertools import product
import sys
option = list(product(
    ('python 3.8.*', 'python 3.7.*', 'python 3.6.*'),
    ('venv + requirements.txt', 'virtualenv + requirements.txt', 'poetry', 'pipenv')
))
number_in_journal = 25
print(option[(number_in_journal - 1) % 12])
print(sys.version)