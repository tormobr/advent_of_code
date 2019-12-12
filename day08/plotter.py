from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np

# solution for part 2 
def part2(data, width, height, layers):
    arrays = []
    result = data[0]
    arrays.append(result)
    for i in range(1, layers):
        result = np.where(result != 2, result, data[i])
        arrays.append(result)

    # Hacky way to show end state longer
    for i in range(20):
        arrays.append(result)
    return arrays

# Reads the string data into a 3d array of grids
def parse_file(data, width, height, layers):
    data = np.reshape(data, (layers, height,width))
    return data

def generate_data(arrays, i):
    return arrays[i]

def update(data):
    mat.set_data(data)
    return mat 

def data_gen(arrays, iterations):
    for i in range(iterations):
        yield generate_data(arrays, i)
if __name__ == "__main__":
    str_data = np.array(list(open("input.txt", "r").read().strip()), dtype=int)
    width = 25
    height  = 6
    layers = len(str_data)//(width*height)
    data = parse_file(str_data, width, height, layers)

    arrays = part2(data, width, height, layers)
    
    fig, ax = plt.subplots()
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    mat = ax.matshow(generate_data(arrays, 0))
    ani = animation.FuncAnimation(fig, update, lambda: data_gen(arrays, layers+20), interval=100, save_count=layers+20)
    plt.show()
    ani.save("plot.mp4", )
