import matplotlib.pyplot as plt


def graph3():
    """plotting graph input from the terminal """
    with plt.xkcd():
        plt.xkcd()
        plt.pie([70, 10, 10, 10], labels=('В комментариях', 'В Ираке', 'В Сирии', 'В Афганистане'))
        plt.title('Где ведутся самые ожесточенные бои')
    plt.show()


eval(input('введите имя функции'))
