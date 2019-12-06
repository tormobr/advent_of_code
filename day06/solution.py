
# solution for part 1
def part1(data):
    tree = {}
    parents = {}
    for line in data:
        A,B = line.split(")")
        if A not in tree.keys():
            tree[A] = []
        tree[A].append(B)
        parents[B] = A
    find_santa(tree, parents)
    return DFS(root, tree, 0)


def DFS(node, tree, depth):
    if leaf(node,tree): return depth
    return sum([DFS(child, tree, depth+1) for child in tree[node]])+depth

def find_santa(tree, parents):
    p = parents[me]
    ans = []
    i = 0
    while p != "COM":
        ans.append(rec(p, tree, i))
        i += 1
        p = parents[p]
    print("answer:", min(ans))

def rec (node, tree, depth):
    if node == santa: return depth-1
    elif leaf(node, tree): return 9999999
    childs = []
    for child in tree[node]:
        childs.append(rec(child, tree, depth+1))
    return min(childs)
    
        

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
    print(f"Part 1 answer: {part1(data)}")
    print(f"Part 2 answer: {part2(data)}")
