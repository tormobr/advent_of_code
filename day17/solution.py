import time
from intcoder import Intcoder


def get_intersections(arr):
    intersections = 0
    for y in range(1, len(arr)-1):
        for x in range(1, len(arr[0])-1):
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

def part1(data):
    computer = Intcoder(data, 0)

    arr = [[]]
    current_y = 0
    res = ""
    while True:
        out = computer.eval(None)
        if out == -1:
            break
        if out == 10:
            arr.append([])
            current_y += 1
        else:
            arr[current_y].append(chr(out))
        print(out)
        res += chr(out)
    arr = trim_array(arr)
    hax = get_intersections(arr)
    return res, hax
if __name__ == "__main__":
    data = {i: int(x) for (i,x) in enumerate(open("input.txt", "r").read().split(","))}
    image, part1_res = part1(data)
    print(image) 
    print(part1_res)

