def read_input(fname, strip=True):
    f = open("./inputs/"+fname, "r")
    if strip:
        contents = f.read().strip().split("\n")
    else:
        contents = f.read().split("\n")
    f.close()
    return contents


reports = read_input("02.txt")
reports = [line.split() for line in reports]


def report_diffs(report):
    levels = [int(i) for i in report]
    diffs = []
    for i in range(1, len(levels)):
        diffs.append(levels[i]-levels[i-1])
    return diffs


def check_report_with_dampening(report):
    for i in range(len(report)):
        sub_report = report[:i] + report[i+1:]
        if check_report_without_dampening(sub_report):
            return True
    return False


def check_report_without_dampening(report):
    diffs = report_diffs(report)
    report_safe = True
    for diff in diffs:
        if not (1 <= abs(diff) <= 3):
            report_safe = False
            break
    if min(diffs) < 0 < max(diffs):
        report_safe = False
    return report_safe


reports_passing_without_dampening = 0
reports_passing_with_dampening = 0
for report in reports:
    if check_report_without_dampening(report):
        reports_passing_without_dampening += 1
        reports_passing_with_dampening += 1
    elif check_report_with_dampening(report):
        reports_passing_with_dampening += 1

print(f"Part 1: {reports_passing_without_dampening}")
print(f"Part 2: {reports_passing_with_dampening}")
