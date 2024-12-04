from raw_inputs import day_1 as actual_input

sample = """3   4
4   3
2   5
1   3
3   9
3   3"""

def parse_input(input_str):
    lines = input_str.split("\n")
    tuples = [(int(a), int(b)) for line in lines for a, b in [line.split()]]
    return [a for a,b in tuples], [b for a,b in tuples]

def part1(raw_input):
    first, second = parse_input(raw_input)
    first.sort()
    second.sort()
    return sum([abs(a-b) for a,b in zip(first, second)])

def part2(raw_input):
    first, second = parse_input(raw_input)
    count_dict = {num:second.count(num) for num in set(first)}
    return sum([num*count_dict[num] for num in first])


    
if __name__ == "__main__":
    print(part2(actual_input))
    