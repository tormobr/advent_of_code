import numpy as np
from matplotlib import pyplot as plt
# solution for part 1
def part1(data):
    res = []
    for i, A in enumerate(data):
        zeros = 0 
        for j, B in enumerate(A):
            for C in B:
                if C == 0:
                    zeros += 1
        res.append([i, zeros])
    
    maxx = min(res, key=lambda x: x[1])[0]
    ones = 0
    twos = 0
    for A in data[maxx]:
        for B in A:
            if B == 1:
                ones += 1
            elif B == 2:
                twos += 1
    return ones * twos

# solution for part 2 
def part2(data):
    result = [[0]*25 for i in range(6)]
    for x in range(25):
        for y in range(6):
            layer = 0
            while data[layer][y][x] == 2:
                layer += 1
            result[y][x] = data[layer][y][x]
    return result

                

if __name__ == "__main__":
    str_data = open("input.txt", "r").read()
    width = 25
    height  = 6
    x, y = 0, 0 
    data = [[]]
    index = 0
    hax = 0
    while index < len(str_data) -1:
        data.append([])
        for i in range(height):
            data[hax].append([])
            for j in range(width):
                data[hax][i].append(int(str_data[index]))
                index +=1
        hax += 1
    print(f"Part 1 answer: {part1(data[:-1])}")
    #print(f"Part 2 answer: {part2(data[:-1])}")
    res = part2(data[:-1])
    hax = ""
    for i, x in enumerate(res) :
        for j, strudel in enumerate(x):
            if strudel == 0:
                hax += "  "
            else: 
                hax += "X "
        hax += "\n"

    print(res)
    print(hax) 
