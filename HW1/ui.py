import ast

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


def get_input_line():
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


def get_input_circle():
    """
    Get input coordinates, expect a tuple and an integer with form (1, 2) 1
    """
    while True:
        input_center = input("Enter the coordinate of the center, for example (1, 2): ")
        input_radius = input("Enter the radius of the circle, for example 1: ")
        try:
            center = ast.literal_eval(input_center)
            radius = int(input_radius)
            if not isinstance(center, tuple) or not isinstance(radius, int):
                print("Coordinates entered is not valid, please try again.")
            else:
                return center, radius
        except (SyntaxError, ValueError):
            print("Invalid input type")
            break

class Drawer:
    def __init__(self):
        self.fig, self.ax = plt.subplots()

    def set_fig(self, xlim=(-10, 10), ylim=(-10, 10), major_locator=2, minor_locator=1, grid=True, minor_grid=True,
                aspect='equal'):
        """
        Set the figure with xlim, ylim, major_locator, minor_locator, grid, minor_grid, aspect
        :param xlim: x limit
        :param ylim: y limit
        :param major_locator: major locator for x and y axis
        :param minor_locator: minor locator for x and y axis
        :param grid: show grid or not
        :param minor_grid: show minor grid or not
        :param aspect: set aspect of the figure
        :return:
        """
        self.ax.set_xlim(xlim)
        self.ax.xaxis.set_major_locator(MultipleLocator(major_locator))
        self.ax.xaxis.set_minor_locator(MultipleLocator(minor_locator))
        self.ax.set_ylim(ylim)
        self.ax.yaxis.set_major_locator(MultipleLocator(major_locator))
        self.ax.yaxis.set_minor_locator(MultipleLocator(minor_locator))
        if grid:
            self.ax.grid(which='major', linestyle='-', linewidth=0.5)
        if minor_grid:
            self.ax.grid(which='minor', linestyle=':', linewidth=0.5)
        self.ax.set_aspect(aspect)

    def line_drawer(self, x, y):
        """
        Draw the line with x, y coordinates
        """
        self.ax.scatter(x, y)

    def circle_drawer(self, x, y, center, radius):
        """
        Draw the circle with discrete points, also draw the desired circle
        :param x: x coordinates of the discrete points, numpy array
        :param y: y coordinates of the discrete points, numpy array
        :param center: center of the circle
        :param radius: radius of the circle
        :return:
        """
        self.ax.scatter(x, y)
        self.ax.add_patch(
            mpatches.Circle(center, radius, edgecolor='blue', facecolor='none', linewidth=1, linestyle=':'))
