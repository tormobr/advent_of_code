import numpy as np

# Solution to part 1
def part1(data, iterations):
    for i in range(iterations):
        data = phase(data)
    return "".join([str(x) for x in data[:8]])

# solution to part 2
# since message_offset if after half we can use cumulative sum from the
# back to the start. There are only 1 and 0 for pattern after half.
def part2(data, iterations):
    message_offset = int("".join([str(x) for x in data[:7]]))
    in_out = data[message_offset:]
    for i in range(iterations):
        reverse = in_out[::-1]
        in_out = last_digit(np.cumsum(reverse))[::-1]
    return "".join([str(x) for x in in_out[:8]])


# executes one phase and returns output list
def phase(inn):
    l = len(inn)
    return [last_digit(np.sum(inn * get_pattern(i, l))) for i in range(l)]

# Extracts the last digit(to the right) from a integer
def last_digit(n):
    return abs(n) % 10

# Generates the repeating pattern depening on out index and input lenght
def get_pattern(i, n):
    basic_pattern = [0,1,0,-1] 
    repeated = np.repeat(basic_pattern, i+1)
    return np.roll(np.tile(repeated, n // len(repeated)+1),-1)[:n]


if __name__ == "__main__":
    string = open("input.txt").read().strip()
    list_data = [int(x) for x in string]
     
    data1 = np.array(list_data)
    data2 = np.array(list_data*10000)

    print(f"Part 1 answer: {part1(data1.copy(), 100)}")
    print(f"Part 2 answer: {part2(data2.copy(), 100)}")
