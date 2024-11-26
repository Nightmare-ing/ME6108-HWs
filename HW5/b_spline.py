import numpy as np


class BSpline:
    def __init__(self, ax, control_points: np.ndarray, k, time_splits=100):
        """
        Initialize a B-Spline class, draw the curve with the De Boor algorithm,
        store all the intermediate computed points to `computed_points`, which
        is a numpy array.
        :param ax: the Axes object to draw the curve
        :param control_points: the control points to construct the curve, with
        the form of np array in two dimension, each row is a pair of
        coordinates
        :param k: order of the B-Spline
        :param time_splits: num of splits of the time.
        """
        self.ax = ax
        self.time_splits = time_splits

        self.k = k
        # n + 1 control points
        self.n = control_points.shape[0] - 1
        self.l = np.arange(1, self.k + 1)
        self.nodes = np.arange(self.n + self.k + 2)

        self.computed_points = np.zeros((self.nodes.size - 1,
                                         self.time_splits, self.n + 1,
                                         self.l.size + 1, 2))
        self.computed_points[:, :, 0] = np.tile(control_points,
                                                (self.nodes.size - 1,
                                                 self.time_splits, 1, 1))
