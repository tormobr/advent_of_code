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
        self.data = data
        self.opcode = 0
        self.ip = 0

    # Solution to part 1 and two
    def eval(self, i1, i2):
        self.input = i1
        self.input2 = i2
        ret = 0
        while ret != -1:
            ret = self.execute_code()
            if self.opcode == 4:
                return self.data[0]
        return -1

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
        #print("inputting: ", self.input)
        self.data[self.data[self.ip+1]] = self.input
        self.input = self.input2
        self.ip += 2

    # ouputs value on parameter 1
    def op_out(self, *args):
        self.data[0] = self.data[self.data[self.ip+1]]
        self.ip += 2

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

if __name__ == "__main__":
    data = [int(x) for x in open("input.txt", "r").read().split(",")]
    inputs = [5,6,7,8,9]
    #inputs = [0,1,2,3,4]
    all_inputs = [list(p) for p in list(permutations(inputs))]
    results = []
    for inputs in all_inputs:
        computers = [Intcoder(data.copy()) for _ in range(5)]
        output = 0
        first = True
        outputs = inputs.copy()
        while output != -1:
            for index,i in enumerate(inputs):
                print(inputs)
                output = computers[index].eval(i, output)
                outputs[(index+1)%5] = output

            results.append(output)
            inputs = outputs
 

    print(max(results))
    #print(f"Part 1 answer: {eval(data.copy())}")
