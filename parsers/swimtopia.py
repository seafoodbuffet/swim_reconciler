from parsers.swimmer import Swimmer

def parse(file):
    swimmers = {}
    f = open(file)
    for line in f:
        if line.startswith('D1'):
            lastname = line[8:28].strip()
            firstname = line[28:48].strip()
            gender = line[2]
            age = line[97:99].strip()
            swimmer = Swimmer(active = True, name = firstname + " " + lastname, gender = gender, age = age)
            swimmers[swimmer.name] = swimmer
    return swimmers
