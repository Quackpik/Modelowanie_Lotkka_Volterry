import numpy as np
import matplotlib.pyplot as plt
from simulation import simulate_predator_prey

t, x, y, suma_populacji = simulate_predator_prey()


if __name__ == '__main__':
    plt.subplot(2, 1, 1)
    plt.plot(t, x)
    plt.plot(t, y)
    plt.xlabel('Czas [jednostki arbitralne]')
    plt.ylabel('Liczebność Populacji')
    plt.legend(('Ofiary', 'Drapieżcy'))
    plt.title('ofiary drapieżcy')
    plt.subplot(2, 1, 2)
    plt.plot(x, y, zorder=1)
    plt.scatter(0.5 / 0.01, 1 / 0.1, c='red', s=10, zorder=2)
    plt.show()

# TODO: paramtetryzajca i obliczanie odległości Gausowskiej