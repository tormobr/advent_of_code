import time
from collections import defaultdict

class Portal_maze:
    def __init__(self, data):
        
        self.data = data
        self.portals = defaultdict(lambda: list())
        self.mappings = {}
        self.max_x = len(data[0])-1
        self.max_y = len(data)-1
        self.directions = [(0,1), (0,-1), (1,0), (-1,0)]

    def part1(self):
        self.get_portals()
        print(self.mappings)
    
        start = self.portals[("A", "A")]
        start_x = start[0][0]
        start_y = start[0][1]
        visited = set()        
        self.DFS(start_x, start_y, 0, visited)
        #self.draw()
        
    def DFS(self, x, y, steps, visited):
        results = []
        visited.add((x,y))
        val = self.data[y][x]
        self.data[y][x] = "M"
        self.draw()
        #time.sleep(.2)
        print(val)
        if (x,y) in self.portals[("Z","Z")]:
            print("STEPS: ", steps)
            time.sleep(4)
            return steps


        if (x, y) in self.mappings.keys():
            self.data[y][x] = "."
            x, y = self.mappings[(x, y)]
            self.data[y][x] = "M"
            visited.add((x,y))
            steps += 1
            self.draw()
            #time.sleep(.2)
        if val >= "A" and val <= "Z":
            return
        self.data[y][x] = "."
        for d in self.directions:
            new_x = x + d[0]
            new_y = y + d[1]
            new_val = self.data[new_y][new_x]
            if new_val not in [" ", "#"] and (new_x, new_y) not in visited:
                self.DFS(new_x, new_y, steps+1, visited.copy())

    def draw(self):
        res = ""
        for line in self.data:
            for c in line:
                res += c
            res += "\n"
        print(res)

    def get_portals(self):
        for y,line  in enumerate(self.data):
            for x,c in enumerate(line):
                #print(f"max_x: {self.max_x} max_y: {self.max_y}, current_x:{x} current_y: {y}")
                d = (0,0)
                if c not in [" ", ".", "#"]:
                    d = self.check_neigbohrs(x,y,c)
        for k, v in self.portals.items():
            print("k", k)
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
    PM = Portal_maze(data)
    print(PM.part1())
