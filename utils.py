import csv
import os.path
from abc import abstractmethod, abstractproperty

import numpy as np
from matplotlib.lines import Line2D


def generate_rhombus(point1, point2):
    """
    Generate all four vertices according to the given points.
    :param point1: coordinates of the left most point
    :param point2: coordinates of the highest point
    :return: list of all four vertices
    """
    point3 = (2 * point2[0] - point1[0], point1[1])
    point4 = (point2[0], 2 * point1[1] - point2[1])
    return [point1, point2, point3, point4]


def generate_trace(rhombus_vertices):
    """
    generate discrete trace points for the given rhombus.
    :param rhombus_vertices: coordinates of the vertices of the rhombus
    :return: two numpy array of the coordinates of the discrete trace points, x, y
    """
    left_up_x = np.linspace(rhombus_vertices[0][0], rhombus_vertices[1][0], 100)
    left_up_y = np.linspace(rhombus_vertices[0][1], rhombus_vertices[1][1], 100)
    right_up_x = np.linspace(rhombus_vertices[1][0], rhombus_vertices[2][0], 100)
    right_up_y = np.linspace(rhombus_vertices[1][1], rhombus_vertices[2][1], 100)
    right_down_x = np.linspace(rhombus_vertices[2][0], rhombus_vertices[3][0], 100)
    right_down_y = np.linspace(rhombus_vertices[2][1], rhombus_vertices[3][1], 100)
    left_down_x = np.linspace(rhombus_vertices[3][0], rhombus_vertices[0][0], 100)
    left_down_y = np.linspace(rhombus_vertices[3][1], rhombus_vertices[0][1], 100)
    return np.concatenate((left_up_x, right_up_x, right_down_x, left_down_x)), np.concatenate(
        (left_up_y, right_up_y, right_down_y, left_down_y))


def read_homogeneous_coor(file_path, data_per_row):
    """
    Read the csv file and return the homogeneous coordinates data as a
    numpy array
    :param file_path: the path of the csv file
    :param data_per_row: number of data in each row
    :return: the data in the csv file, in the form of numpy array
    """
    coors = read_coor(file_path, data_per_row)
    return np.hstack((coors, np.ones((coors.shape[0], 1))))

def read_coor(file_path, data_per_row):
    """
    Read the csv file and return the 2d coordinates data as a numpy array
    :param file_path: the path of the csv file
    :param data_per_row: number of data in each row
    :return: the data in the csv file, in the form of numpy array
    """
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        coors = []
        for row in reader:
            if len(row) != data_per_row:
                raise ValueError('Invalid data format')
            coors.append([float(i) for i in row])
        coors = np.array(coors)
    return coors

def read_data_prompt(hw):
    """
    Prompt when reading a test data file
    :param hw: String for HWs, for example "HW1", "HW2", ...
    :return: path of the file
    """
    print("This is the demo of my {}, there are some sample files under "
          "{}/data, you can use them to test the program".format(hw, hw))
    print("Or you can put your own data file under {}/data and test "
          "them.".format(hw))

    while True:
        file = input("Please choose the data file you want to test(data1.csv or "
                     "data2.csv): ")
        file_path = os.path.join(os.getcwd(), hw, 'data', file)
        if not os.path.exists(file_path):
            print("The file does not exist, please try again.")
        else:
            break

    print("You choose to test the file: ", file)
    return file_path

class Curve:
    def __init__(self, ax):
        """
        Basic properties of a custom curve class
        :param ax: the Axes object to draw the curve
        """
        self.ax = ax
        # properties for drawing
        self.control_line_artists = None
        self.intermediate_line_artists = None
        self.trajectory_artists = None

    @property
    @abstractmethod
    def _control_points(self):
        """
        Retrieve the data for control points
        :return: Position of the control points, in the form of n x 2 np
        array, each row is the coordinates of a point
        """
        pass

    @property
    @abstractmethod
    def _trajectory(self):
        """
        Retrieve the data for the trajectory.
        :return: Position of the trajectory, in the form of time_splits x 2
        np array
        """
        pass

    @abstractmethod
    def _get_intermediate_points(self, time_stamp):
        """
        Return the intermediate points at the given time stamp,
        because we should draw the animation of the intermediate points
        :param time_stamp: time stamp for required intermediate points.
        :return: intermediate points along the time axis
        """
        pass

    def initialize_artists(self):
        """
        Initialize the drawing Artists
        """
        self.control_line_artists = Line2D(self._control_points[:, 0],
                                           self._control_points[:, 1],
                                           marker='o', color='green',
                                           linewidth=2)
        self.intermediate_line_artists = [Line2D(layer[0, 0:1],
                                                 layer[0, 1:2],
                                                 marker='.', color='blue')
                                          for layer in
                                          self._get_intermediate_points(0)[1:-1]]
        self.trajectory_artists = Line2D(self._trajectory[0, 0:1],
                                         self._trajectory[0, 1:2],
                                         color='red', linewidth=3)
        artists = ([self.control_line_artists] + self.intermediate_line_artists
                   + [self.trajectory_artists])
        for artist in artists:
            self.ax.add_line(artist)
        return artists

    def update(self, frame):
        """
        Update the properties of the artists for each frame of the animation
        :param frame: frame number of the animation, equal to the timestamp
        of the evolution of the line
        :return: updated Artists
        """
        # update intermediate lines
        for l in range(1, self.n - 1):
            l_index = l - 1
            self.intermediate_line_artists[l_index].set_data(
                self._get_intermediate_points(frame)[l][:self.n - l].T)

        # update trajectory line
        self.trajectory_artists.set_data(self._trajectory[:frame].T)
        return [self.control_line_artists] + self.intermediate_line_artists + [self.trajectory_artists]
