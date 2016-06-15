import sys
from parsers import tmmgr
from parsers import swimtopia

def swimmer_match(sw1, sw2):
    match = False
    if (sw1.name == sw2.name and sw1.age == sw2.age
        and sw1.gender == sw2.gender):
        match = True
    return match

if len(sys.argv) != 3:
    print("Usage: test.py <team manager file> <swimtopia file>")
    sys.exit(1)

tm_swimmers = tmmgr.parse(sys.argv[1])
st_swimmers = swimtopia.parse(sys.argv[2])

for tm_name, tm_swimmer in tm_swimmers.items():
    if (not tm_swimmer.active and tm_name in st_swimmers
        and swimmer_match(tm_swimmer, st_swimmers[tm_name])):
        print(tm_name + " is inactive in Team Manager, but in SwimTopia roster")
    if (tm_swimmer.active and tm_name not in st_swimmers):
        print(tm_name + " is active in Team Manager, but NOT in SwimTopia roster")
