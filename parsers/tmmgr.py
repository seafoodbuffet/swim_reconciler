import csv
from parsers.swimmer import Swimmer

def parse(file):
    swimmers = {}
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            swimmer = Swimmer(active = False if "*I" == row[19] else True, name = row[20], gender = row[21], age = row[22])
            swimmers[swimmer.name] = swimmer
        return swimmers
