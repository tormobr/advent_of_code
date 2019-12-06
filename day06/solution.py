
# solution for part 1
def part1(data):
    tree = {}
    for line in data:
        A,B = line.split(")")
        if A not in orbits.keys():
            tree[A] = []
        tree[A].append(B)
    print(tree)
print(tree)


def hax(node):
    pass 

# solution for part 2
def part2(data):
    pass


if __name__ == "__main__":
    data = [line[:-1] for line in open("input.txt", "r")]
    print(f"Part 1 answer: {part1(data)}")
    print(f"Part 2 answer: {part2(data)}")
