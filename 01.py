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
l_nums = [int(i[0]) for i in nums]
r_nums = [int(i[0]) for i in nums]
print(l_nums)
