import math
from collections import defaultdict

# Solution for part 1 
def part1(data):
    return max([(get_angles(data,x,y, length=True), x,y) for (x,y) in data])
 
# Solution for part 2
def part2(data, x, y):
    R,_ = get_angles(data, x, y)
    R = [(k, R[k]) for k in reversed(sorted(R.keys()))]
    return (x +R[199][1][-1][0])*100 + (y+R[199][1][-1][1])     # Kinda hacky, but works

# Creates a dict over possible angles, and the gridpoints as values
def get_angles(data, x, y, length=False):
    hax = defaultdict(lambda : list())
    for x2, y2 in data:
        r_x, r_y = get_relative(x, y, x2, y2)
        k = math.atan2(r_x, r_y)
        hax[k].append((r_x, r_y))
    if length: return len(hax)
    return hax,len(hax)
            
# gets the relative grid x,y from a starting point
def get_relative(x, y, i, j):
    return i - x, j - y

if __name__ == "__main__":
    lines = [line for line in open("input.txt", "r")]
    data = [(x,y) for y in range(len(lines)) for x in range(len(lines[y])) if lines[y][x] == "#"]
    maxx, x, y = part1(data)
    print(f"Part 1 answer: {maxx}")
    print(f"Part 2 answer: {part2(data, x, y)}")

