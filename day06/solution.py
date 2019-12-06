
# solution for part 1
def part1(data):
    tree = {}
    for line in data:
        A,B = line.split(")")
        if A not in tree.keys():
            tree[A] = []
        tree[A].append(B)
    return DFS(root, tree, 0)


def DFS(node, tree, depth):
    if leaf(node,tree): return depth
    return sum([DFS(child, tree, depth+1) for child in tree[node]])+depth


def leaf(node, tree):
    return node not in tree.keys()

# solution for part 2
def part2(data):
    pass

root = "COM"
me = "YOU"
santa = "SAN"

if __name__ == "__main__":
    data = open("input.txt", "r").read().split("\n")[:-1]
    print(data)
    print(f"Part 1 answer: {part1(data)}")
    print(f"Part 2 answer: {part2(data)}")
