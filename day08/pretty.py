import numpy as np
# solution for part 1
def part1(data, width, height, layers):
    maxx = min([(np.count_nonzero(data[i] == 0),i) for i in range(layers)], key=lambda x: x[0])
    ones = np.count_nonzero(data[maxx[1]] == 1)
    twos = np.count_nonzero(data[maxx[1]] == 2)
    return ones * twos

# solution for part 2 
def part2(data, width, height, layers):
    result = data[0]
    for i in range(1, layers):
        result = np.where(result != 2, result, data[i])
    return result

# Reads the string data into a 3d array of grids
def parse_file(data, width, height, layers):
    data = np.reshape(data, (layers, height,width))
    return data

# Creates a nice readable string from the result matrix
def pretty_print(data):
    output = ""
    for line in data :
        for elem in line:
            output += "  " if elem == 0 else "X " 
        output += "\n"
    return output


if __name__ == "__main__":
    str_data = np.array(list(open("input.txt", "r").read().strip()), dtype=int)
    width = 25
    height  = 6
    layers = len(str_data)//(width*height)
    data = parse_file(str_data, width, height, layers)

    print(f"Part 1 answer: {part1(data, width, height, layers)}")
    part2_res = part2(data, width, height, layers)
    print(f"Part 2 answer:\n{pretty_print(part2_res)}")
