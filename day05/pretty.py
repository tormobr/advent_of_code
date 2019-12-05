# Solution to part 1
def part1(data):
    i = 0
    while i != -1:
        i = execute_code(data, i)
    return data[0]

# executes a intcode
def execute_code(data, i):
    opcode, param1, param2 = parse_instruction(data, i) 
    return OPS[opcode](data, i, param1, param2)

def parse_instruction(data, i):
    param1, param2 = 0, 0
    instruction = "0"*(5 - len(str(data[i]))) + str(data[i])    # adds missing 0's
    opcode = int(instruction[-2] + instruction[-1])
    if opcode not in [3,4,99]:
        param1 = data[i+1] if  int(instruction[-3]) else data[data[i+1]]
        param2 = data[i+2] if  int(instruction[-4]) else data[data[i+2]]

    return opcode, param1, param2


def op_add(data, i, p1, p2):
    data[data[i+3]] = p1 + p2
    return i + 4

def op_mul(data, i, p1, p2):
    data[data[i+3]] = p1 * p2
    return i + 4

def op_in(data, i, *args):
    data[data[i+1]] = 5
    return i + 2

def op_out(data, i, *args):
    data[0] = data[data[i+1]]
    return i + 2

def op_jump_if_true(data, i, p1, p2):
    if p1 != 0:
        return p2
    return i + 3

def op_jump_if_false(data, i, p1, p2):
    if p1 == 0:
        return p2
    return i + 3

def op_less(data, i, p1, p2):
    if p1 < p2:
        data[data[i+3]] = 1
        return i+4
    data[data[i+3]] = 0
    return i + 4

def op_equals(data, i, p1, p2):
    if p1 == p2:
        data[data[i+3]] = 1
        return i+4
    data[data[i+3]] = 0
    return i + 4

def op_halt(*args):
    return -1

OPS = {
    1: op_add,
    2: op_mul,
    3: op_in,
    4: op_out,
    5: op_jump_if_true,
    6: op_jump_if_false,
    7: op_less,
    8: op_equals,
    99: op_halt
}
    
if __name__ == "__main__":
    data = [int(x) for x in open("input.txt", "r").read().split(",")]
    print(f"Part 1 answer: {part1(data.copy())}")


