import numpy as np
from matplotlib.lines import Line2D

from utils import Curve


class BSpline(Curve):
    def __init__(self, ax, control_points: np.ndarray, k, sect_time_splits=100):
        """
        Initialize a B-Spline class, draw the curve with the De Boor algorithm,
        store all the intermediate computed points to `computed_points`, which
        is a numpy array.
        :param ax: the Axes object to draw the curve
        :param control_points: the control points to construct the curve, with
        the form of np array in two dimension, each row is a pair of
        coordinates
        :param k: order of the B-Spline
        :param sect_time_splits: num of splits of the time.
        """
        super().__init__(ax)
        self.sect_time_splits = sect_time_splits
        self.sect_timestamps = np.linspace(0, 1, sect_time_splits,
                                           endpoint=True).reshape(sect_time_splits, 1)

        self.k = k
        # n + 1 control points
        self.n = control_points.shape[0] - 1
        # values for l
        self.ls = np.arange(1, self.k + 1)
        # the nodes vector
        self.nodes = np.arange(self.k + self.n + 2)
        # values for j, means the number of sections of the BSpline
        self.js = [(index, item) for index, item in enumerate(range(self.k, self.n + 1))]
        # total number of timestamps
        self.time_stamps_num = self.sect_time_splits * len(self.js)

        self.computed_points = np.zeros((len(self.js),
                                         self.sect_time_splits, self.ls.size + 1,
                                         self.n + 1, 2))
        self.computed_points[:, :, 0] = np.tile(control_points,
                                                (len(self.js),
                                                 self.sect_time_splits, 1, 1))
        self._compute_points()

    def _compute_section_at(self, l, i, j_pack):
        """
        Compute the point `i` at layer `l`, between nodes `j` and `j + 1`,
        which is a section of the B Spline.
        :param l: Layer index
        :param i: Index of the point
        :param j_pack: tuple, (section index, node index of j)
        """
        t_index = i + self.k - l + 1
        sect_index, j = j_pack
        t = self.sect_timestamps + j
        t_coeff = (self.nodes[t_index] - t) / (self.nodes[t_index] -
                                            self.nodes[i])
        self.computed_points[sect_index, :, l, i] = (t_coeff *
                                                     self.computed_points[
                                                     sect_index, :, l - 1, i - 1] +
                                                     (1 - t_coeff) *
                                                     self.computed_points[sect_index, :, l - 1, i])

    def _compute_points(self):
        """
        Compute all the points of the B-Spline in this 5d np array
        """
        for j_pack in self.js:
            for l in range(1, self.k + 1):
                for i in range(max(j_pack[1] - self.k + l, 0), j_pack[1] + 1):
                    self._compute_section_at(l, i, j_pack)

    @property
    def _control_points(self):
        """
        Retrieve the data for control points
        :return: Position of the control points, in the form of n x 2 np
        array, each row is the coordinates of a point
        """
        return self.computed_points[0, 0, 0]

    @property
    def _trajectory(self):
        """
        Retrieve the data for the trajectory.
        Reshape the array to link all sections of the B-Spline, so we can
        draw along all the nodes.
        :return: Position of the trajectory, in the form of time_splits x 2
        np array
        """
        result = np.zeros((len(self.js), self.sect_time_splits, 2))
        for sect_index, j in self.js:
            result[sect_index] = self.computed_points[sect_index, :,
                                  self.ls[-1], j]
        return result.reshape(len(self.js) * self.sect_time_splits, 2)

    def get_intermediate_points(self, time_stamp):
        """
        Return the intermediate points at the given time stamp,
        because we should draw the animation of the intermediate points
        :param time_stamp: time stamp for required intermediate points,
        range from 0 to time_splits * (self.nodes.size - 1)
        :return: intermediate points along the time axis
        """
        sect_index = time_stamp // self.sect_time_splits
        return self.computed_points[sect_index, time_stamp % self.sect_time_splits]

    def update(self, frame):
        """
        Update the artists for the animation
        :param frame: frame index
        :return: updated artists
        """
        _, j = self.js[frame // self.sect_time_splits]
        for l in self.ls[:-1]:
            l_index = l - 1
            i_lower_bound = j - self.k + l
            self.intermediate_line_artists[l_index].set_data(
                self.get_intermediate_points(frame)[l,
                i_lower_bound:j+1].T)
        self.trajectory_artists.set_data(self._trajectory[0:frame].T)
        return [self.control_line_artists] + self.intermediate_line_artists + \
                [self.trajectory_artists]
