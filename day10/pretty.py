import math
def part1(data):
    return max([get_angles(data, item[0], item[1]) for item in data], key=lambda x: x[1])

def get_angles(data, x, y):
    hax = {}
    for item in data:
        c_x, c_y = get_relative(x, y, item[0], item[1])
        k = math.atan2(c_x, c_y)
        if k not in hax :
            hax[k] = []
        hax[k].append((c_x, c_y))

    return hax,len(hax)
            
def part2(data, x, y):
    R = get_angles(data, x, y)
    R = [(k, R[k]) for k in reversed(sorted(R.keys()))]
    
    return R[199]

    return R, len(R)

def get_relative(x, y, i, j):
    return i - x, j - y

if __name__ == "__main__":
    lines = [line for line in open("input.txt", "r")]
    data = [(x,y) for y in range(len(lines)) for x in range(len(lines[y])) if lines[y][x] == "#"]
    print(part1(data)[1])
    #print(part2(data, 26, 36))

