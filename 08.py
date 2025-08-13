def read_input(fname, strip=True):
    f = open("./inputs/"+fname, "r")
    if strip:
        contents = f.read().strip().split("\n")
    else:
        contents = f.read().split("\n")
    f.close()
    return contents


antenna_map = read_input("08.py")
antennas = set()
for line in antenna_map:
    for char in line:
        antennas.add(char)
antennas.remove(".")

for x in range(len(antenna_map)):
    for y in range(len(antenna_map)):
        for antenna in antennas:




