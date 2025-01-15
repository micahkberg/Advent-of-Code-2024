from functools import cmp_to_key

def read_input(fname, strip=True):
    f = open("./inputs/"+fname, "r")
    if strip:
        contents = f.read().strip().split("\n")
    else:
        contents = f.read().split("\n")
    f.close()
    return contents


lines = read_input("05.txt")
rules = []
updates = []

for line in lines:
    if "|" in line:
        rules.append(line.split("|"))
    if "," in line:
        updates.append(line.split(","))


def corrected_order(upd):
    def compare_values(v1, v2):
        for rule in rules:
            if rule[0] == v1 and rule[1] == v2:
                return -1
            if rule[1] == v1 and rule[0] == v2:
                return 1
        return 0
    return sorted(upd, key=cmp_to_key(compare_values))


def is_order_correct(upd):
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[0]) > update.index(rule[1]):
                return False
    return True


correct_update_total = 0
incorrect_update_total = 0
for update in updates:
    if is_order_correct(update):
        correct_update_total += int(update[len(update) // 2])
    else:
        incorrect_update_total += int(corrected_order(update)[len(update)//2])


print(f"Part 1: middle page total {correct_update_total}")
print(f"Part 2: middle page total {incorrect_update_total}")
