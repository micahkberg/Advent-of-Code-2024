def read_input(fname, strip=True):
    f = open("./inputs/"+fname, "r")
    if strip:
        contents = f.read().strip().split("\n")
    else:
        contents = f.read().split("\n")
    f.close()
    return contents


word_search = read_input('04.txt')
dirs = [(1, 0), (0, 1), (-1, 0,),
        (0, -1), (1, 1), (1, -1),
        (-1, 1), (-1, -1)]

#begin by identifying each X location:
x_locations = []
a_locations = []
for row_num in range(len(word_search)):
    for col_num in range(len(word_search[0])):
        if word_search[row_num][col_num] == "X":
            x_locations.append((col_num, row_num))
        if word_search[row_num][col_num] == "A":
            a_locations.append((col_num, row_num))

XMAS_count = 0
for x in x_locations:
    for v in dirs:
        end_spot = (x[0]+v[0]*3, x[1]+v[1]*3)
        if 0 <= end_spot[0] < len(word_search) and 0 <= end_spot[1] < len(word_search[0]):
            test_word = "X"
            for i in range(1, 4):
                test_word += word_search[x[1]+v[1]*i][x[0]+v[0]*i]
            if test_word == "XMAS":
                XMAS_count += 1
print(f"Part 1 xmas count: {XMAS_count}")

mas_count = 0
for a in a_locations:
    if 1 <= a[0] < 139 and 1 <= a[1] < 139:
        if word_search[a[1]-1][a[0]-1] + word_search[a[1]+1][a[0]+1] in ["MS","SM"]:
            if word_search[a[1]-1][a[0]+1] + word_search[a[1]+1][a[0]-1] in ["MS","SM"]:
                mas_count+=1
print(f"Part 2 x'd mas count: {mas_count}")

