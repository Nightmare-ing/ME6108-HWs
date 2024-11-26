import numpy as np
from matplotlib.lines import Line2D


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
        self.timestamps = np.linspace(0, 1, time_splits,
                                      endpoint=True).reshape(time_splits, 1)

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
        self._compute_points()

        self.control_line_artists = None
        self.intermediate_line_artists = None
        self.trajectory_artists = None


    def _compute_section_at(self, l, i, j):
        """
        Compute the point `i` at layer `l`, between nodes `j` and `j + 1`,
        which is a section of the B Spline.
        :param l: Layer index
        :param i: Index of the point
        :param j: Index of the node
        :return Point coordinates at layer `l`, index `i`, between node `j`
        and node `j + 1`, in the form of 2d array, the first array
        represents the timestamps, the second array represents the x and y
        coordinates of the point
        """
        t_index = i + self.k - l + 1
        t = self.timestamps + self.nodes[j]
        t_coeff = (self.nodes[t_index] - t) / (self.nodes[t_index] -
                                                self.nodes[i])
        result = t_coeff * self.computed_points[j, :, i - 1, l - 1] + \
                    (1 - t_coeff) * self.computed_points[j, :, i, l - 1]
        return result

    def _compute_points(self):
        """
        Compute all the points of the B-Spline in this 5d np array
        """
        for j in self.nodes[:-1]:
            for l in range(1, self.k + 1):
                for i in range(j - self.k + l, j + 1):
                    self.computed_points[j, :, l, i] = (
                        self._compute_section_at(l, i, j))

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
        result = np.zeros((self.nodes.size - 1, self.time_splits, 2))
        for j in range(self.nodes.size - 1):
            result[j] = self.computed_points[j, :, self.l.size, j]
        return result.reshape((self.nodes.size - 1) * self.time_splits, 2)

    def get_intermediate_points(self, time_stamp):
        """
        Return the intermediate points at the given time stamp,
        because we should draw the animation of the intermediate points
        :param time_stamp: time stamp for required intermediate points,
        range from 0 to time_splits * (self.nodes.size - 1)
        :return: intermediate points along the time axis
        """
        j = time_stamp // self.time_splits
        return self.computed_points[j, time_stamp % self.time_splits]

    def initialize_artists(self):
        """
        Initialize the artists for the animation
        :return: artists for the animation
        """
        self.control_line_artists = Line2D(self._control_points[:, 0],
                                           self._control_points[:, 1],
                marker='o', color='green', linewidth=2)
        self.intermediate_line_artists = [Line2D(layer[0, 0:1], layer[0, 1:2],
                                                 marker='.', color='blue')
                                          for index, layer in
                                          enumerate(self.get_intermediate_points(0))]
        self.trajectory_artists = Line2D(self._trajectory[0, 0:1],
                                         self._trajectory[0, 1:2],
                                         color='red')
        artists = ([self.control_line_artists] + self.intermediate_line_artists
                   + [self.trajectory_artists])
        for artist in artists:
            self.ax.add_line(artist)
        return artists

    def update(self, frame):
        """
        Update the artists for the animation
        :param frame: frame index
        :return: updated artists
        """
        j = frame // self.time_splits
        for layer_index in range(self.nodes.size - 1):
            i_lower_bound = j - self.k + self.nodes.size - 1
            self.intermediate_line_artists[layer_index].set_data(
                self.get_intermediate_points(frame)[layer_index,
                i_lower_bound:j+1].T)
        self.trajectory_artists.set_data(self._trajectory[0:frame, 0].T)
