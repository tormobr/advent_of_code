from itertools import combinations
import time
import random
from intcoder import Intcoder

class Zork:
    def __init__(self, data):
        self.data = data
        self.computer = Intcoder(self.data, 0)
        #self.directions = {
            #"north": (0,-1),
            #"south": (0,1),
            #"west": (-1,0),
            #"east": (1,0),
        #}
        self.directions = ["north\n", "south\n", "east\n", "west\n"]
        self.trans = {
            "n": "north",
            "s": "south",
            "w": "west",
            "e": "east"
        }

    def drop_items(self, items):
        out = 0
        res = ""
        self.computer.set_input(self.string_to_ascii("drop "+items[0]+"\n"))
        print("drop "+items[0] + "\n")
        index = 1
        while out != -1 and index < len(items):
            out = self.computer.eval()
            res += chr(out)
            if "Command?" in res:
                print(res)
                res = ""
                self.computer.set_input(self.string_to_ascii("drop "+items[index]+"\n"))
                index += 1

    def take_items(self, items):
        out = 0
        res = ""
        self.computer.set_input(self.string_to_ascii("take "+items[0]+"\n"))
        print("take "+items[0] + "\n")
        index = 1
        while out != -1 and index < len(items):
            out = self.computer.eval()
            res += chr(out)
            if "Command?" in res:
                print(res)
                res = ""
                self.computer.set_input(self.string_to_ascii("take "+items[index]+"\n"))
                index += 1


    def break_door(self):
        items = ["cake", "prime number", "mutex", "dehydrated water", "coin", "manifold", "candy cane", "fuel cell", ""]
        out = 0
        res = ""
        all_inns = list(combinations(items, 5))
        current_inn = 0
        
        for perm in all_inns:
            self.drop_items(items)
            self.take_items(perm)
            self.computer.set_input(self.string_to_ascii("west\n"))
            while "Command?" not in res:
                out = self.computer.eval()
                if out == -1:
                    print("out = 1", res)
                    time.sleep(1)
                res += chr(out)
            print(res)
            if "ejected" not in res:
                print(res)
                time.sleep(7)
            else:
                res = ""


    def solve(self):
        out = 0
        res = ""
        inputs = ["south", "take fuel cell", "south", "take manifold", "north", "north", "north", "take candy cane", "south", "west", "take mutex", "south", "south", "south", "take coin", "west", "take dehydrated water", "south", "take prime number", "north", "east", "north", "east", "take cake", "north", "west", "south", ""]
        items = ["cake", "prime number", "mutex", "dehydrated water", "coin", "manifold", "candy cane", "fuel cell", ""]
        index = 0
        while out != -1:
            out = self.computer.eval()
            if out == -1:
                print("out = -1", res)
                break
            res += chr(out)
            if "Command?" in res:
                if "ejected" in res:
                    print("THIS COMBO DID NOT WORK!!!")
                #if "fuel cell" in res:
                    #print("currently at fuel cell:", inputs[index])
                    #time.sleep(3)
                print(res)
                #inn = self.string_to_ascii(random.choice(self.directions))
                if index < len(inputs):
                    inn = self.string_to_ascii(inputs[index] + "\n")
                else: 
                    self.break_door()
                    inn = self.string_to_ascii(input("Enter direcion:") + "\n")
                #print(inn)
                self.computer.set_input(inn)
                #self.parse_out(res)
                #time.sleep(20)
                res = ""
                index += 1
                print(res)
    def parse_out(self, s):
        print(s.strip().split("\n")) 

    def pretty_print(self):
        pass

    def string_to_ascii(self, s):
        return [ord(c) for c in s]

if __name__ == "__main__":
    data = {i:int(x) for i,x in enumerate(open("input.txt").read().split(","))}

    Z = Zork(data)
    print(Z.solve())
