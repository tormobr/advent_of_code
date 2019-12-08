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
        self.exit_ip = 0

    # Solution to part 1 and two
    def eval(self, i1, i2):
        self.input = i1
        self.input2 = i2
        i = self.exit_ip
        while i != -1:
            i = self.execute_code(i)
            if self.opcode == 4:
                print("output returning", data[i:i+10], " value: ", self.data[0])
                self.exit_ip = i
                return self.data[0]
        return -1

    # executes a intcode
    def execute_code(self, i):
        param1, param2 = self.parse_instruction(i) 
        return self.OPS[self.opcode](i, param1, param2)

    # parses an instruction and its parameters
    def parse_instruction(self, i):
        param1, param2 = 0, 0
        instruction = "0"*(5 - len(str(self.data[i]))) + str(self.data[i])    # adds missing 0's
        self.opcode = int(instruction[-2] + instruction[-1])
        if self.opcode not in [3,4,99]:
            param1 = self.data[i+1] if  int(instruction[-3]) else self.data[self.data[i+1]]
            param2 = self.data[i+2] if  int(instruction[-4]) else self.data[self.data[i+2]]

        return param1, param2


    # adds two parameters and stores in third
    def op_add(self, i, p1, p2):
        self.data[self.data[i+3]] = p1 + p2
        return i + 4

    # mulitplies two parameters and stores in third
    def op_mul(self, i, p1, p2):
        self.data[self.data[i+3]] = p1 * p2
        return i + 4

    # takes input and stores at parameter 1
    def op_in(self, i, *args):
        print("inputting: ", self.input)
        self.data[self.data[i+1]] = self.input
        self.input = self.input2
        return i + 2

    # ouputs value on parameter 1
    def op_out(self, i, *args):
        self.data[0] = self.data[self.data[i+1]]
        return i + 2

    # Jumps to parameter 2 index if parameter 1 is true
    def op_jump_if_true(self, i, p1, p2):
        return p2 if p1 != 0 else i +3

    # Jumps to parameter 2 index if parameter 1 is false
    def op_jump_if_false(self, i, p1, p2):
        return p2 if p1 == 0 else i + 3

    # sets parameter 3 to 1 if parameter 1 is less than parameter 2
    def op_less(self, i, p1, p2):
        self.data[self.data[i+3]] = 1 if p1 < p2 else 0
        return i + 4

    # sets parameter 3 to 1 if parameter 1 and 2 are equal
    def op_equals(self, i, p1, p2):
        self.data[self.data[i+3]] = 1 if p1 == p2 else 0
        return i + 4

    # halts the program
    def op_halt(self, *args):
        return -1

if __name__ == "__main__":
    data = [int(x) for x in open("input.txt", "r").read().split(",")]
    inputs = [5,6,7,8,9]
    #inputs = [0,1,2,3,4]
    all_inputs = list(permutations(inputs))
    results = []
    for permutation in all_inputs:
        computers = [Intcoder(data.copy()) for _ in range(5)]
        output = 0
        first = True
        while output != -1:
            for index,i in enumerate(permutation):
                if first:
                    output = computers[index].eval(i, output)
                else: 
                    output = computers[index].eval(output, output)
                results.append(output)

            first = False
 

    print(max(results))
    #print(f"Part 1 answer: {eval(data.copy())}")
