def read_input(fname, strip=True):
    f = open("./inputs/"+fname, "r")
    if strip:
        contents = f.read().strip().split("\n")
    else:
        contents = f.read().split("\n")
    f.close()
    return contents


import itertools

tests = read_input("07.txt")
test_total = 0
failed_part_1 = []
for test in tests:
    goal, nums = test.split(":")
    goal = int(goal)
    nums = [int(i) for i in nums.strip().split()]
    operations = itertools.product("AM", repeat=len(nums)-1)
    fail=True
    for operation in operations:
        oper_iter = iter(operation)
        result = nums[0]
        for num in nums[1:]:
            op = next(oper_iter)
            if op == "A":
                result += num
            elif op == "M":
                result *= num
            if result > goal:
                break
        if goal == result:
            test_total += goal
            fail=False
            break
    if fail:
        failed_part_1.append(test)

print(test_total)

test_total_part_2 = test_total
print(f"total tests that failed to try again on: {len(failed_part_1)}")
c = 0
for test in failed_part_1:
    c += 1
    print(c)
    goal, nums = test.split(":")
    goal = int(goal)
    nums = [int(i) for i in nums.strip().split()]
    operations = itertools.product("AMC", repeat=len(nums)-1)
    for operation in operations:
        oper_iter = iter(operation)
        result = nums[0]
        for num in nums[1:]:
            op = next(oper_iter)
            if op == "A":
                result += num
            elif op == "M":
                result *= num
            elif op == "C":
                result = int(str(result)+str(num))
            if result > goal:
                break
        if goal == result:
            test_total_part_2 += goal
            break
print(test_total_part_2)


