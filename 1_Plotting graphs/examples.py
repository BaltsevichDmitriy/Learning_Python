



def graph4():
    x = np.arange(-1, 9, 0.02)
    plt.plot(x, x ** 2, label=r'$f= x^2$')
    plt.plot([1, 2, 8], [1, 2, 3], 'go-', label='line 1', linewidth=2)
    plt.grid()
    plt.fill_between(x, 1.3 * x ** 2, 0.7 * x ** 2, alpha=0.5)
    plt.legend(loc='best')
    plt.show()


# graph4()