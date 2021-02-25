import numpy as np
import matplotlib.pyplot as plt


def graph4():
    x = np.arange(-1, 9, 0.02)
    plt.plot(x, x ** 2, label=r'$f= x^2$')
    plt.plot([1, 2, 8], [1, 2, 3], 'go-', label='line 1', linewidth=2)
    plt.grid()
    plt.fill_between(x, 1.3 * x ** 2, 0.7 * x ** 2, alpha=0.5)
    plt.legend(loc='best')
    plt.show()


# graph4()
# help(np.poly1d)


def poly():
    x = np.arange(20)
    y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    curve = np.polyfit(x, y, 2)
    poly = np.poly1d(curve)
    new_x = []
    new_y = []
    for i in range(-1,19,1):
        new_x.append(i + 1)
        calc = poly(i + 1)
        new_y.append(calc)
    plt.plot(new_x, new_y)
    plt.plot(x, y)
    plt.show()

poly()
# help(np.arange)
