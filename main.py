import numpy as np
import matplotlib.pyplot as plt

# Globalne stałe
dt = .0001      # krok czasu
czas = 100      # czas symulacji
t = np.arange(0, czas, dt) # wektor czasowy

x = [100]       # wektor liczby ofiar
y = [20]        # wektor liczby drapieżców

# parametry równań
A = 1           # współczynnik rozrodczości ofiar
B = .1          # współczynnik śmierci ofiar z powodu drapieżców
C = .5          # współczynnik śmierci drapieżników
D = .1          # wspołcyznnik rozrodczości związanych z jedzeniem ofiar

###
# dx / dt = Ax - Bxy
# dy / dy = -Cy + Dxy
###

for i in range(1, len(t)):
    dx = x[i - 1] * (A - B * y[i - 1])
    dy = -y[i - 1] * (C - D * x[i - 1])

    x.append(x[i - 1] + dx * dt)
    y.append(y[i - 1] + dy * dt)

#obliczenie sumy populacji w czasie
suma_populacji = np.array(x) + np.array(y)


if __name__ == '__main__':
    plt.subplot(2, 1, 1)
    plt.plot(t, x)
    plt.plot(t, y)
    plt.xlabel('Czas')
    plt.ylabel('Wielkość Populacji')
    plt.legend(('Ofiary', 'Drapieżcy'))
    plt.title('ofiary drapieżcy')
    plt.subplot(2, 1, 2)
    plt.plot(x, y)
    plt.show()

# TODO: paramtetryzajca i obliczanie odległości Gausowskiej