
from copy import deepcopy
from collections import defaultdict, namedtuple, deque
import time

class Maze_solver:
    def __init__(self,data):
        self.data = data
        self.start = []
        self.directions = [(0,-1), (1,0), (0,1),(-1,0)]
        self.keys = []
        self.TL = []
        self.TR = []
        self.BL = []
        self.BR = []
        self.get_keys()
        self.bin_keys = self.generate_binkeys(self.keys)
        self.doors = [k.upper() for k in self.keys]
        self.visited = set()
        self.arrays = []

    def generate_binkeys(self, keys):
        bin_keys = 0
        for i in range(len(keys)):
            bin_keys = bin_keys | (1 << (ord(keys[i])-97))
        return bin_keys
        

    def part1(self):
        x,y = self.start[0]
        keys = [self.TL, self.TR, self.BL, self.BR]
        res = []
        for (x,y),k in zip(self.start, keys):

            res.append(min(self.BFS(x,y,k, self.generate_binkeys(k))))
        print(res, sum(res))

    def has_key(self, val, keys):
        shift_val = ord(val.lower()) - 97
        if (keys >> (shift_val) & 1) == 1:
            return True
        return False

    def BFS(self, x, y, k, bin_keys):
        print("NEW BFS: ", k, bin_keys)
        visited = set()
        State = namedtuple("State","x y keys")
        current = State(x, y, 0)
        queue = deque()
        queue.append((current, 0))
        results = []

        while queue:
            current,steps = queue.popleft()
            val = self.data[current.y][current.x]
            key = (current.x, current.y, current.keys)
            new_keys = current.keys
            
            if val == "#" or key in visited:
                continue
            visited.add(key)

            if val in self.doors and not self.has_key(val, current.keys):
                if val.lower in k:
                    continue

            """
            self.data[current.y][current.x] = "X"
            self.draw()
            time.sleep(.5)
            """

            if val in self.keys:
                if (new_keys >> ord(val)-97) & 1 != 1:
                    new_keys = new_keys + (1 << ord(val)-97)
                    print("found new key:", val)
                    #print(bin(new_keys))
                if new_keys == bin_keys:
                    results.append(steps)
                    print("found all keys fucker!!!!!")
                    time.sleep(.5)
                    return results

            #self.data[current.y][current.x] = "."
            for d in self.directions:
                new_x = current.x + d[0]
                new_y = current.y + d[1]
                new_state = State(new_x, new_y, new_keys)
                queue.append((new_state, steps+1))
            

        print(results)
        return results



    def draw(self):
        res = ""
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                res += self.data[i][j]
            res += "\n"
        print(res)

    def get_keys(self):
        for i,line in enumerate(data):
            for j, c in enumerate(line):
                if "a" <= c <= "z":
                    if i < len(data)//2 and j < len(data[0])//2:
                        self.TL.append(c)
                        print("appending ", c , "to TL")
                    elif i < len(data)//2 and j > len(data[0])//2:
                        self.TR.append(c)
                        print("appending ", c , "to TR")
                    elif i > len(data)//2 and j < len(data[0])//2:
                        self.BL.append(c)
                        print("appending ", c , "to BL")
                    elif i > len(data)//2 and j > len(data[0])//2:
                        self.BR.append(c)
                        print("appending ", c , "to BR")
                    self.keys.append(c)
                elif c == "@":
                    self.start.append((j,i))



if __name__ == "__main__":
    #data = [[s for s in line.strip()] for line in open("input.txt", "r").read().split()]
    #data = [[s for s in line.strip()] for line in open("input2.txt", "r").read().split()]
    data = [[s for s in line.strip()] for line in open("input3.txt", "r").read().split()]

    m = Maze_solver(data)
    s = time.time()
    print(m.part1())
    e = time.time()
    print("runtime: ", e-s)
