from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from simulation import simulate_predator_prey
from find_peaks import find_distance
import numpy as np

t, x, y, suma_populacji = simulate_predator_prey()


def plot_graphs():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        c = float(entry3.get())
        d = float(entry4.get())
    except ValueError:
        messagebox.showerror("Błąd", "Wprowadź poprawne liczby!")
        return
    checkbox_value = checkbox_var.get()
    checkbox_value1 = checkbox_var1.get()

    t, x, y, suma_populacji = simulate_predator_prey(A=a, B=b, C=c, D=d, stc=checkbox_value, hides=checkbox_value1)

    ax1.clear()
    ax2.clear()

    ax1.plot(t, x)
    ax1.plot(t, y)
    ax1.set_xlabel('Czas [jednostki arbitralne]')
    ax1.set_ylabel('Liczebność Populacji')
    ax1.legend(('Ofiary', 'Drapieżcy'))
    ax1.set_title("Szeregi czasowe populacji")

    ax2.plot(x, y, zorder=1)
    ax2.scatter(c / d, a / b, c='red', s=10, zorder=2)
    ax2.set_ylabel('drapieżcy')
    ax2.set_xlabel('ofiary')
    ax2.set_title("Przestrzeń fazowa")

    label_s.config(text=f"S ({c / d:.2f},{a / b:.2f}) ")

    max_prey = np.max(x)
    max_predator = np.max(y)
    label_max_prey.config(text=f"Maks. ofiary: {max_prey:.2f}")
    label_max_predator.config(text=f"Maks. drapieżcy: {max_predator:.2f}")
    try:
        time_prey = find_distance(t, x)
        label_time_prey.config(text=f"Czas (ofiary): {time_prey:.2f}")

        time_predator = find_distance(t, y)
        label_time_predator.config(text=f"Czas (drapieżcy): {time_predator:.2f}")
    except:
        messagebox.showerror("Błąd", "jakiś błąd na razie idk")
    canvas.draw()


root = tk.Tk()
root.title("Lotkka-Voltery Model")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")
root.state('zoomed')

# Ramka na wpisy
input_frame = ttk.Frame(root)
input_frame.pack(side=tk.TOP, pady=10)

# Pola do wpisywania liczb
ttk.Label(input_frame, text="Wartość a:").grid(row=0, column=0)
entry1 = ttk.Entry(input_frame, width=10)
entry1.grid(row=1, column=0, padx=5)
entry1.insert(0, "1.0")

ttk.Label(input_frame, text="Wartość b:").grid(row=0, column=1)
entry2 = ttk.Entry(input_frame, width=10)
entry2.grid(row=1, column=1, padx=5)
entry2.insert(0, "0.1")

ttk.Label(input_frame, text="Wartość c:").grid(row=0, column=2)
entry3 = ttk.Entry(input_frame, width=10)
entry3.grid(row=1, column=2, padx=5)
entry3.insert(0, "0.5")

ttk.Label(input_frame, text="Wartość d:").grid(row=0, column=3)
entry4 = ttk.Entry(input_frame, width=10)
entry4.grid(row=1, column=3, padx=5)
entry4.insert(0, "0.01")

# Przycisk do rysowania wykresów
plot_button = ttk.Button(input_frame, text="Generuj wykresy", command=plot_graphs)
plot_button.grid(row=1, column=4, padx=10)

checkbox_var = tk.BooleanVar()
checkbox = ttk.Checkbutton(input_frame, text="włącz/wyłącz szum", variable=checkbox_var)
checkbox.grid(row=2, column=0, columnspan=4, pady=5)

checkbox_var1 = tk.BooleanVar()
checkbox1 = ttk.Checkbutton(input_frame, text="włącz/wyłącz kryjówki", variable=checkbox_var1)
checkbox1.grid(row=2, column=2, columnspan=4, pady=5)

# Miejsce na wykresy
fig = Figure(figsize=(16, 8))
ax1 = fig.add_subplot(121)  # 1 rząd, 2 kolumny, pierwszy wykres
ax2 = fig.add_subplot(122)  # 1 rząd, 2 kolumny, drugi wykres

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# Dodaj etykiety do wyświetlania wartości c / d i a / b obok przycisku
label_s = ttk.Label(input_frame, text="-")
label_s.grid(row=1, column=5, padx=10)

# Dodaj etykiety do wyświetlania maksymalnych wartości
label_max_prey = ttk.Label(input_frame, text="Maks. ofiary: -")
label_max_prey.grid(row=2, column=5, padx=10)

label_max_predator = ttk.Label(input_frame, text="Maks. drapieżcy: -")
label_max_predator.grid(row=2, column=6, padx=10)

# Dodaj etykiety do wyświetlania czasu od minimum do maksimum
label_time_prey = ttk.Label(input_frame, text="Czas (ofiary): -")
label_time_prey.grid(row=3, column=5, padx=10)

label_time_predator = ttk.Label(input_frame, text="Czas (drapieżcy): -")
label_time_predator.grid(row=3, column=6, padx=10)

if __name__ == '__main__':
    plot_graphs()
    root.mainloop()
