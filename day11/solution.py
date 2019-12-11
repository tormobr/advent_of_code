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
    print(H)
    max_x =100
    max_y = 100
    mid = max_x // 2
    arr = [[0 for i in range(max_x)] for j in range(max_y)]
    for key, value in H.items():
        print(key)
        arr[mid -key[1]-1][mid-key[0]] = value
    res = ""
    for y in range(max_y):
        for x in range(max_x):
            if arr[y][x] == 1:
                res += "X " 
            else:
                res += "  "
        res += "\n"
    print(res)

def part_n(data, inn):
    dirr = (0,1)
    inn = [0]
    x,y = 0, 0
    painted = {}
    out = 0
    computer = Intcoder(data, 0)
    outputs = []
    total = 0
    hax = 0
    first = True
    while out != -1:
        out = computer.eval(inn)
        if (x,y) in painted:
            total += 1
        hax += 1
        painted[(x,y)] = out
        
        out2 = computer.eval(inn)
        dirr =move(out2, dirr)
        x += dirr[0]
        y += dirr[1]
        inn.append(painted.get((x,y),0))

    pretty_print(painted)
    return len(painted)

if __name__ == "__main__":
    data = [int(x) for x in open("input.txt", "r").read().split(",")]
    data = {i:x for (i,x) in enumerate(data)}
    print(f"Part 1 answer: {part_n(data.copy(), 1)}")
    #print(f"Part 1 answer: {part_n(data.copy(), [2])}")




