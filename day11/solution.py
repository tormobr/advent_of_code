import numpy as np
from itertools import permutations

class Intcoder:
    def __init__(self, data, idd):
        self.data = data
        self.opcode = 0
        self.ip = 0
        self.current_input = 0
        self.relative_base = 0
        self.output = ""

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
            9: self.set_relative_base,
            99: self.op_halt
        }
        self.num_params = {
            1: 3,
            2: 3,
            3: 1,
            4: 1,
            5: 3,
            6: 3,
            7: 3,
            8: 3,
            9: 1,
            99: 0
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
        param1, param2, param3 = self.parse_instruction() 
        return self.OPS[self.opcode](param1, param2, param3)

    # 21199
    # parses an instruction and its parameters
    def parse_instruction(self):
        param1, param2, param3 = 0, 0, 0 
        parameter_base = 2
        params = [param1, param2, param3]
        instruction = "0"*(5 - len(str(self.data[self.ip]))) + str(self.data[self.ip])
        self.opcode = int(instruction[-2] + instruction[-1])
        for i in range(self.num_params[self.opcode]):
            if int(instruction[parameter_base-i]) == 1:
                params[i] = self.ip+i+1
            elif int(instruction[parameter_base-i]) == 2:
                params[i] = self.data[self.ip+i+1] + self.relative_base
            else:
                params[i] = self.data.get(self.ip+i+1, 0 )

        return params


    # adds two parameters and stores in third
    def op_add(self, p1, p2, p3):
        self.data[p3] = self.data.get(p1, 0) + self.data.get(p2, 0)
        self.ip += 4

    # mulitplies two parameters and stores in third
    def op_mul(self, p1, p2, p3):
        self.data[p3] = self.data.get(p1, 0) * self.data.get(p2, 0)
        self.ip += 4

    # takes input and stores at parameter 1
    def op_in(self, p1, *args):
        self.data[p1] = self.input
        self.current_input += 1
        self.ip += 2

    # ouputs value on parameter 1
    def op_out(self, p1, *args):
        self.output += str(self.data.get(p1, 0))
        #self.data[0] = param1
        self.ip += 2
        return self.data.get(p1,0)

    # Jumps to parameter 2 index if parameter 1 is true
    def op_jump_if_true(self, p1, p2, *args):
        self.ip = self.data.get(p2, 0) if self.data.get(p1, 0) != 0 else self.ip+3

    # Jumps to parameter 2 index if parameter 1 is false
    def op_jump_if_false(self, p1, p2, *args):
        self.ip = self.data.get(p2, 0) if self.data.get(p1, 0) == 0 else self.ip+3

    # sets parameter 3 to 1 if parameter 1 is less than parameter 2
    def op_less(self, p1, p2, p3):
        self.data[p3] = 1 if self.data.get(p1, 0) < self.data.get(p2, 0) else 0
        self.ip += 4

    # sets parameter 3 to 1 if parameter 1 and 2 are equal
    def op_equals(self, p1, p2, p3):
        self.data[p3] = 1 if self.data.get(p1, 0) == self.data.get(p2, 0) else 0
        self.ip += 4

    def set_relative_base(self, p1, *args):
        self.relative_base += self.data.get(p1, 0)
        self.ip += 2

    # halts the program
    def op_halt(self, *args):
        return -1

def move(n, dirr):
    if dirr[1] == 1 and n == 0:
        dirr = [1,0]
    elif dirr[1] == -1 and n == 0:
        dirr = [-1,0]

    elif dirr[0] == 1 and n == 0:
        dirr = [0,-1]
    elif dirr[0] == -1 and n == 0:
        dirr = [0,1]


    elif dirr[1] == 1 and n == 1:
        dirr = [-1,0]
    elif dirr[1] == -1 and n == 1:
        dirr = [1,0]

    elif dirr[0] == 1 and n == 1:
        dirr = [0,1]
    elif dirr[0] == -1 and n == 1:
        dirr = [0,-1]

    return dirr

def pretty_print(H):
    print(H)
    max_x = 300
    max_y = 300
    arr = [[0 for i in range(max_x)] for j in range(max_y)]
    for key, value in H.items():
        print(key)
        arr[key[1]-1][key[0]] = value
    res = ""
    for y in range(max_y):
        for x in range(max_x):
            if arr[y][x] == 1:
                res += "X " 
            else:
                res += "  "
        res += "\n"
    print(res)

def part_n(data, inn):
    dirr = (0,1)
    inn = 1
    x,y = 0, 0
    painted = {}
    out = 0
    computer = Intcoder(data, 0)
    outputs = []
    total = 0
    hax = 0
    first = True
    while out != -1:
        if not first:
            inn = painted.get((x,y),0)
        else:
            first = False
            inn = 1
        out = computer.eval(inn)
        if (x,y) in painted:
            total += 1
        hax += 1
        painted[(x,y)] = out
        
        out2 = computer.eval(inn)
        dirr =move(out2, dirr)
        x += dirr[0]
        y += dirr[1]
        if out != -1:
            outputs.append(out)
    pretty_print(painted)
    return len(painted)

if __name__ == "__main__":
    data = [int(x) for x in open("input.txt", "r").read().split(",")]
    data = {i:x for (i,x) in enumerate(data)}
    print(f"Part 1 answer: {part_n(data.copy(), 1)}")
    #print(f"Part 1 answer: {part_n(data.copy(), [2])}")




