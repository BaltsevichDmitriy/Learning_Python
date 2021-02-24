import numpy as np
import matplotlib.pyplot as plt


def graph2():
    """ This function created the graph
     log(tan(1 / 1 + sin(x) ** 2)) * (x ** 2 + 1) * exp(-(|x| / 10))
     """
    x = np.arange(-0.2, 0.8, 0.01)
    y = np.log(np.tan(1 / 1 + np.sin(x) ** 2)) * (x ** 2 + 1) * np.exp(-1 * (np.abs(x) / 10))
    plt.xlabel('x')
    plt.ylabel('y(x)')
    plt.title(r'$log(tan(1 / 1 + sin(x) ^ 2))*(x ^ 2 + 1)*exp(-(|x| / 10))$')
    plt.plot(y)
    plt.show()


graph2()
