from collections import defaultdict


lines = [line.strip() for line in open("input.txt", "r")]
planets = {}
for line in lines:
    splitted = line.split(",")
    x = int(splitted[0].strip()[3:])
    y = int(splitted[1].strip()[2:])
    z = int(splitted[2].strip()[2:-1])
    planets[(x,y,z)] = [0,0,0]
    print(x,y,z)

steps = 999
for i in range(steps):
    new_planets = {}
    print(planets)
    for k,v in planets.items():
        x_min = 0
        y_min = 0
        z_min = 0
        for k2, v2 in planets.items():
            if k == k2:
                continue
            for i in range(3):
                val = 0 
                if k[i] < k2[i]:
                    val = 1
                elif k[i] > k2[i]:
                    val = -1
                planets[k][i] += val

        #planets[k][0] += x_min
        #planets[k][1] += y_min
        #planets[k][2] += z_min

        new_planets[(k[0]+planets[k][0], k[1]+planets[k][1], k[2]+planets[k][2])] = planets[k]
    planets = new_planets.copy()

res = 0
for k, v in planets.items():
    a = sum([abs(x) for x in k])
    b = sum([abs(x) for x in v])
    res += a*b
print("energy: ",res)

         

#<x=-1, y=0, z=2>
#<x=2, y=-10, z=-7>
#<x=4, y=-8, z=8>
#<x=3, y=5, z=-1>
