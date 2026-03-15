import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from calculus.function import f

def animate_function():
    x=np.linspace(-2,4,200)
    fig, ax=plt.subplots()
    line, = ax.plot([],[])

    ax.set_xlim(-2,4)
    ax.set_ylim(-10,10)
    ax.set_title("Animated Calculus Experiment")

    def update(frame):
        x_data=x[:frame]
        y_data=f(x_data)

        line.set_data(x_data, y_data)
        return line, 

    animation = FuncAnimation(
        fig,
        update,
        frames=len(x),
        interval=20
    )
    plt.show()