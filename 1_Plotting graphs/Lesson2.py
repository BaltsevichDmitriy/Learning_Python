import numpy as np
import matplotlib.pyplot as plt


def graph1():
    """ This function creates the graph y(x)=x*x-x-6 and finds out root y(x)=0"""
    x = np.arange(0, 6, 1)
    plt.xlabel('x')
    plt.ylabel('y(x)=x*x - x - 6')
    plt.title('График y(x)=x*x-x-6', fontsize=16)
    plt.grid(color='gray')
    plt.text(1.9, 0.85, 'y(x)=0',
             fontsize=18, bbox={'facecolor': 'yellow'})
    plt.plot(x * x - x - 6, 'r-o')
    plt.plot(3, 0, 'bs')
    plt.show()


graph1()
