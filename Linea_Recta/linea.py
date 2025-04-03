import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class LineaRecta:
    def __init__(self, root):
        self.root = root
        self.root.title("Línea Recta")
        self.root.geometry("400x400")

        self.m_var = DoubleVar()
        self.b_var = DoubleVar()

        self.fig, self.ax = plt.subplots()
        self.x = np.arange(-10, 10, 0.1)

        self.componentes()

    def componentes(self):
        Label(self.root, text="y = mx + b").pack()

        Label(self.root, text="Valor de m").pack()
        Entry(self.root, textvariable=self.m_var).pack()

        Label(self.root, text="Valor de b").pack()
        Entry(self.root, textvariable=self.b_var).pack()

        Button(self.root, text="Graficar", command=self.grafica).pack()

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack()

    def grafica(self):
        m = self.m_var.get()
        b = self.b_var.get()
        y = m * self.x + b

        self.ax.clear()
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-10, 10)

        self.ax.axhline(0, color='black', linewidth=1)
        self.ax.axvline(0, color='black', linewidth=1)
        self.ax.grid(True, linestyle="--", linewidth=0.5)

        self.ax.plot(self.x, y, label=f"y = {m}x + {b}", color="red")
        self.ax.legend()

        self.canvas.draw()

root = Tk()
app = LineaRecta(root)
root.mainloop()