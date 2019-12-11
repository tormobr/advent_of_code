import math
def part1(data):
    best = 0
    xy = (0,0)
    for x,y in data:
        angles, length = get_angles(data, x, y)
        if length > best:
            best = length
            xy = (x,y)
    return best, xy
 
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
    R,_ = get_angles(data, x, y)
    R = [(k, R[k]) for k in reversed(sorted(R.keys()))]
    return x +R[199][1][0][0], y+R[199][1][0][1]

def get_relative(x, y, i, j):
    return i - x, j - y

if __name__ == "__main__":
    lines = [line for line in open("input.txt", "r")]
    data = [(x,y) for y in range(len(lines)) for x in range(len(lines[y])) if lines[y][x] == "#"]
    maxx, xy = part1(data)
    print(maxx)
    print(part2(data, xy[0], xy[1]))

