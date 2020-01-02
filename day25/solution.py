from itertools import combinations
import time
import random
from intcoder import Intcoder

class Zork:
    def __init__(self, data):
        self.data = data
        self.computer = Intcoder(self.data, 0)
        self.items = ["cake", "prime number", "mutex", "dehydrated water", "coin", "manifold", "candy cane", "fuel cell", ""]
        self.out = 0
        self.res = ""

    def take_drop_items(self, items, keyword="take"):
        next_in = self.string_to_ascii(keyword + items[0] + "\n")
        self.computer.set_input(next_in)
        print("take "+items[0] + "\n")
        index = 1
        while index < len(items):
            self.out = self.computer.eval()
            self.res += chr(self.out)
            if "Command?" in self.res:
                print(self.res)
                self.res = ""
                self.computer.set_input(self.string_to_ascii(keyword+items[index]+"\n"))
                index += 1


    def break_door(self):
        last_perm = self.items
        for r in range(1, len(self.items)): 
            all_inns = list(combinations(self.items, r))
            for perm in all_inns:
                self.take_drop_items(last_perm, keyword="drop ")
                self.take_drop_items(perm, keyword="take ")
                self.computer.set_input(self.string_to_ascii("west\n"))
                while "Command?" not in self.res:
                    self.out = self.computer.eval()
                    if self.out == -1:
                        return self.res
                        time.sleep(1)
                    self.res += chr(self.out)
                print(self.res)
                self.res = ""
                last_perm = perm


    def solve(self):
        inputs = [line for line in open("path.txt").read().split("\n")]
        #print(inputs2)
        #time.sleep(100)
        items = ["cake", "prime number", "mutex", "dehydrated water", "coin", "manifold", "candy cane", "fuel cell", ""]
        index = 0
        while self.out != -1:
            self.out = self.computer.eval()
            if self.out == -1:
                print("out = -1", self.res)
                break
            self.res += chr(self.out)
            if "Command?" in self.res:
                print(self.res)
                #inn = self.string_to_ascii(random.choice(self.directions))
                if index < len(inputs):
                    inn = self.string_to_ascii(inputs[index] + "\n")
                else: 
                    return self.break_door()
                self.computer.set_input(inn)
                self.res = ""
                index += 1
                print(self.res)

    def string_to_ascii(self, s):
        return [ord(c) for c in s]

if __name__ == "__main__":
    data = {i:int(x) for i,x in enumerate(open("input.txt").read().split(","))}

    Z = Zork(data)
    print(Z.solve())
