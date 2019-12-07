from itertools import permutations

class Intcoder:
    def __init__(self, data):
        # operation codes and their functions
        self.OPS = {
            1: self.op_add,
            2: self.op_mul,
            3: self.op_in,
            4: self.op_out,
            5: self.op_jump_if_true,
            6: self.op_jump_if_false,
            7: self.op_less,
            8: self.op_equals,
            99: self.op_halt
        }

    # Solution to part 1 and two
    def eval(self, data, i1, i2):
        self.input = i1
        self.input2 = i2
        i = 0
        while i != -1:
            i = self.execute_code(data, i)
        return data[0]

    # executes a intcode
    def execute_code(self, data, i):
        opcode, param1, param2 = self.parse_instruction(data, i) 
        return self.OPS[opcode](data, i, param1, param2)

    # parses an instruction and its parameters
    def parse_instruction(self, data, i):
        param1, param2 = 0, 0
        instruction = "0"*(5 - len(str(data[i]))) + str(data[i])    # adds missing 0's
        opcode = int(instruction[-2] + instruction[-1])
        if opcode not in [3,4,99]:
            param1 = data[i+1] if  int(instruction[-3]) else data[data[i+1]]
            param2 = data[i+2] if  int(instruction[-4]) else data[data[i+2]]

        return opcode, param1, param2


    # adds two parameters and stores in third
    def op_add(self, data, i, p1, p2):
        data[data[i+3]] = p1 + p2
        return i + 4

    # mulitplies two parameters and stores in third
    def op_mul(self, data, i, p1, p2):
        data[data[i+3]] = p1 * p2
        return i + 4

    # takes input and stores at parameter 1
    def op_in(self, data, i, *args):
        data[data[i+1]] = self.input
        self.input = self.input2
        return i + 2

    # ouputs value on parameter 1
    def op_out(self, data, i, *args):
        data[0] = data[data[i+1]]
        return i + 2

    # Jumps to parameter 2 index if parameter 1 is true
    def op_jump_if_true(self, data, i, p1, p2):
        return p2 if p1 != 0 else i +3

    # Jumps to parameter 2 index if parameter 1 is false
    def op_jump_if_false(self, data, i, p1, p2):
        return p2 if p1 == 0 else i + 3

    # sets parameter 3 to 1 if parameter 1 is less than parameter 2
    def op_less(self, data, i, p1, p2):
        data[data[i+3]] = 1 if p1 < p2 else 0
        return i + 4

    # sets parameter 3 to 1 if parameter 1 and 2 are equal
    def op_equals(self, data, i, p1, p2):
        data[data[i+3]] = 1 if p1 == p2 else 0
        return i + 4

    # halts the program
    def op_halt(self, *args):
        return -1

if __name__ == "__main__":
    data = [int(x) for x in open("input.txt", "r").read().split(",")]
    computer = Intcoder(data.copy())
    inputs = [0,1,2,3,4]
    all_inputs = list(permutations(inputs))
    results = []
    for permutation in all_inputs:
        output = 0
        for i in permutation:
            output = computer.eval(data.copy(), i, output)
        results.append(output)
 

    print(max(results))
    #print(f"Part 1 answer: {eval(data.copy())}")


