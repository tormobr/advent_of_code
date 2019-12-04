
def create_grid(w):
    directions = {"R": (1,0), "L": (-1,0), "U": (0,-1), "D": (0,1)}
    x,y = 0, 0
    grid = []
    for item in w:
        for i in range(int(item[1:])):
            x += directions[item[0]][0]
            y += directions[item[0]][1]
            grid.append((x,y))

    return grid

def task1(filename):
    w1,w2,_ = [x.split(",") for x in open(filename, "r").read().split("\n")]

    grid1 = create_grid(w1)
    grid2 = create_grid(w2)
    combined = set(grid1) & set(grid2)
    return min([abs(x[0]) + abs(x[1]) for x in combined])


print(task1("input.txt"))
