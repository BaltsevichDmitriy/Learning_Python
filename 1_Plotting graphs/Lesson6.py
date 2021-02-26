import numpy as np
import matplotlib.pyplot as plt


def weierstrass():
    a = 3
    b = 0.5
    x = np.arange(0.01, 2, 0.01)

    for n in range(1, 10, 1):
        w = b ** n * np.cos(a ** n * np.pi * x)
    plt.plot(x, w)
    plt.show()

    print(w,x)


#weierstrass()
print(0.5 ** 1 *np.cos(3 ** 1 * np.pi * 0))
print(np.cos(0))