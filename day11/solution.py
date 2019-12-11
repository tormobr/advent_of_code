from collections import defaultdict
import numpy as np
from intcoder import Intcoder


# Prints the painting in a nice way
def pretty_print(H, minmax):
    max_x, max_y = get_dimensions(H, minmax)
    min_x, min_y = minmax[1], minmax[3]
    print(max_x, max_y)
    arr = np.zeros((max_y, max_x), dtype=str)
    for key, value in H.items():
        c_x = key[0] + abs(min_x)
        c_y = key[1] + abs(min_y)
        arr[c_y][c_x] = value

    arr = np.where(arr != "1", "  ", arr)
    arr = np.where(arr == "1", "\u2b1c", arr)
    arr = np.concatenate([arr, [["\n"]]*max_y], axis=1)
    return "".join(np.reshape(arr, ((max_x+1)*max_y)))

# Gets the dimensions needed for the painted pic
def get_dimensions(H, minmax):
    #arr = [key for key in H.keys()]
    #max_x = max(arr, key=lambda x: x[0])[0]
    #max_y = max(arr, key=lambda x: x[1])[1]
    #min_x = min(arr, key=lambda x: x[0])[0]
    #min_y = min(arr, key=lambda x: x[1])[1]
    dim_x = abs(minmax[1]) + abs(minmax[0]) + 1
    dim_y = abs(minmax[2]) + abs(minmax[3]) + 1 
    return dim_x, dim_y


def test_new_minmax(x,y, minmax):
    if x > minmax[0]: minmax[0] = x
    if x < minmax[1]: minmax[1] = x
    if y > minmax[2]: minmax[2] = y
    if y < minmax[3]: minmax[3] = y

# Solves part one and part 2
def part_n(data, inn):
    computer = Intcoder(data, 0)
    directions = [(0,-1), (1,0), (0,1), (-1,0)]
    minmax = [0,0,0,0]
    x, y, color, dir_index = 0, 0, 0, 0
    painted = defaultdict(int)

    while color != -1:
        color = computer.eval(inn)
        painted[(x,y)] = color
        test_new_minmax(x,y,minmax)

        turn_dir = computer.eval(inn)
        dir_index += 1 if turn_dir else -1
        x += directions[dir_index%4][0]
        y += directions[dir_index%4][1]
        inn.append(painted[(x,y)])

    return painted, len(painted), minmax

if __name__ == "__main__":
    data = [int(x) for x in open("input.txt", "r").read().split(",")]
    data = {i:x for (i,x) in enumerate(data)}
    print(f"Part 1 answer: {part_n(data.copy(), [0])[1]}")
    H,length,minmax = part_n(data.copy(), [1])
    print(f"Part 2 answer:\n{pretty_print(H, minmax)}")
