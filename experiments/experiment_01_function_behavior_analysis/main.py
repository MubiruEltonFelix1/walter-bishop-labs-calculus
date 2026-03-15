from calculus.derivatives import get_derivatives
from calculus.analysis import find_critical_points
from visualization.static_plot import plot_function
from visualization.animation_plot import animate_function

def run_experiment():

    d1, d2 = get_derivatives()

    print("\nFirst derivative:")
    print(d1)

    print("\nSecond derivative:")
    print(d2)

    print("\nCritical points:")
    print(find_critical_points())

    print("\nDisplaying static graph...")
    plot_function()

    print("\nRunning animated visualization...")
    animate_function()


if __name__ == "__main__":
    run_experiment()