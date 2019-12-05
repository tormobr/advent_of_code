
# Solution to part 1
def part1(data):
    i = 0
    while True:
        ret = execute_code(data, i)
        if ret == -1:
            break
        else:
            i += ret
    return data[0]

# executes a intcode
def execute_code(data, i):
    instruction = data[i]
    print("iunstrunction and params", data[i], data[i+1], data[i+2], data[i+3])
    modes = [x for x in str(instruction)]
    while len(modes) < 5:
        modes = ["0"] + modes
    print("modes", modes)
    opcode = int(modes[-2]+modes[-1])
    print("opcode", opcode)
    param1, param2, param3 = 0, 0, 0
    if opcode not in [3,4,99]:
        param1 = data[i+1] if  int(modes[-3]) else data[data[i+1]]
        param2 = data[i+2] if  int(modes[-4]) else data[data[i+2]]
        param3 = data[i+3] if  int(modes[-5])  else data[data[i+3]]
 
    print(param1, param2, param3)
    if opcode == 1:
        data[data[i+3]] = param1 + param2
    elif opcode == 2:
        data[data[i+3]] = param1 * param2
    elif opcode == 3:
        data[data[i+1]] = 1
        return 2
    elif opcode == 4:
        print(data[data[i+1]])
        return 2
    elif opcode == 99:
        return -1
    return 4

# sets the noun and verb in the intcodes
def set_noun_verb(n, v, data):
    data[1] = n
    data[2] = v

if __name__ == "__main__":
    data = [int(x) for x in open("input.txt", "r").read().split(",")]
    print(f"Part 1 answer: {part1(data.copy())}")


