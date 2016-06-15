from collections import namedtuple

Swimmer = namedtuple('Swimmer', ['active', 'name', 'age', 'gender'])
Swimmer.__new__.__defaults__ = (True, None, None, None)
