import math

import matplotlib.pyplot as plt
import numpy as np

from HW2.trivs import trivs


class Drawer:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        # invert the x-axis
        self.fig.gca().invert_xaxis()

    def draw_connected_points(self, coordinates):
        """
        Draw connected points with given coordinates
        :param coordinates: np.array, [[x1, y1], [x2, y2], ...]
        """
        self.ax.plot(coordinates[:, 0], coordinates[:, 1])

    def draw_three_view_fig(self, coors):
        """
        Draw three views of the given coordinates
        """
        dist = max(np.max(coors) / 10, 1)
        front_trans_res = trivs(coors, 'front profile', 0, 0, dist)
        top_trans_res = trivs(coors, 'top profile', 0, 0, dist)
        side_trans_res = trivs(coors, 'side profile', 0, 0, dist)
        self.draw_connected_points(front_trans_res)
        self.draw_connected_points(top_trans_res)
        self.draw_connected_points(side_trans_res)

    def draw_isometric_fig(self, coors, theta=45.0, fi=35.264389682):
        """
        Draw isometric view of the given coordinates
        """
        dist = 1
        theta = math.radians(theta)
        fi = math.radians(fi)
        iso_trans_res = trivs(coors, 'isometric', theta, fi)
        self.draw_connected_points(iso_trans_res)

