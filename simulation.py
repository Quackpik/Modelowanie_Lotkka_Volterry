import numpy as np
import random


def StochasticTerm(amp=0.1):
    rand = amp * np.random.uniform(-1, 1)
    if np.abs(rand) > 1:
        return 0
    else:
        return rand


def simulate_predator_prey(
        dt=0.001,
        total_time=100,
        prey_init=100,
        predator_init=20,
        A=1.0,
        B=0.1,
        C=0.5,
        D=0.01,
        stc=True
):
    """
    Symuluje model drapieżnik-ofiara (Lotki-Volterry) z podanymi parametrami.

    Parametry:
    - dt: krok czasowy
    - total_time: całkowity czas symulacji
    - prey_init: początkowa liczba ofiar
    - predator_init: początkowa liczba drapieżników
    - A: współczynnik rozrodczości ofiar
    - B: współczynnik śmierci ofiar z powodu drapieżników
    - C: współczynnik śmierci drapieżników
    - D: współczynnik rozrodczości drapieżników w wyniku jedzenia ofiar

    Zwraca:
    - t: wektor czasu
    - x: populacja ofiar w czasie
    - y: populacja drapieżników w czasie
    - suma_populacji: łączna populacja w czasie
    """
    t = np.arange(0, total_time, dt)
    if stc:
        x = [C / D]
        y = [A / B]
    else:
        x = [prey_init]
        y = [predator_init]

    for i in range(1, len(t)):
        if stc:
            dx = x[i - 1] * ((A + StochasticTerm()) - (B + StochasticTerm()) * y[i - 1])
            dy = -y[i - 1] * ((C + StochasticTerm()) - (D + StochasticTerm()) * x[i - 1])
        else:
            dx = x[i - 1] * (A - B * y[i - 1])
            dy = -y[i - 1] * (C - D * x[i - 1])

        x.append(x[i - 1] + dx * dt)
        y.append(y[i - 1] + dy * dt)

    x = np.array(x)
    y = np.array(y)
    suma_populacji = x + y

    return t, x, y, suma_populacji
