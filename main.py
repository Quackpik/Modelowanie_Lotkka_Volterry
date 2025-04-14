import numpy as np
import matplotlib.pyplot as plt
from simulation import simulate_predator_prey

t, x, y, suma_populacji = simulate_predator_prey()


if __name__ == '__main__':
    plt.plot(t, x)
    plt.plot(t, y)
    plt.xlabel('Czas')
    plt.ylabel('Wielkość Populacji')
    plt.legend(('Ofiary', 'Drapieżcy'))
    plt.title('ofiary drapieżcy')
    plt.show()

# TODO: paramtetryzajca i obliczanie odległości Gausowskiej