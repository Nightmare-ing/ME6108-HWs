import ast
from matplotlib.ticker import MultipleLocator
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

def get_input():
    """
    Get input coordinates, expect two tuples with form (1, 2) (1, 2)
    """
    while True:
        input_start = input("Enter the coordinate of the starting point, for example (1, 2): ")
        input_end = input("Enter the coordinate of the ending point, for example (1, 2): ")
        try:
            start = ast.literal_eval(input_start)
            end = ast.literal_eval(input_end)
            if not isinstance(start, tuple) or not isinstance(end, tuple):
                print("Coordinates entered is not valid, please try again.")
            else:
                return start, end
        except (SyntaxError, ValueError):
            print("Invalid input type")
            break


def line_drawer(x, y):
    fig, ax = plt.subplots()
    ax.set_xlim(-10, 10)
    ax.xaxis.set_major_locator(MultipleLocator(2))
    ax.xaxis.set_minor_locator(MultipleLocator(1))
    ax.set_ylim(-10, 10)
    ax.yaxis.set_major_locator(MultipleLocator(2))
    ax.yaxis.set_minor_locator(MultipleLocator(1))
    ax.grid(which='minor', linestyle=':', linewidth=0.5)
    ax.grid(True)
    ax.set_aspect('equal')
    ax.scatter(x, y)
    return fig, ax


def circle_drawer(x, y, center, radius):
    fig, ax = line_drawer(x, y)
    ax.add_patch(mpatches.Circle(center, radius, edgecolor='blue', facecolor='none', linewidth=1, linestyle=':'))

