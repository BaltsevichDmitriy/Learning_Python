import numpy as np
import matplotlib.pyplot as plt


def graph4():
    x = [1, 2, 3, 4, 5, 6]
    y = [1, 1.1, 1.76, 2, 2.04, 2.5]
    poly = np.poly1d(np.polyfit(x, y, deg=1))
    poly2 = np.poly1d(np.polyfit(x, y, deg=2))
    y1 = []
    y2 = []
    for i in range(6):
        calc = poly(i + 1)
        calc2 = poly2(i + 1)
        y1.append(calc)
        y2.append(calc2)
    plt.plot(x, y1, label=r'$p(x, deg=1)$')
    plt.plot(x, y2, label=r'$p(x, deg=2)$')
    plt.plot(x, y, label=r'$y(x)$')
    plt.legend(loc='best')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('аппроксимационные кривые')
    plt.show()


graph4()
