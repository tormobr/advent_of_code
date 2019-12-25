from intcoder import Intcoder

# Solution for part 1 and 2
def part1(data, part=1):
    computer = Intcoder(data,0)
    if part == 1:
        ascii_in = [ord(c) for c in program1()]
    else: 
        ascii_in = [ord(c) for c in program2()]
    out = 1
    while out != -1:
        out = computer.eval(ascii_in)
        if out > 255:
            return out
    return -1 

# fetches spring script program 1
def program1():
    return  "".join([line for line in open("prog1.txt")])

# fetches spring script program 2
def program2():
    return  "".join([line for line in open("prog2.txt")])

if __name__ == "__main__":
    data = {i:int(x) for (i,x) in enumerate(open("input.txt", "r").read().split(","))}

    print(f"Part 1 answer: {part1(data.copy())}")
    print(f"Part 2 answer: {part1(data.copy(), part=2)}")
