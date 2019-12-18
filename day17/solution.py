from intcoder import Intcoder


def get_intersections(arr):
    intersections = 0
    for y in range(len(arr)-5):
        for x in range(len(arr[0])-5):
            print(x,y)
            if x not in [0, len(arr[0])] and y not in [0, len(arr)] and arr[y][x] == "#" :
                print("inside", x,y)
                print(len(arr))
                print(len(arr[0]))
                if x > 45 or y > 45:
                    break

                if arr[y+1][x] != "#" or arr[y-1][x] != "#":
                    continue
                elif arr[y][x+1] != "#" or arr[y][x-1] != "#":
                    continue
                print("intersection found")
                intersections += x*y
    return intersections
def part1(data):
    computer = Intcoder(data, 0)

    arr = [[]]
    current_y = 0
    res = ""
    while True:
        out = computer.eval(None)
        if out == -1:
            break
        if out == 10:
            arr.append([])
            current_y += 1
        else:
            arr[current_y].append(chr(out))

        res += chr(out)
    hax = get_intersections(arr)
    return res, hax
if __name__ == "__main__":
    data = {i: int(x) for (i,x) in enumerate(open("input.txt", "r").read().split(","))}
    image, part1_res = part1(data)
    print(image) 
    print(part1_res)

