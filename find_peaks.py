from scipy.signal import argrelextrema
import numpy as np
from simulation import simulate_predator_prey
import matplotlib.pyplot as plt


def find_distance(x, y):
    minima = argrelextrema(y, np.less)[0]
    maxima = argrelextrema(y, np.greater)[0]
    for min_idx in minima:
        max_candidates = maxima[maxima > min_idx]
        if len(max_candidates) > 0:
            max_idx = max_candidates[0]
            break
    return x[max_idx] - x[min_idx]


a = np.arange(0.5, 3, 0.1)


if __name__ == '__main__':
    times_prey = []
    times_predator = []
    for num in a:
        t, x, y, suma_populacji = simulate_predator_prey(A=num)
        times_prey.append(find_distance(t, x))
        times_predator.append(find_distance(t, y))
    plt.plot(a, times_prey)
    plt.plot(a, times_predator)
    plt.show()
    print(a)
