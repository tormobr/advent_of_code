
import numpy as np
# solution for part 1
def part1(data, width, height):
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
def part2(data, width, height):
    result = np.zeros((height, width))
    for x in range(width):
        for y in range(height):
            layer = 0
            while data[layer][y][x] == 2:
                layer += 1
            result[y][x] = data[layer][y][x]
    return result

# Reads the string data into a 3d array of grids
def parse_file(str_data, width, height):
    index = 0
    layers = len(str_data)//(width*height)
    data = np.zeros((layers, height ,width))
    for i in range(layers):
        for j in range(height):
            data[i][j] = np.array([int(c) for c in str_data[index:index+width]])
            index += width
    return data


def pretty_print(data):
    output = ""
    for line in data :
        for elem in line:
            output += "  " if elem == 0 else "X " 
        output += "\n"
    return output

if __name__ == "__main__":
    str_data = open("input.txt", "r").read()
    width = 25
    height  = 6
    data = parse_file(str_data, width, height)

    print(f"Part 1 answer: {part1(data, width, height)}")
    part2_res = part2(data, width, height)
    print(f"Part 2 answer:\n{pretty_print(part2_res)}")
