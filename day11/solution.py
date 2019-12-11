from intcoder import Intcoder

def move(n, dirr):
    if dirr[1] == 1 and n == 0:
        dirr = [1,0]
    elif dirr[1] == -1 and n == 0:
        dirr = [-1,0]

    elif dirr[0] == 1 and n == 0:
        dirr = [0,-1]
    elif dirr[0] == -1 and n == 0:
        dirr = [0,1]


    elif dirr[1] == 1 and n == 1:
        dirr = [-1,0]
    elif dirr[1] == -1 and n == 1:
        dirr = [1,0]

    elif dirr[0] == 1 and n == 1:
        dirr = [0,1]
    elif dirr[0] == -1 and n == 1:
        dirr = [0,-1]

    return dirr

def pretty_print(H):
    max_x, max_y, min_x, min_y = get_dimensions(H)
    arr = [[0 for i in range(max_x)] for j in range(max_y)]
    for key, value in H.items():
        c_x = key[0] + abs(min_x)
        c_y = key[1] + abs(min_y)
        arr[c_y][c_x] = value
    res = ""
    for y in range(max_y):
        for x in range(max_x):
            if arr[y][x] == 1:
                res += "X " 
            else:
                res += "  "
        res += "\n"
    return res

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
    dirr = (0,-1)
    x,y = 0, 0
    painted = {}
    out = 0
    computer = Intcoder(data, 0)
    first = True
    while out != -1:
        out = computer.eval(inn)
        hax += 1
        painted[(x,y)] = out
        
        out2 = computer.eval(inn)
        dirr =move(out2, dirr)
        x += dirr[0]
        y += dirr[1]
        inn.append(painted.get((x,y),0))

    pretty_print(painted)
    return painted, len(painted)

if __name__ == "__main__":
    data = [int(x) for x in open("input.txt", "r").read().split(",")]
    data = {i:x for (i,x) in enumerate(data)}
    print(f"Part 1 answer: {part_n(data.copy(), [0])[1]}")
    print(f"Part 2 answer:\n{pretty_print(part_n(data.copy(), [1])[0])}")




