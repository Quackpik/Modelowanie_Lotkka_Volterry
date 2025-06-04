import numpy as np
from scipy.integrate import solve_ivp


def StochasticTerm(amp=0.1):
    rand = amp * np.random.uniform(-1, 1)
    if np.abs(rand) > 1:
        return 0
    else:
        return rand

def hide():
    return 30


def simulate_predator_prey(
        dt=0.0001,
        total_time=100,
        prey_init=100,
        predator_init=20,
        A=1.0,
        B=0.1,
        C=0.5,
        D=0.01,
        stc=False,
        hides=False
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
        x0 = C / D
        y0 = A / B
    else:
        x0 = prey_init
        y0 = predator_init

    def lotka_volterra(t, z):
        x, y = z
        if stc and not hides:
            dxdt = x * ((A + StochasticTerm()) - (B + StochasticTerm()) * y)
            dydt = -y * ((C + StochasticTerm()) - (D + StochasticTerm()) * x)
        elif hides and not stc:
            h = hide()
            dxdt = x * (A - B * (y - h))
            dydt = -y * (C - D * x)
        elif stc and hides:
            h = hide()
            dxdt = x * ((A + StochasticTerm()) - (B + StochasticTerm()) * (y - h))
            dydt = -(y - h) * ((C + StochasticTerm()) - (D + StochasticTerm()) * x)
        else:
            dxdt = x * (A - B * y)
            dydt = -y * (C - D * x)
        return [dxdt, dydt]

    z0 = np.array([x0, y0], dtype=float)

    t_span = (0, total_time)
    t_eval = np.linspace(*t_span, 1000)

    sol = solve_ivp(lotka_volterra, t_span, z0, t_eval=t_eval, method='RK45')

    t = sol.t
    x = sol.y[0]
    y = sol.y[1]
    suma_populacji = x + y

    return t, x, y, suma_populacji


