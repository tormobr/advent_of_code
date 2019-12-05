
# Solution to part 1
def part1(w1, w2):
    grid1 = create_grid(w1)
    grid2 = create_grid(w2)
    intersections = set(grid1.keys()) & set(grid2.keys())
    return min([abs(x[0]) + abs(x[1]) for x in intersections])


# Solution to part 2
def part2(w1, w2):
    grid1 = create_grid(w1)
    grid2 = create_grid(w2)
    intersections = set(grid1.keys()) & set(grid2.keys())
    return min([grid1[x] + grid2[x] for x in intersections])

# Creates grid points based on wire instructions
def create_grid(w):
    directions = {"R": (1,0), "L": (-1,0), "U": (0,-1), "D": (0,1)}
    x,y = 0, 0
    grid = {}
    steps = 0
    for item in w:
        for i in range(int(item[1:])):
            x += directions[item[0]][0]
            y += directions[item[0]][1]
            steps += 1
            grid[(x,y)] = steps

    return grid
    
if __name__ == "__main__":
    w1,w2 = [x.split(",") for x in open("input.txt", "r").read().split("\n")][:-1]
    print(f"Part 1 answer: {part1(w1, w2)}")
    print(f"Part 2 answer: {part2(w1, w2)}")
