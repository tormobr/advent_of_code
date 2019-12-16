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
    out = data
    for i in range(100):
        out = phase2(out)
        print(i)
    return out[message_offset:message_offset+9]

def phase2(inn):
    print("new phase")
    s = sum(inn)
    out = []
    for i in range(len(inn)):
        out += [((s % 10)+ 10)%10]
        s -= inn[i]
    return out
    out = []
    
    for i in range(len(inn)):
        print("digit:", i)
        full = np.zeros((len(inn)+1))
        pattern = [0,1,0,-1]
        index = 0
        filled = False
        for j in range(len(full)):
            for k in range(i+1):
                if index < len(full):
                    full[index] = pattern[j%4]
                    index += 1
                else:
                    filled = True
                    break
            if filled: break
            j += i+1
        full = full[1:]
        multi = inn * full
        total = int(np.sum(inn*full))

        last = int(str(total)[-1])
        out.append(last)
    return out

def phase(inn):
    print("new phase")
    out = []
    
    for i in range(len(inn)):
        full = np.zeros((len(inn)+1))
        pattern = [0,1,0,-1]
        index = 0
        filled = False
        for j in range(len(full)):
            for k in range(i+1):
                if index < len(full):
                    full[index] = pattern[j%4]
                    index += 1
                else:
                    filled = True
                    break
            if filled: break
            j += i+1
        full = full[1:]
        multi = inn * full
        total = int(np.sum(inn*full))

        last = int(str(total)[-1])
        out.append(last)
    return out
        

string = open("input.txt").read().strip()
list_data = [int(x) for x in string]
 
data1 = np.array(list_data)

#print(part1(data1.copy()))
data2 = np.array(list_data*10000)
print(part2(data2.copy()))
