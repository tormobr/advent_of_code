# Solution to part 1 and two
def eval(data):
    i = 0
    while i != -1:
        i = execute_code(data, i)
    return data[0]

# executes a intcode
def execute_code(data, i):
    opcode, param1, param2 = parse_instruction(data, i) 
    return OPS[opcode](data, i, param1, param2)

# parses an instruction and its parameters
def parse_instruction(data, i):
    param1, param2 = 0, 0
    instruction = "0"*(5 - len(str(data[i]))) + str(data[i])    # adds missing 0's
    opcode = int(instruction[-2] + instruction[-1])
    if opcode not in [3,4,99]:
        param1 = data[i+1] if  int(instruction[-3]) else data[data[i+1]]
        param2 = data[i+2] if  int(instruction[-4]) else data[data[i+2]]

    return opcode, param1, param2


# adds two parameters and stores in third
def op_add(data, i, p1, p2):
    data[data[i+3]] = p1 + p2
    return i + 4

# mulitplies two parameters and stores in third
def op_mul(data, i, p1, p2):
    data[data[i+3]] = p1 * p2
    return i + 4

# takes input and stores at parameter 1
def op_in(data, i, *args):
    data[data[i+1]] = innput
    return i + 2

# ouputs value on parameter 1
def op_out(data, i, *args):
    data[0] = data[data[i+1]]
    return i + 2

# Jumps to parameter 2 index if parameter 1 is true
def op_jump_if_true(data, i, p1, p2):
    return p2 if p1 != 0 else i +3

# Jumps to parameter 2 index if parameter 1 is false
def op_jump_if_false(data, i, p1, p2):
    return p2 if p1 == 0 else i + 3

# sets parameter 3 to 1 if parameter 1 is less than parameter 2
def op_less(data, i, p1, p2):
    data[data[i+3]] = 1 if p1 < p2 else 0
    return i + 4

# sets parameter 3 to 1 if parameter 1 and 2 are equal
def op_equals(data, i, p1, p2):
    data[data[i+3]] = 1 if p1 == p2 else 0
    return i + 4

# halts the program
def op_halt(*args):
    return -1

# operation codes and their functions
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
# The input ID for the system.. 1 for part 1, and 5 for part 2
innput = 1
    
if __name__ == "__main__":
    data = [int(x) for x in open("input.txt", "r").read().split(",")]
    print(f"Part 1 answer: {eval(data.copy())}")
    innput = 5
    print(f"Part 2 answer: {eval(data.copy())}")


