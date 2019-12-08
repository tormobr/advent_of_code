from itertools import permutations

class Intcoder:
    def __init__(self, data, idd):
        self.data = data
        self.opcode = 0
        self.ip = 0
        self.current_input = 0

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
    def eval(self, i1):
        self.input = i1
        ret = None
        while ret == None:
            ret = self.execute_code()
        return ret

    # executes a intcode
    def execute_code(self):
        param1, param2 = self.parse_instruction() 
        return self.OPS[self.opcode](param1, param2)

    # parses an instruction and its parameters
    def parse_instruction(self):
        param1, param2 = 0, 0
        instruction = "0"*(5 - len(str(self.data[self.ip]))) + str(self.data[self.ip])    # adds missing 0's
        self.opcode = int(instruction[-2] + instruction[-1])
        if self.opcode not in [3,4,99]:
            param1 = self.data[self.ip+1] if  int(instruction[-3]) else self.data[self.data[self.ip+1]]
            param2 = self.data[self.ip+2] if  int(instruction[-4]) else self.data[self.data[self.ip+2]]

        return param1, param2


    # adds two parameters and stores in third
    def op_add(self, p1, p2):
        self.data[self.data[self.ip+3]] = p1 + p2
        self.ip += 4

    # mulitplies two parameters and stores in third
    def op_mul(self, p1, p2):
        self.data[self.data[self.ip+3]] = p1 * p2
        self.ip += 4

    # takes input and stores at parameter 1
    def op_in(self, *args):
        self.data[self.data[self.ip+1]] = self.input[self.current_input]
        self.current_input += 1
        self.ip += 2

    # ouputs value on parameter 1
    def op_out(self, *args):
        self.data[0] = self.data[self.data[self.ip+1]]
        self.ip += 2
        return self.data[0]

    # Jumps to parameter 2 index if parameter 1 is true
    def op_jump_if_true(self, p1, p2):
        self.ip = p2 if p1 != 0 else self.ip+3

    # Jumps to parameter 2 index if parameter 1 is false
    def op_jump_if_false(self, p1, p2):
        self.ip = p2 if p1 == 0 else self.ip+3

    # sets parameter 3 to 1 if parameter 1 is less than parameter 2
    def op_less(self, p1, p2):
        self.data[self.data[self.ip+3]] = 1 if p1 < p2 else 0
        self.ip += 4

    # sets parameter 3 to 1 if parameter 1 and 2 are equal
    def op_equals(self, p1, p2):
        self.data[self.data[self.ip+3]] = 1 if p1 == p2 else 0
        self.ip += 4

    # halts the program
    def op_halt(self, *args):
        return -1

# solves part 1 and 2 based on input phase settings
def part_n(data, inputs):
    perms = list(permutations(inputs))
    winner = 0
    for p in perms:
        computers = [Intcoder(data.copy(), x) for x in inputs]
        output = 0
        inputs = [[p] for p in p]
        inputs[0].append(0)   # The first amplifiers input
        while output != -1:
            for i in range(len(inputs)):
                output = computers[i].eval(inputs[i])
                inputs[(i+1)%len(inputs)].append(output)
                winner = output if output > winner else winner

    return winner

if __name__ == "__main__":
    data = [int(x) for x in open("input.txt", "r").read().split(",")]
    inputs1 = [0,1,2,3,4]
    inputs2 = [5,6,7,8,9]
    print(f"Part 1 answer: {part_n(data.copy(), inputs1)}")
    print(f"Part 2 answer: {part_n(data.copy(), inputs2)}")
