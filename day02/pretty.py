
# Solution to part 1
def part1(data):
    set_noun_verb(12, 2, data)
    for i in range(0, len(data), 4):
        if execute_code(data, i) == -1:
            break
    return data[0]


# Solution to part 2
def part2(data):
    for noun in range(100):
        for verb in range(100):
            a = data.copy()
            set_noun_verb(noun, verb, a)
            for i in range(0, len(a), 4):
                if execute_code(a, i) == -1:
                    break
            if a[0] == 19690720:
                return noun * 100 + verb

# executes a intcode
def execute_code(data, i):
    if data[i] == 1:
        data[data[i+3]] = data[data[i+1]] + data[data[i+2]]
    elif data[i] == 2:
        data[data[i+3]] = data[data[i+1]] * data[data[i+2]]
    elif data[i] == 99:
        return -1
    return 0

# sets the noun and verb in the intcodes
def set_noun_verb(n, v, data):
    data[1] = n
    data[2] = v

if __name__ == "__main__":
    data = [int(x) for x in open("input.txt", "r").read().split(",")]
    print(f"Part 1 answer: {part1(data.copy())}")
    print(f"Part 2 answer: {part2(data.copy())}")


