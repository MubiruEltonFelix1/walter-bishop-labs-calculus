import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import sympy as sp
from calculus.function import f
from calculus.derivatives import first_derivative, x as sym_x

def animate_function():
    plt.style.use('dark_background')

    f_prime = sp.lambdify(sym_x, first_derivative, 'numpy')

    x = np.linspace(-2, 4, 200)
    fig, ax = plt.subplots()
    line,    = ax.plot([], [], linewidth=2,   label="f(x)")
    tangent, = ax.plot([], [], linewidth=1.5, label="tangent",
                       linestyle='--', color='tomato')
    dot,     = ax.plot([], [], 'o', color='tomato', markersize=6)

    ax.set_xlim(-2, 4)
    ax.set_ylim(-10, 10)
    ax.set_title("Animated Calculus Experiment")
    ax.legend(loc='upper left')

    def update(frame):
        if frame == 0:
            line.set_data([], [])
            tangent.set_data([], [])
            dot.set_data([], [])
            return line, tangent, dot

        x_data = x[:frame]
        y_data = f(x_data)
        line.set_data(x_data, y_data)

        # Tangent line at the leading point
        x_tip   = x[frame - 1]
        y_tip   = float(f(x_tip))
        slope   = float(f_prime(x_tip))
        t       = np.linspace(x_tip - 0.6, x_tip + 0.6, 60)
        tangent.set_data(t, y_tip + slope * (t - x_tip))
        dot.set_data([x_tip], [y_tip])

        return line, tangent, dot

    animation = FuncAnimation(
        fig,
        update,
        frames=len(x),
        interval=20
    )
    plt.show()