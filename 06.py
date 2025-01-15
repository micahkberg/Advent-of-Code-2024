def read_input(fname, strip=True):
    f = open("./inputs/"+fname, "r")
    if strip:
        contents = f.read().strip().split("\n")
    else:
        contents = f.read().split("\n")
    f.close()
    return contents

area_map_raw = read_input("06.txt")
area_dict = {}


for y in range(len(area_map_raw)):
    for x in range(len(area_map_raw[0])):
        area_dict[(x, y)] = area_map_raw[y][x]
        if area_dict[(x, y)] == "^":
            start = (x, y)

x, y = start


def walk_map(map_dict, s):
    x, y = s
    facing = (0, -1)
    visited = set()
    visited.add(s)
    visited_more_details = set()
    visited_more_details.add((s, facing))

    while 0 <= x + facing[0] < len(area_map_raw[0]) and 0 <= y + facing[1] < len(area_map_raw):
        if area_dict[(x + facing[0], y + facing[1])] in ".^":
            x, y = (x + facing[0], y + facing[1])
            visited.add((x, y))
            if ((x, y), facing) in visited_more_details:
                return "unbounded"
            visited_more_details.add(((x, y), facing))
        elif area_dict[(x + facing[0], y + facing[1])] == "#":
            facing = (-facing[1], facing[0])
            visited_more_details.add(((x, y), facing))
    return visited


print(f"Part 1: guard visited {len(walk_map(area_dict, start))}")

count = 0
tiles_tried = 0
for location in walk_map(area_dict, start):
    if area_dict[location]=="^":
        continue
    area_dict[location] = "#"
    if walk_map(area_dict, start) == "unbounded":
        count += 1
    area_dict[location] = "."
    tiles_tried+=1
    #print(f"{tiles_tried}/5444")
print(f"Part 2: {count}")






