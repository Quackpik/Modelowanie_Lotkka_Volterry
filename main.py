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
    plt.plot(x, y)
    plt.show()

# TODO: paramtetryzajca i obliczanie odległości Gausowskiej