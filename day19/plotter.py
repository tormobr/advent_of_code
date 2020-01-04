from matplotlib import pyplot as plt
from matplotlib import animation

class Animater:
    def __init__(self, arrays):
        fig, ax = plt.subplots()
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        self.mat = ax.matshow(self.generate_data(arrays, len(arrays)-19))
        ani = animation.FuncAnimation(fig, self.update, lambda: self.data_gen(arrays, len(arrays)), interval=50, save_count=len(arrays))
        plt.show()
        ani.save("plot.mp4", )

    def generate_data(self, arrays, i):
        return arrays[i]

    def update(self, data):
        self.mat.set_data(data)
        return self.mat 

    def data_gen(self, arrays, iterations):
        for i in range(1, iterations, 5):
            yield self.generate_data(arrays, i)
