import time
from intcoder import Intcoder


def get_intersections(arr):
    intersections = 0
    for y in range(1, len(arr)-1):
        for x in range(1, len(arr[y])-1):
            if arr[y][x] == "#":
                if arr[y+1][x] != "#" or arr[y-1][x] != "#":
                    continue
                elif arr[y][x+1] != "#" or arr[y][x-1] != "#":
                    continue
                intersections += x*y
    return intersections

# removes 0 arrays from 2d array
def trim_array(arr):
    ret = []
    for line in arr:
        if not len(line) == 0:
            ret.append(line)
    return ret

def find_path(grid):
    for i, r in enumerate(grid):
        for j, p in enumerate(r):
            if p == '^':
                x, y = j, i
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    dirs = []
    c = -1
    l = 'R'
    d = 1
    while True:
        c+=1
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid) and grid[ny][nx] == '#':
            x, y = nx, ny
            continue
        if y+1 < len(grid) and grid[y+1][x] == '#':
            print("this should at least happend")
            if (x, y+1) != (x-dx[d], y-dy[d]):
                dirs.append((l, c))
                l = 'R' if d == 1 else 'L'
                d = 2
                c = 0
                x, y = x, y + 1
                print ("this does never happen")
                continue
        if 0 <= y-1 and grid[y-1][x] == '#':
            print("this should at least happend")
            if (x, y-1) != (x-dx[d], y-dy[d]):
                dirs.append((l, c))
                l = 'L' if d == 1 else 'R'
                d = 0
                c = 0
                x, y = x, y - 1
                print ("this does never happen")
                continue
        if x+1 < len(grid[0]) and grid[y][x+1] == '#':
            print("this should at least happend")
            if (x+1, y) != (x-dx[d], y-dy[d]):
                dirs.append((l, c))
                l = 'R' if d == 0 else 'L'
                d = 1
                c = 0
                x, y = x+1, y
                print ("this does never happen")
                continue
        if 0 <= x-1 and grid[y][x-1] == '#':
            print("this should at least happend")
            if (x-1, y) != (x-dx[d], y-dy[d]):
                dirs.append((l, c))
                l = 'L' if d == 0 else 'R'
                d = 3
                c = 0
                x, y = x-1, y
                print ("this does never happen")
                continue
        break
    dirs.append((l, c))
    return ''.join([l+str(d)for l,d in dirs])

def string_to_ascii_list(string: str) -> list:
    return list(map(ord, list(string)))

main = string_to_ascii_list('A,B,A,B,A,C,A,C,B,C\n'
                            'R,6,L,10,R,10,R,10\n'
                            'L,10,L,12,R,10\n'
                            'R,6,L,12,L,10\n'
                            'n\n')

def part_n(data, part=1):
    computer = Intcoder(data, 0)
    if part == 2: 
        data[0] = 2 

    arr = [[]]
    current_y = 0
    res = ""
    while True:
        out = computer.eval(main)
        if out == -1:
            break
        if out == 10:
            arr.append([])
            current_y += 1
        else:
            arr[current_y].append(chr(out))
        res += chr(out)
    print(res)
    return arr, res


if __name__ == "__main__":
    data = {i: int(x) for (i,x) in enumerate(open("input.txt", "r").read().split(","))}
    arr,image = part_n(data.copy(), part=1)
    part1_res = get_intersections(trim_array(arr))
    print(image) 
    print(f"Part 1 answer: {part1_res}")
    #print(find_path(trim_array(arr)))
    arr = part_n(data.copy(), part=2)
    #print(part2_res)

