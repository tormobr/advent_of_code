
# solutio for part 1
def part1(l, h):
    data = [[int(x) for x in str(i)] for i in range(l, h)]
    return [test_double_1(digits) and not test_decreasing(digits) for digits in data].count(True)

# solution for part 2
def part2(l, h):
    data = [[int(x) for x in str(i)] for i in range(l, h)]
    return [test_double_2(digits) and not test_decreasing(digits) for digits in data].count(True)

# test if contains double digits for part 2
def test_double_2(digits):
    length = 6
    DP = [-1] + digits + [-1]
    return any([DP[i] != DP[i-1] and DP[i] == DP[i+1] and DP[i] != DP[i+2] for i in range(1,length)])


# test if contains double digits for part 1
def test_double_1(digits):
    return any([digits[i] == digits[i+1] for i in range(len(digits)-1)])

# test if digits are decreasing through the number
def test_decreasing(digits):
    return any([digits[i] > digits[i+1] for i in range(len(digits)-1)])

if __name__ == "__main__":
    l,h = [int(line) for line in open("input.txt", "r")]
    print(f"Part 1 answer: {part1(l, h)}")
    print(f"Part 2 answer: {part2(l, h)}")
