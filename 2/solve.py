def check_report(report):
    """returns 1 if report is safe, 0 else"""
    prior_level = report[0]
    increasing = True
    decreasing = True
    for level in report[1:]:
        delta = abs(level - prior_level)
        if (delta > 3) or (delta == 0):
            return 0
        if level > prior_level:
            decreasing = False
        if level < prior_level:
            increasing = False
        prior_level = level
    return int(increasing or decreasing)

def check_report_dampener(report):
    """laziest possible solutions lol"""
    result = check_report(report)
    if result:
        return 1
    # otherwise, yeet
    for i in range(len(report)):
        temp_report = report[0:i] + report[i+1:]
        if check_report(temp_report):
            return 1
    return 0

def parse_report(file_obj):
    return list(map(lambda report: [int(x) for x in report.split()], file_obj.read().strip().split('\n')))

with open("input", "r") as input_file:
    reports = parse_report(input_file)

with open("test_input", "r") as test_file:
    test_reports = parse_report(test_file)

#print("TEST CASE: ", sum(map(check_report, test_reports)))
print("Part 1: ", sum(map(check_report, reports)))
print("Part 2: ", sum(map(check_report_dampener, reports)))




