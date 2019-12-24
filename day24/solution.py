from copy import deepcopy


def part1(data):
    SEEN = [data]
    while True:
        draw(data)
        new_data = deepcopy(data)
        for y,line in enumerate(data):
            for x,c in enumerate(line):
                count = get_adjecent(x,y,data)
                if c == ".":
                    if count == 1 or count == 2:
                        new_data[y][x] = "#"
                else:
                    if count != 1:
                        new_data[y][x] = "."
        data = deepcopy(new_data)
        if new_data in SEEN:
            return get_biodiv(data)
        SEEN.append(data)

def draw(data):
    res = ""
    for line in data:
        for c in line:
            res += c
        res += "\n"
    print(res)

def get_biodiv(data):
    index = 0
    res = 0
    for line in data:
        for c in line:
            if c == "#":
                res += 2 ** index
            index += 1
    return res

def get_adjecent(x, y, data):
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    count = 0
    for d in directions:
        new_x = x + d[0]
        new_y = y + d[1]
        if out_of_bounds(new_x, new_y, data):
            continue
        if data[new_y][new_x] == "#":
            count += 1
    return count



# checks if x,y coordinates are off the grid
def out_of_bounds(x, y, data):
    if x < 0 or x > len(data[0])-1:
        return True
    elif y < 0 or y > len(data)-1:
        return True

    return False


if __name__ == "__main__":
    data = [[c for c in line.strip()] for line in open("input.txt")]

    print(f"Part 1 answer: {part1(data)}")
