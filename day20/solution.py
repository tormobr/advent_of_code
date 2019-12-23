from plotter import Animater
from copy import deepcopy
import sys
import time
from collections import defaultdict
sys.setrecursionlimit(10**6)
class Portal_maze:
    def __init__(self, data):
        self.data = data
        self.portals = defaultdict(lambda: list())
        self.mappings = {}
        self.max_x = len(data[0])-1
        self.max_y = len(data)-1
        self.directions = [(0,1), (0,-1), (1,0), (-1,0)]
        self.arrays = []

    def part1(self):
        self.get_portals()
    
        start = self.portals[("A", "A")]
        start_x = start[0][0]
        start_y = start[0][1]
        visited = set()        
        #res = self.DFS(start_x, start_y, 0, visited)
        res = self.BFS(start_x, start_y, levels=False)
        return res
        #self.draw()

    def part2(self):
        self.get_portals()
        start_x, start_y = self.portals[("A", "A")][0]
        res = self.BFS(start_x, start_y, levels=True)
        return res

    # Determines wether a point is on inner or outer side of donut
    def outer(self, x, y):
        if 3 < x and x < self.max_x-3 and 3 < y and y < self.max_y-3:
            return False
        return True

    

    def BFS(self, start_x, start_y, levels=False):
        visited = set()
        queue = [(start_x, start_y, 0, 0, [])]
        level = 0        
        iteration = 0
        while len(queue) > 0:
            x, y, current_steps, level, path = queue.pop(0)
            visited.add((x,y,level))
            val = self.data[y][x]
            path.append((x,y))
            self.data[y][x] = "M"
            if iteration % 10 == 0:
                arr = self.convert_array(deepcopy(self.data))
                self.arrays.append(arr)
            if val >= "A" and val <= "Z":
                continue

            if (x,y) in self.portals[("Z","Z")] and level == 0:
                print(f"answer: {current_steps}")
                self.backtrack(path)
                #return current_steps

            if (x, y) in self.mappings.keys():
                new_x, new_y = self.mappings[(x, y)]
                # For part one where levels are irrelevant
                if not levels:
                    queue.append((new_x, new_y, current_steps+1, level, path.copy()))

                elif self.outer(x,y) and level != 0 and (new_x, new_y, level-1) not in visited:
                    queue.append((new_x, new_y, current_steps +1, level-1, path.copy()))
                elif not self.outer(x,y) and (new_x, new_y, level+1) not in visited:
                    queue.append((new_x, new_y, current_steps +1, level+1, path.copy()))

            for d in self.directions:
                new_x = x + d[0]
                new_y = y + d[1]
                new_val = self.data[new_y][new_x]
                if new_val not in [" ", "#"] and (new_x, new_y, level) not in visited:
                    queue.append((new_x, new_y, current_steps + 1, level, path.copy()))
            iteration += 1

        arr = self.convert_array(deepcopy(self.data))
        for _ in range(100):
            self.arrays.append(arr)
   
    def backtrack(self, path):
        for x,y in path:
            self.data[y][x] = "K"
            arr = self.convert_array(deepcopy(self.data))
            self.arrays.append(arr)

    def convert_array(self, a):
        for i in range(len(a)):
            for j in range(len(a[i])):
                if a[i][j] == " ": a[i][j] = 0
                elif a[i][j] == "#": a[i][j] = 1
                elif a[i][j] == "M": a[i][j] = 2
                elif a[i][j] == ".": a[i][j] = 3
                elif a[i][j] == "K": a[i][j] = 5
                else:
                    a[i][j] = 4
        return a

        

    def get_portals(self):
        for y,line  in enumerate(self.data):
            for x,c in enumerate(line):
                #print(f"max_x: {self.max_x} max_y: {self.max_y}, current_x:{x} current_y: {y}")
                d = (0,0)
                if c not in [" ", ".", "#"]:
                    d = self.check_neigbohrs(x,y,c)
        for k, v in self.portals.items():
            if len(v) >1:
                self.mappings[v[0]] = v[1]
                self.mappings[v[1]] = v[0]

    def check_neigbohrs(self, x, y, val):
        for d in self.directions:
            new_x = x + d[0]
            new_y = y + d[1]
            if self.out_of_bounds(new_x, new_y):
                continue
            new_val = self.data[new_y][new_x]
            if new_val not in [".", "#", " "]:
                if (new_val, val) not in self.portals.keys():
                    self.portals[(val, new_val)].append(self.get_closest((x,y), (new_x, new_y)) )
                    break
        return (abs(d[0]), abs(d[1]))
       
    def get_closest(self, pos1, pos2):
        pos = [pos1, pos2]
        for d in self.directions:
            for p in pos:
                x, y = p
                new_x = x + d[0]
                new_y = y + d[1]
                if self.out_of_bounds(new_x, new_y):
                    continue
                
                if self.data[new_y][new_x] == ".":
                    return (new_x, new_y)
    def out_of_bounds(self, x, y):
        if x < 0 or x > self.max_x:
            return True
        elif y < 0 or y > self.max_y:
            return True

        return False


if __name__ == "__main__":
    
    data = [[c for c in line.strip("\n")] for line in open("input.txt")]
    PM = Portal_maze(data.copy())
    print(f"Part 1 answer: {PM.part1()}")
    Animater(PM.arrays)
    #PM2 = Portal_maze(data)
    #print(f"Part 2 answer: {PM2.part2()}")
