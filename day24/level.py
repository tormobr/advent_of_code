from copy import deepcopy
import numpy as np

class Level:
    def __init__(self, depth=0, data=None, ID=None):
        self.ID = ID
        self.data = data
        self.nexxt = None
        self.depth = depth
        self.parent = None
        self.child = None
        self.inner = {
            "top": (2,1),
            "bottom": (2,3),
            "left": (1,2),
            "right": (3,2)
        }

    def set_parent(self, parent=None, child=None):
        self.child = child
        self.parent = parent

    def iteration(self):
        self.nexxt = deepcopy(self.data)
        for y,line in enumerate(self.data):
            for x,c in enumerate(line):
                if y == 2 and x == 2:
                    continue
                count = self.get_adjecent(x,y,self.data)
                if c == 0:
                    if count == 1 or count == 2:
                        self.nexxt[y][x] = 1
                else:
                    if count != 1:
                        self.nexxt[y][x] = 0

    def set_nexxt(self):
        self.data = deepcopy(self.nexxt)

    def set_data(self, data):
        self.data = data

    def get_adjecent(self, x, y, data):
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        count = 0
        if x == 2 == y:
            return
        
        count += self.check_child_parent(x,y)

        for d in directions:
            new_x = x + d[0]
            new_y = y + d[1]
            if self.out_of_bounds(new_x, new_y, data):
                continue
            if data[new_y][new_x] == 1:
                count += 1
        return count

    # checks if x,y coordinates are off the grid
    def out_of_bounds(self, x, y, data):
        if x < 0 or x > len(data[0])-1:
            return True
        elif y < 0 or y > len(data)-1:
            return True

        return False

    def check_child_parent(self, x, y):
        count = 0
        if self.parent:
            parent_data = self.parent.data
            if y == 0:
                parent_top = self.parent.inner["top"]
                count += parent_data[parent_top[1]][parent_top[0]]
            if y == 4:
                parent_bottom = self.parent.inner["bottom"]
                count += parent_data[parent_bottom[1]][parent_bottom[0]]
            if x == 0:
                parent_left = self.parent.inner["left"]
                count += parent_data[parent_left[1]][parent_left[0]]
            if x == 4:
                parent_right = self.parent.inner["right"]
                count += parent_data[parent_right[1]][parent_right[0]]

        if self.child:
            child_data = self.child.data
            if (x,y) == self.inner["top"]:
                count += np.sum([child_data[0,i] for i in range(5)])
            elif (x,y) == self.inner["bottom"]:
                count += np.sum([child_data[-1,i] for i in range(5)])
            elif (x,y) == self.inner["left"]:
                count += np.sum([child_data[i,0] for i in range(5)])
            elif (x,y) == self.inner["right"]:
                count += np.sum([child_data[i,-1] for i in range(5)])
        return count

    def __repr__(self):
        res = ""
        for line in grid:
            for c in line:
                res += c
            res += "\n"
        return res
