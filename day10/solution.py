

def part1(data):

    res = []
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == "#":
                res.append(get_below(data, x, y) +
                            get_above(data, x, y) + 
                            get_on_line(data,x , y))
    print(res)
    return max(res)

def get_below(data, x, y):
    res = []
    for i in range(len(data[0])):
        for j in range(y+1, len(data)):
            if data[j][i] == "#":
                c_x, c_y = get_relative(x, y, i, j)
                if  c_x / c_y not in res:
                    res.append(c_x / c_y)
    return len(res)

def get_above(data, x, y):
    res = []
    for i in range(len(data[0])):
        for j in range(y-1, -1, -1):
            if data[j][i] == "#":
                c_x, c_y = get_relative(x, y, i, j)
                if  c_x / c_y not in res:
                    res.append( c_x / c_y)
    return len(res)
def get_on_line(data, x, y):
    res = []
    left = 0
    right = 0
    for i in range(len(data[0])):
        if data[y][i] == "#" and i < x:
            left = 1
        if data[y][i] == "#" and i > x:
            right = 1
    return left + right

def get_relative(x, y, i, j):
    return i - x, j - y

if __name__ == "__main__":
    data = [[c for c in line.strip()] for line in open("input.txt", "r")]
    print(part1(data))
