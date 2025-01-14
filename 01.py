def read_input(fname, strip=True):
    f = open("./inputs/"+fname, "r")
    if strip:
        contents = f.read().strip().split("\n")
    else:
        contents = f.read().split("\n")
    f.close()
    return contents


lines = read_input("01.txt")
nums = [i.split() for i in lines]
l_nums = sorted([int(i[0]) for i in nums])
r_nums = sorted([int(i[1]) for i in nums])
distance_total = 0
for i in range(len(l_nums)):
    l = l_nums[i]
    r = r_nums[i]
    distance_total += abs(l-r)
print(f"Part 1: {distance_total}")

similarity_total=0
for l in l_nums:
    l_count = 0
    for r in r_nums:
        if l==r:
            l_count+=1
    similarity_total+=l_count*l
print(f"Part 2: {similarity_total}")
