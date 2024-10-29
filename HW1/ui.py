import ast
import math

import matplotlib.animation as animation
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

from HW1.utils import generate_rhombus, generate_trace


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

class ScanningDrawer:
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


class AnimationDrawer:
    def __init__(self, window_width=200, window_height=150, margin=15, radius=6):
        self.fig, self.ax = plt.subplots()
        self.ball = None
        self.animation_paused = False
        self.ani = None
        self.trace_x = None
        self.trace_y = None
        self.window_width = window_width
        self.window_height = window_height
        self.margin = margin
        self.radius = radius

    def set_fig(self):
        # Compute some parameters for the animation
        rec_start = (self.margin, self.margin)
        rec_width = float(self.window_width - 2 * self.margin)
        rec_height = float(self.window_height - 2 * self.margin)
        edge_rhombus = generate_rhombus((rec_start[0], rec_start[1] +
                                         rec_height / 2.0), (rec_start[0] +
                                                             rec_width / 2.0, rec_start[1] + rec_height))

        self.ax.set_aspect('equal')
        self.ax.set_xlim(0, self.window_width)
        self.ax.set_ylim(0, self.window_height)

        # Draw the rectangle and the rhombus
        self.ax.add_patch(mpatches.Rectangle(rec_start, rec_width, rec_height, fc='none',
                                        edgecolor='blue',
                                        linewidth=1, linestyle='--'))
        self.ax.add_patch(mpatches.Polygon(edge_rhombus, closed=True,
                                      edgecolor='blue', fc='none'))

        theta = math.atan((edge_rhombus[1][1] - edge_rhombus[0][1]) / (edge_rhombus[1][0] - edge_rhombus[0][0]))
        trace_rhombus = generate_rhombus((edge_rhombus[0][0] + self.radius / math.sin(theta), edge_rhombus[0][1]),
                                         (edge_rhombus[1][0], edge_rhombus[1][1] - self.radius / math.cos(theta)))
        self.trace_x, self.trace_y = generate_trace(trace_rhombus)
        self.ball = self.ax.add_patch(mpatches.Circle((self.trace_x[0], self.trace_y[0]), self.radius,
                                            color='red',
                                            fc='none'))

    def update(self, frame):
        """
        For updating each frame of the animation
        :param frame: represent which frame
        :return: updated Artiest objects
        """
        self.ball.set_center((self.trace_x[frame % self.trace_x.size],
                         self.trace_y[frame % self.trace_y.size]))

    def press(self, event):
        """
        For handling key press event
        :param event:  object transferred in
        :return: None
        """
        if event.key is not None:
            if self.animation_paused:
                self.ani.event_source.start()
            else:
                self.ani.event_source.stop()
            self.animation_paused = not self.animation_paused

    def show_animation(self):
        """
        Show the animation of the ball moving along the trace
        """
        self.ani = animation.FuncAnimation(self.fig, self.update, frames=1000, interval=10, blit=False)
        self.fig.canvas.mpl_connect('key_press_event', self.press)