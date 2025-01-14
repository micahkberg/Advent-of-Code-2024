def read_input(fname, strip=True):
    f = open("./inputs/"+fname, "r")
    #if strip:
    #    contents = f.read().strip().split("\n")
    #else:
    #    contents = f.read().split("\n")
    contents=f.read()
    f.close()
    return contents

import re

memory = read_input("03.txt")
#print(memory)
muls = re.findall("mul\(\d+,\d+\)", memory)
total_value = 0
for mul in muls:
    #print(mul)
    m, n = [int(i) for i in mul.strip("mul()").split(",")]
    #print(f"{m} * {n}")
    total_value += m*n
print(f"Part 1: {total_value}")

total_value_part2 = 0
do = True
for m in re.finditer("mul\(\d+,\d+\)|do\(\)|don't\(\)", memory):
    #print(m.group())
    if m.group() == "do()":
        do = True
    elif m.group() == "don't()":
        do = False
    elif do:
        i, j = [int(i) for i in m.group().strip("mul()").split(",")]
        total_value_part2 += i * j


print(f"Part 2: {total_value_part2}")



