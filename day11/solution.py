import numpy as np
from intcoder import Intcoder

def pretty_print(H):
    max_x, max_y, min_x, min_y = get_dimensions(H)
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

def get_dimensions(H):
    arr = [key for key in H.keys()]
    max_x = max(arr, key=lambda x: x[0])[0]
    max_y = max(arr, key=lambda x: x[1])[1]
    min_x = min(arr, key=lambda x: x[0])[0]
    min_y = min(arr, key=lambda x: x[1])[1]
    dim_x = abs(min_x) + abs(max_x) + 1
    dim_y = abs(min_y) + abs(max_y) + 1 
    return dim_x, dim_y, min_x, min_y

def part_n(data, inn):
    computer = Intcoder(data, 0)
    directions = [(0,-1), (1,0), (0,1), (-1,0)]
    dirr_index = 0
    x,y = 0, 0
    painted = {}
    out = 0

    while out != -1:
        out = computer.eval(inn)
        painted[(x,y)] = out

        out2 = computer.eval(inn)
        dirr_index += 1 if out2 else -1
        x += directions[dirr_index%4][0]
        y += directions[dirr_index%4][1]
        inn.append(painted.get((x,y),0))

    return painted, len(painted)

if __name__ == "__main__":
    data = [int(x) for x in open("input.txt", "r").read().split(",")]
    data = {i:x for (i,x) in enumerate(data)}
    print(f"Part 1 answer: {part_n(data.copy(), [0])[1]}")
    print(f"Part 2 answer:\n{pretty_print(part_n(data.copy(), [1])[0])}")




