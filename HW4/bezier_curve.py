import numpy as np
from matplotlib.patches import Circle
from matplotlib.lines import Line2D

class BezierCurve:
    def __init__(self, control_points: np.ndarray, time_splits=100):
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
        self.time_splits = time_splits
        self.n = control_points.shape[1]
        self.time_stamps = np.linspace(0, 1, time_splits, endpoint=True)
        self.computed_points = np.zeros((time_splits, self.n, self.n, 2))
        self.computed_points[:, 0] = np.tile(control_points,
                                          (time_splits, 1, 1))

        # properties for drawing
        self.control_line_artists = None
        self.intermediate_line_artists = None
        self.trajectory_artists = None

    def generate(self, i, j):
        """
        Generate the point in layer `i`, index `j`
        :param i: layer `i` in recursion
        :param j: `j`th point
        """
        self.computed_points[:, i, j] = (((1 - self.time_stamps) *
                                      self.computed_points[:, i - 1, j])
                                         - self.time_stamps *
                                      self.computed_points[:, i - 1, j + 1])

    def compute(self):
        """
        Compute all the intermediate and the final points for generating the Bezier Curve
        """
        for i in range(self.n):
            for j in range(self.n - i):
                self.generate(i, j)

    @property
    def control_points(self):
        """
        Retrieve the data for control points
        :return: Position of the control points, in the form of n x 2 np
        array, each row is the coordinates of a point
        """
        return self.computed_points[0, 0]

    @property
    def trajectory(self):
        """
        Retrieve the data for the trajectory
        :return: Position of the trajectory, in the form of time_splits x 2
        np array
        """
        return self.computed_points[:, self.n - 1, 0]

    def get_intermediate_points(self, time_stamp):
        """
        Return the intermediate points at the given time stamp,
        because we should draw the animation of the intermediate points
        :param time_stamp: time stamp for required intermediate points,
        range from 0 to time_splits
        :return: intermediate points along the time axis
        """
        return self.computed_points[time_stamp]

    def initialize_drawing(self):
        """
        Initialize the drawing Artists
        """
        self.control_line_artists = Line2D(self.computed_points[0, 0, :, 0],
                                           self.computed_points[0, 0, :, 1],
                                           marker='o')
        self.intermediate_line_artists = [Line2D(layer[:, 0], layer[:, 1],
                                                 marker='.')
                                          for layer in
                                          self.computed_points[0]]
        self.trajectory_artists = Line2D(self.computed_points[0, self.n - 1,
        0, 0], self.computed_points[0, self.n - 1, 0, 1])
        return ([self.control_line_artists] + self.intermediate_line_artists
                + [self.trajectory_artists])

