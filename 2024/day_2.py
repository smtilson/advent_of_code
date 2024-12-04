from raw_inputs import day_2 as actual_input

sample = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

def parse_input(raw_input:str):
    lines = raw_input.split("\n")
    return [[int(x) for x in line.split()] for line in lines]

def part1(raw_data):
    reports = parse_input(raw_data)
    return sum(safe_report(report) for report in reports)

def part2(raw_data):
    reports = parse_input(raw_data)
    count = 0
    for report in reports:
        if safe_report(report):
            count += 1
        elif problem_dampener(report):
            count += 1
    return count

def increasing(report:list[int]) -> bool:
    for i in range(1, len(report)):
        if report[i] <= report[i-1]:
            return False
    return True

def decreasing(report:list[int]) -> bool:
    for i in range(1, len(report)):
        if report[i] >= report[i-1]:
            return False
    return True

def max_change(report):
    for i in range(1, len(report)):
        if abs(report[i] - report[i-1]) < 1:
            return False
        if abs(report[i] - report[i-1]) > 3:
            return False
    return True

def safe_report(report:list[int]) -> bool:
    return (increasing(report) or decreasing(report)) and max_change(report)

def problem_dampener(report: list[int]) -> bool:
    for i in range(len(report)):
        test = [report[j] for j in range(len(report)) if j != i]
        if safe_report(test):
            return True
    return False

if __name__ == "__main__":
    print(part2(actual_input))