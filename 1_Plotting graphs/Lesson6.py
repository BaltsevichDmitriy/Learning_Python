import numpy as np
import matplotlib.pyplot as plt


def weierstrass():
    """graph of the Weierstrass function
    w(x) = b ** n * np.cos(a ** n * np.pi * x)
    """
    a = 3
    b = 0.7
    x = np.arange(0, 2.1, 0.01)
    y = 0
    for n in range(1, 10, 1):
        w = b ** n * np.cos(a ** n * np.pi * x)
        y += w
    plt.plot(x, y, label=r'$W(x)$')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('график функции Вейерштрасса')
    plt.legend(loc='best')
    plt.grid()
    plt.show()


weierstrass()
