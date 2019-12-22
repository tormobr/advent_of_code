
    def BFS(self):
        queue = [(*self.start, 0)]
        current_keys = []
        steps = 0

        while queue:
            steps += 1
            s = queue.pop(0)
            print(queue, current_keys, steps)
            x = s[0] 
            y = s[1] 
            d = s[2] 
            val = self.data[y,x]
            self.data[y,x] = "X"
            self.visited.add((x, y, tuple(current_keys.copy())))
            self.draw()

            if val in self.doors and val.lower() not in current_keys:
                print("hit door", val, current_keys)
                continue

            if val in self.keys and val not in current_keys:
                current_keys.append(val)
                print("new key found", val, "at step", d)
                if set(current_keys) == set(self.keys):
                    print("all keys found:", current_keys, d)
                    time.sleep(10)
            for dirr in self.directions:
                new_x = x + dirr[0]
                new_y = y + dirr[1]
                if (new_x, new_y, tuple(current_keys)) not in self.visited:
                    if self.data[new_y, new_x] != "#":
                        queue.append((new_x, new_y, d+1))

