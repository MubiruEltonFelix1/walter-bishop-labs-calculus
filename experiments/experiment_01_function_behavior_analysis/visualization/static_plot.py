import numpy as np
import matplotlib.pyplot as plt
from calculus.function import f

def plot_function():
    x=np.linspace(-2,4,400)
    y=f(x)
    plt.figure(figsize=(8,5))

    plt.plot(x,y,label="f(x)")
    plt.axhline(0)
    plt.axvline(0)

    plt.title("Walter Bishop Calculus Experiment")
    plt.xlabel("x")
    plt.ylabel("y")

    plt.grid(True)
    plt.legend()

    plt.show()