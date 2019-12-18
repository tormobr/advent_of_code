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


def string_to_ascii_list(s)
    return list(map(ord, list(s)))

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
        if part == 1:
            res += chr(out)
        else: 
            res = out
    return arr, res


if __name__ == "__main__":
    data = {i: int(x) for (i,x) in enumerate(open("input.txt", "r").read().split(","))}
    arr,image = part_n(data.copy(), part=1)
    part1_res = get_intersections(trim_array(arr))
    print(image) 
    print(f"Part 1 answer: {part1_res}")
    #print(find_path(trim_array(arr)))
    arr, part2_res = part_n(data.copy(), part=2)
    print(f"Part 2 answer: {part2_res}")

