import numpy as np
from matplotlib.lines import Line2D

from utils import Curve


class BezierCurve(Curve):
    def __init__(self, ax, control_points: np.ndarray, time_splits=100):
        """
        Initialize a BezierCurve class, draw the curve with the Casteljau
        algorithm, store all the intermediate computed points to
        `computed_points`, which is a numpy array.
        Construct the np.array in the form (t, i, j, cor), `t` stands for the
        coordinates at the specific time stamp, `i` stands for the layer
        index, `j` stands for the point index, `cor` is a 2d array, with x
        and y coordinates
        :param control_points: the control points to construct the curve,
        with the form of np.array in two dimension, each row is a pair of
        coordinates
        :param time_splits: num of splits of the time [0, 1]
        """
        super().__init__(ax)
        self.time_splits = time_splits
        self.n = control_points.shape[0]
        self.computed_points = np.zeros((self.time_splits, self.n, self.n, 2))
        self.time_stamps = np.linspace(0, 1, time_splits, endpoint=True).reshape(time_splits, 1)
        self.computed_points[:, 0] = np.tile(control_points,
                                             (time_splits, 1, 1))

        for i in range(1, self.n):
            for j in range(self.n - i):
                self.computed_points[:, i, j] = self._compute_at(i, j)

    def _compute_at(self, i, j):
        """
        Compute the point in layer `i`, index `j`
        :param i: layer `i` in recursion
        :param j: `j`th point
        """
        result = (((1 - self.time_stamps) * self.computed_points[:, i - 1, j])
                  + self.time_stamps * self.computed_points[:, i - 1, j + 1])
        return result

    @property
    def _control_points(self):
        """
        Retrieve the data for control points
        :return: Position of the control points, in the form of n x 2 np
        array, each row is the coordinates of a point
        """
        return self.computed_points[0, 0]

    @property
    def _trajectory(self):
        """
        Retrieve the data for the trajectory
        :return: Position of the trajectory, in the form of time_splits x 2
        np array
        """
        return self.computed_points[:, self.n - 1, 0]

    def _get_intermediate_points(self, time_stamp):
        """
        Return the intermediate points at the given time stamp,
        because we should draw the animation of the intermediate points
        :param time_stamp: time stamp for required intermediate points,
        range from 0 to time_splits
        :return: intermediate points along the time axis
        """
        return self.computed_points[time_stamp]
