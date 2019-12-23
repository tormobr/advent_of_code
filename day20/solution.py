from collections import defaultdict

class Portal_maze:
    def __init__(self, data):
        
        self.data = data
        self.portals = defaultdict(lambda: list())
        self.max_x = len(data[0])-1
        self.max_y = len(data)-1

    def part1(self):
        self.get_portals()
        print(self.portals)
        #self.draw()
        
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
                print(f"max_x: {self.max_x} max_y: {self.max_y}, current_x:{x} current_y: {y}")
                d = (0,0)
                if c not in [" ", ".", "#"]:
                    d = self.check_neigbohrs(x,y,c)

    def check_neigbohrs(self, x, y, val):
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        for d in directions:
            new_x = x + d[0]
            new_y = y + d[1]
            if self.out_of_bounds(new_x, new_y):
                continue
            new_val = self.data[new_y][new_x]
            if new_val not in [".", "#", " "]:
                if (new_val, val) not in self.portals.keys():
                    self.portals[(val, new_val)].append(self.get_closest((x,y), (new_x, new_y)) )
                    break
        print(d)
        return (abs(d[0]), abs(d[1]))
       
    def get_closest(self, pos1, pos2):
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        pos = [pos1, pos2]
        for d in directions:
            for p in pos:
                x, y = p
                new_x = x + d[0]
                new_y = y + d[1]
                if self.out_of_bounds(new_x, new_y):
                    continue
                
                if self.data[new_y][new_x] == ".":
                    return (new_x, new_y)
    def out_of_bounds(self, x, y):
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        for d in directions:
            new_x = x + d[0]
            new_y = y + d[1]
        
            if new_x < 0 or new_x > self.max_x:
                return True
            if new_y < 0 or new_y > self.max_y:
                return True

        return False


if __name__ == "__main__":
    
    data = [[c for c in line.strip("\n")] for line in open("input.txt")]
    PM = Portal_maze(data)
    print(PM.part1())
