from numba import jit
from copy import deepcopy
from plotter import Animater
from collections import defaultdict, namedtuple, deque
import time

class Maze_solver:
    def __init__(self,data):
        self.data = data
        self.start = (0,0)
        self.directions = [(0,-1), (1,0), (0,1),(-1,0)]
        self.keys = set()
        self.get_keys()
        self.doors = [k.upper() for k in self.keys]
        self.visited = set()
        self.arrays = []
        print(self.keys)
        time.sleep(2)


    def part1(self):
        return min(self.BFS())

    def convert_array(self, a):
        for i in range(len(a)):
            for j in range(len(a[i])):
                if a[i][j] == "#": a[i][j] = 1
                elif a[i][j] == ".": a[i][j] = 3
                elif a[i][j] == "@": a[i][j] = 2
                elif a[i][j] in self.keys: a[i][j] = 4
                elif a[i][j] in self.doors: a[i][j] = 5
                else:
                    a[i][j] = 6
        return a

    def track(self, path, arr):
        for x,y in path:
            if arr[y][x] not in [4, 5]:
                prev = arr[y][x]
                arr[y][x] = 7
                self.arrays.append(deepcopy(arr))
                arr[y][x] = prev
            else:
                arr[y][x] = 3

    def BFS(self):
        draw_array = self.convert_array(deepcopy(self.data))
        visited = set()
        State = namedtuple("State","x y keys")
        x, y = self.start
        path = []
        current = State(x, y, [])
        queue = deque()
        queue.append((current, 0, path))
        results = []

        while queue:
            current,steps, path = queue.popleft()
            val = self.data[current.y][current.x]
            key = (current.x, current.y, tuple(sorted(current.keys)))
            new_keys = set(current.keys)
            
            if val == "#" or key in visited:
                continue
            visited.add(key)
            path.append((current.x, current.y))

            if val in self.doors and val.lower() not in current.keys:
                continue

            if val in self.keys and val not in current.keys:
                new_keys.add(val)
                print(new_keys)
                if new_keys == self.keys:
                    results.append(steps)
                    self.track(path, draw_array)
                    return results

            #self.data[current.y][current.x] = "."
            for d in self.directions:
                new_x = current.x + d[0]
                new_y = current.y + d[1]
                new_state = State(new_x, new_y, new_keys)
                queue.append((new_state, steps+1, path.copy()))
            

        print(results)
        return results



    def draw(self):
        res = ""
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                res += self.data[i,j]
            res += "\n"
        print(res)

    def get_keys(self):
        for i,line in enumerate(data):
            for j, c in enumerate(line):
                if "a" <= c <= "z": self.keys.add(c)
                elif c == "@": self.start = (j,i)


if __name__ == "__main__":
    #data = [[s for s in line.strip()] for line in open("input.txt", "r").read().split()]
    #data = [[s for s in line.strip()] for line in open("input2.txt", "r").read().split()]
    data = [[s for s in line.strip()] for line in open("input3.txt", "r").read().split()]

    m = Maze_solver(data)
    s = time.time()
    print(m.part1())
    e = time.time()
    Animater(m.arrays)
    print(f"runtime: {e-s}")
