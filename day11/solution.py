from collections import defaultdict
import numpy as np
from intcoder import Intcoder

# Prints the painting in a nice way
def pretty_print(H, minmax):
    dim_x = abs(minmax[1]) + abs(minmax[0]) + 1
    dim_y = abs(minmax[2]) + abs(minmax[3]) + 1 
    min_x, min_y = minmax[1], minmax[3]
    arr = np.zeros((dim_y, dim_x), dtype=str)
    # Fill array at coordinates with values
    for k, value in H.items():
        arr[k[1]+abs(min_y)][k[0]+abs(min_x)] = value
    
    # Replace 1 and 0 with more readable stuff
    arr = np.where(arr != "1", "  ", arr)
    arr = np.where(arr == "1", "\u2b1c", arr)
    arr = np.concatenate([arr, [["\n"]]*dim_y], axis=1)
    return "".join(np.reshape(arr, ((dim_x+1)*dim_y)))

# Check if current x or y is new low or high
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

    # While intcode program is not done paint new square and move
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
