from copy import deepcopy

class level:
    def __init__(self, parent, child, depth, data=None):
        self.data = data
        self.parent = parent
        self.child = child
        self.depth = depth
        self.top = (2,1)
        self.bottom = (2,3)
        self.left = (1,2)
        self.right = (3,2)

    def iteration(self):
        new_data = deepcopy(self.data)
        for y,line in enumerate(self.data):
            for x,c in enumerate(line):
                count = self.get_adjecent(x,y,self.data)
                if c == ".":
                    if count == 1 or count == 2:
                        new_data[y][x] = "#"
                else:
                    if count != 1:
                        new_data[y][x] = "."
        self.data = deepcopy(new_data)

        if new_data in SEEN:
            return get_biodiv(data)
        SEEN.append(data)
        pass

    def get_adjecent(self, x, y, data):
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        count = 0
        for d in directions:
            new_x = x + d[0]
            new_y = y + d[1]
            if out_of_bounds(new_x, new_y, data):
                continue
            if data[new_y][new_x] == "#":
                count += 1
        return count

    def __repr__(self):
        res = ""
        for line in grid:
            for c in line:
                res += c
            res += "\n"
        return res
