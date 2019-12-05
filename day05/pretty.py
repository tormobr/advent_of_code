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
    opcode, param1, param2 = parse_instruction(data, i) 
    return OPS[opcode](param1, param2, i, data)

def parse_instruction(data, i):
    instruction = data[i]
    modes = [x for x in str(instruction)]
    while len(modes) < 5:
        modes = ["0"] + modes
    opcode = int(modes[-2]+modes[-1])
    param1, param2, param3 = 0, 0, 0
    if opcode not in [3,4,99]:
        param1 = data[i+1] if  int(modes[-3]) else data[data[i+1]]
        param2 = data[i+2] if  int(modes[-4]) else data[data[i+2]]

    return opcode, param1, param2
    

def op_add(p1, p2, i, data):
    data[data[i+3]] = p1 + p2
    return 4

def op_mul(p1, p2, i, data):
    data[data[i+3]] = p1 * p2
    return 4

def op_in(p1, p2, i, data):
    data[data[i+1]] = 1
    return 2

def op_out(p1, p2, i, data):
    data[0] = data[data[i+1]]
    return 2

def op_halt(p1, p2, i, data):
    return -1

OPS = {
    1: op_add,
    2: op_mul,
    3: op_in,
    4: op_out,
    99: op_halt
}
    
if __name__ == "__main__":
    data = [int(x) for x in open("input.txt", "r").read().split(",")]
    print(f"Part 1 answer: {part1(data.copy())}")


