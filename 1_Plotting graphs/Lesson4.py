import numpy as np
import matplotlib.pyplot as plt

def graph3():
    """

    :return:
    """
    with plt.xkcd():
        plt.xkcd()
        plt.pie([70,10, 10, 10], labels=('В комментариях', 'В Ираке', 'В Сирии', 'В Афганистане'))
        plt.title('Где ведутся самые ожесточенные бои')


    plt.show()
#graph3()
eval("2 + 3*len('hello')")