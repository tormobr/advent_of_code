
# solution for part 1
def part1(data):
    tree, parents = get_trees(data)
    return DFS(root, tree, 0)

# solution for part 2
def part2(data):
    tree, parents = get_trees(data)
    return find_santa(tree, parents)

# gets the direct and indirect obits using depth first search
def DFS(node, tree, depth):
    if leaf(node,tree): return depth
    return sum([DFS(child, tree, depth+1) for child in tree[node]])+depth

# moves ups parents of "YOU" and look for santas parent
def find_santa(tree, parents):
    p, ret, i = parents[me], -1, 0
    while ret == -1:
        ret = find_santa_recursion(p, tree, i)
        i += 1
        p = parents[p]
    return ret


# Recursively checks if santa is a child of a node
def find_santa_recursion (node, tree, depth):
    if node == santa: return depth -1
    elif leaf(node, tree): return -1
    return max([find_santa_recursion(child, tree, depth+1) for child in tree[node]])

# Checks if a node is a leaf node(no kids)
def leaf(node, tree):
    return node not in tree.keys()


# Generates a couple of dicts for the parent-kid relationships
def get_trees(data):
    parents, tree = {}, {}
    for line in data:
        A,B = line.split(")")
        if A not in tree.keys():
            tree[A] = []
        tree[A].append(B)
        parents[B] = A
    return tree, parents


# Just some juicy vars
root = "COM"
me = "YOU"
santa = "SAN"

if __name__ == "__main__":
    data = open("input.txt", "r").read().split("\n")[:-1]
    print(f"Part 1 answer: {part1(data)}")
    print(f"Part 2 answer: {part2(data)}")
