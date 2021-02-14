import numpy as nu


def math_formula():
    """make mathematical formula:
        nu.log(1 + x ** 2) * ((1 / nu.e * nu.sin(x) + 1) / (5 / 4 + 1 / x * 5))
    """
    x = [1, 10, 1000]
    for x in x:
        y = nu.log(1 + x ** 2) * ((1 / nu.e * nu.sin(x) + 1) / (5 / 4 + 1 / x * 5))
        print(y)


math_formula()
