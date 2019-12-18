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

def get_path(arr):
    pass

def string_to_ascii_list(string: str) -> list:
    return list(map(ord, list(string)))

main = string_to_ascii_list('A,B,C\n'
                            'R,6\n'
                            'L,10\n'
                            'R,10\n'
                            'y\n')

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

    arr = part_n(data.copy(), part=2)
    #print(part2_res)

