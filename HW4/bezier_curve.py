import numpy as np
from matplotlib.patches import Circle

class BezierCurve:
    def __init__(self, control_points: np.ndarray, time_splits=100):
        """
        Initialize a BezierCurve class, draw the curve with the Casteljau
        algorithm, store all the intermediate computed points to
        `computed_points`, which is a numpy array.
        Construct the np.array in the form (i, j, t, cor), `i` stands for
        the layer index, `j` stands for the point index, `t` stands for the
        coordinates at the specific time stamp, `cor` is a 2d array, with x
        and y coordinates
        :param control_points: the control points to construct the curve,
        with the form of np.array in two dimension, each row is a pair of
        coordinates
        :param time_splits: num of splits of the time [0, 1]
        """
        self.n = control_points.shape[1]
        self.time_stamps = np.linspace(0, 1, time_splits, endpoint=True)
        self.computed_points = np.zeros((self.n, self.n, time_splits, 2))
        self.computed_points[0] = np.tile(control_points,
                                          (time_splits, 1, 1))

    def generate(self, i, j):
        """
        Generate the point in layer `i`, index `j`
        :param i: layer `i` in recursion
        :param j: `j`th point
        """
        self.computed_points[i, j] = (((1 - self.time_stamps) *
                                      self.computed_points[i - 1,
                                      j]) - self.time_stamps *
                                      self.computed_points[i - 1, j + 1])

    def compute(self):
        """
        Compute all the intermediate and the final points for generating the Bezier Curve
        """
        for i in range(self.n):
            for j in range(i):
                self.generate(i, j)

    def get_control_points(self):
        """
        Return the control points Artists
        :return: the control points artists for Matplotlib to draw
        """
        drawing_points = [Circle(self.computed_points[0, index, 0, :].tolist(), 0.1)
                          for index in range(self.n)]
        return drawing_points

    
