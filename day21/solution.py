from intcoder import Intcoder
from copy import deepcopy
import numpy as np



def part2(data):
    computer = Intcoder(data,0)
    inputs = []
    inputs.append("NOT A J\n")
    inputs.append("NOT B T\n")
    inputs.append("OR T J\n")
    inputs.append("NOT C T\n")
    inputs.append("OR T J\n")
    inputs.append("AND D J\n")
    inputs.append("NOT I T\n")
    inputs.append("NOT T T\n")
    inputs.append("OR F T\n")
    inputs.append("AND E T\n")
    inputs.append("OR H T\n")
    inputs.append("AND T J\n")
    inputs.append("RUN\n")
    ascii_in = [ord(c) for s in inputs for c in s]
    out = 1
    res = ""
    while out != -1:
        out = computer.eval(ascii_in)
        if out <= 0x110000 and out != -1:
            res += chr(out)
        else:
            return out
        print(res)
    return data
    

def part1(data):
    computer = Intcoder(data,0)
    inputs = []
    inputs.append("NOT A J\n")
    inputs.append("NOT B T\n")
    inputs.append("OR T J\n")
    inputs.append("NOT C T\n")
    inputs.append("OR T J\n")
    inputs.append("NOT C T\n")
    inputs.append("AND D J\n")
    inputs.append("WALK\n")
    ascii_in = [ord(c) for s in inputs for c in s]
    out = 1
    res = ""
    while out != -1:
        out = computer.eval(ascii_in)
        if out <= 0x110000 and out != -1:
            res += chr(out)
        else:
            return out
        print(res)
    return data
    


data = {i:int(x) for (i,x) in enumerate(open("input.txt", "r").read().split(","))}

print(f"Part 1 answer: {part1(data.copy())}")
print(f"Part 2 answer: {part2(data.copy())}")
