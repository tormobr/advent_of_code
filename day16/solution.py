import time
import numpy as np
def part1(data):
    out = data
    for i in range(100):
        out = phase(out)
    return out

def part2(data):
    print(data)
    message_offset = int("".join([str(x) for x in data[:7]]))
    print(message_offset)
    print(len(data))
    out = data[message_offset:]
    for i in range(100):
        out = phase2(out)
        print(i)
        #print(out)
    return out[:9]

def get_pattern(i, n):
    basic_pattern = [0,1,0,-1] 
    repeated = np.repeat(basic_pattern, i+1)
    return np.roll(np.tile(repeated, n // len(repeated)+1),-1)[:n]


def phase2(inn):
    print("new phase")
    s = sum(inn)
    out = []
    for i in range(len(inn)):
        out += [((s % 10)+ 10)%10]
        s -= inn[i]
    return out
    
def last_digit(n):
    return abs(n) % 10

def phase(inn):
    print("new phase")
    l = len(inn)
    return [last_digit(np.sum(inn * get_pattern(i, l))) for i in range(l)]

string = open("input.txt").read().strip()
list_data = [int(x) for x in string]
 
data1 = np.array(list_data)

print(part1(data1.copy()))
#data2 = np.array(list_data*10000)
#print(part2(data2.copy()))
