
    def DFS(self, x, y, steps, visited):
        results = []
        visited.add((x,y))
        val = self.data[y][x]
        self.data[y][x] = "M"
        #self.draw()
        if (x,y) in self.portals[("Z","Z")]:
            return steps

        if (x, y) in self.mappings.keys():
            self.data[y][x] = "."
            x, y = self.mappings[(x, y)]
            self.data[y][x] = "M"
            visited.add((x,y))
            steps += 1
            #self.draw()
        if val >= "A" and val <= "Z":
            return -1

        self.data[y][x] = "."
        for d in self.directions:
            new_x = x + d[0]
            new_y = y + d[1]
            new_val = self.data[new_y][new_x]
            if new_val not in [" ", "#"] and (new_x, new_y) not in visited:
                results.append(self.DFS(new_x, new_y, steps+1, visited.copy()))
        results = list(filter(lambda x: x != -1, results))
        if len(results) > 0:
            #time.sleep(1)
            return min(results)
        return -1

    def draw(self):
        res = ""
        for line in self.data:
            for c in line:
                res += c
            res += "\n"
