from collections import defaultdict
import time
import numpy as np

class Maze_solver:
    def __init__(self,data):
        self.data = data
        start_arr = np.where(data == "@")
        self.start = (start_arr[1][0], start_arr[0][0])
        print(self.start)
        self.directions = [(0,-1), (1,0), (0,1),(-1,0)]
        self.keys = []
        self.get_keys()
        print(self.keys)
        self.doors = [k.upper() for k in self.keys]
        self.visited = set()
        self.distances = defaultdict(int)
        print(self.start)
    def get_keys(self):
        for y in range(len(data)):
            for x in range(len(data[y])):
                if ord(data[y,x]) >= 97 and ord(self.data[y,x]) <= 122:
                    self.keys.append(data[y,x])
    def part1(self):
        res = {}
        current_keys = []
        current = self.start
        self.DFS(*self.start, current_keys, 0, res, 0)
        print("from root", res)

        while set(self.distances.keys()) != set(self.keys):
            prev_res = res.copy()
            print("from k", res)
            for k,v in prev_res.items():
                self.visited = set()
                res = {}
                #if self.distances[k] == 0 or v[0] < self.distances[k]:
                self.distances[k] = v[0]
                self.draw()
                self.data = np.where(self.data == k, ".", self.data) 
                self.data = np.where(self.data == k.upper(), ".", self.data) 
                self.draw()
                self.DFS(*v[1], current_keys, 0, res, v[0])
                print(self.distances.items())

        return self.distances.items()
    
    # gets the distance to all keys from one pos
    def DFS(self, x, y, current_keys, steps, res, prevdist):
        self.visited.add((x,y))
        #print("current_steps:", steps, current_keys)
        #print("x,y", x,y)
        val = self.data[y,x]
        #print(x,y,val)
        #self.data[y,x] = "X"
        #print(val)
        #self.draw()
        if val in self.keys and val not in current_keys:
            #print("collecting key:", val, "on step:", steps)
            current_keys.append(val)
            res[val] = (steps + prevdist, (x,y))
        #self.data[y,x] = "."
        for dirr in self.directions:
            new_x = x + dirr[0]
            new_y = y + dirr[1]
            if (new_x, new_y) not in self.visited:
                if self.data[new_y, new_x] != "#" and self.data[new_y, new_x] not in self.doors:
                    #print("recursing into")
                    self.DFS(new_x, new_y, current_keys.copy(), steps+1,  res, prevdist)
        #print("backtracking")
            else:
                pass
                #print("been to", new_x, new_y, "with keys:", current_keys)

    def draw(self):
        res = ""
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                res += self.data[i,j]
            res += "\n"
        print(res)


if __name__ == "__main__":
    #data = np.array([[s for s in line.strip()] for line in open("input.txt", "r").read().split()], dtype=str)
    #data = np.array([[s for s in line.strip()] for line in open("input2.txt", "r").read().split()], dtype=str)
    data = np.array([[s for s in line.strip()] for line in open("input3.txt", "r").read().split()], dtype=str)

    m = Maze_solver(data)
    print(m.part1())
