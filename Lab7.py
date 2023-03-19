
import random
import numpy as np
from time import perf_counter
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import PillowWriter, FuncAnimation


# Задание 1
def Exercise1():
 StartList = perf_counter()
 array_1 = []
 array_2 = []
 result = []
 for i in range(1000000):
    num_1 = random.randint(1, 1000000)
    num_2 = random.randint(1, 1000000)
    array_1.append(num_1)
    array_2.append(num_2)
    result.append(array_1[i] * array_2[i])
 TimeN = perf_counter() - StartList
 print(TimeN, '[c], python lists')

 TimeN = perf_counter()
 array_1 = np.random.randint(0, 1000000, 1000000)
 array_2 = np.random.randint(0, 1000000, 1000000)
 result = np.multiply(array_1, array_2)
 print(perf_counter() - TimeN, '[c], numpy')

# Задание 2
def Histogram():
    data = np.genfromtxt('data2.csv', delimiter=',')
    FifthColumn = np.array(data[:, 4], float)[1:]

    plt.hist(FifthColumn, 25, color='lawngreen', ec='darkgreen')
    plt.title('bar chart')
    plt.xlabel('Value')
    plt.ylabel('frequency')
    plt.grid()
    plt.show()

    plt.hist(FifthColumn, 20, ec='gold', color='yellow', density=True)
    plt.title('Normalized histogram')
    plt.xlabel('Value')
    plt.ylabel('frequency')
    plt.grid()
    plt.show()

    print(f'standard deviation: {np.std(FifthColumn)}')


# Задание 3
def ThreeDimensional():
    x = np.linspace(-np.pi * 3, np.pi * 3, 100)
    y = x * np.cos(x)
    z = np.sin(x)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z, marker='x', c='dodgerblue')

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    ax.set_title('3D Plot')

    plt.show()

# доп
def ExtraExercise():
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x)

    fig, ax = plt.subplots()
    line, = ax.plot(x, y)

    def animate(i):
        line.set_ydata(np.sin(x + i / 10.0))
        return line,
    animation = FuncAnimation(fig, animate, interval=16, repeat=True)
    def animate(i):
        line.set_ydata(np.sin(x + i / 10.0))
        return line,

    plt.show()

    writer = PillowWriter(fps=25)
    animation.save("sine_x.gif", writer=writer)


if __name__ == '__main__':
    Exercise1()
    Histogram()
    ThreeDimensional()
    ExtraExercise()
