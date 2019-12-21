import time
from collections import defaultdict
import re

# solution for part 1
def part1(data):
    ores = []
    spare = defaultdict(int)
    execute_reactions(data, "FUEL", 1,ores,spare)

    return sum(ores)

# solution for part 2
def part2(data):
    h = 100004302010
    l = 1
    c = (h + l) // 2
    spare = defaultdict(int)
    return bisection(l, h, data, spare, 1000000000000)

def bisection(l, h, data, spare, n ):
    c = (h + l) // 2
    while l < c  and c < h:
        ores = []
        execute_reactions(data, "FUEL", c,ores,spare)
        res = sum(ores)
        l, h, c = set_boundary(l, h, c, res, n)
    return l,c,h, sum(ores)

def set_boundary(l, h, c, res, n):
    if res > n:
        h = c
        c = (h + l) // 2
    else: 
        l = c
        c = (h + l) // 2
    return l, h, c
    
    

def execute_reactions(data, current, needed, ores,spare):
    gets = data[current]["val"]
    reactants = data[current]["reac"]
    mul = (needed // gets)
    if gets*mul < needed:
        mul += 1
    new_gets = (mul*gets)
    if spare[current] >= needed:
        spare[current] -= needed
        return
    if spare[current] !=0 and needed - spare[current] <= data[current]["val"]*(mul-1):
        needed -= spare[current]
        spare[current] = data[current]["val"]*(mul-1)-needed
        mul -= 1
    else:
        spare[current] += new_gets - needed
    if reactants[0][1] == "ORE":
        ores.append(reactants[0][0]*mul)
        return

    # recursive calls
    for reac in reactants:
        execute_reactions(data, reac[1], reac[0]*mul, ores,spare)

if __name__ == "__main__":
    data = {}
    with open("input.txt") as f:
        for line in f:
            line = line.strip()
            line = line.split("=>")
            strudels = line[0].split(",")
            product = line[1]
            for i,elem in enumerate(strudels):
                splitted = elem.split()
                strudels[i] = (int(splitted[0]), splitted[1])
            hax = product.split()
            product = hax[1]
            reactants = {"reac": strudels, "val": int(hax[0])}
            data[product] = reactants

    print(f"Part 1 answer: {part1(data)}")
    print(f"Part 2 answer: {part2(data)}")
