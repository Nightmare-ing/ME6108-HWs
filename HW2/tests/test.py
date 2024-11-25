import math
import csv
import unittest

import matplotlib.pyplot as plt
import numpy as np
import numpy.testing as npt

from HW2.drawer import Drawer
from HW2.trivs import trivs
from utils import read_homogeneous_coor


class TestTrivs(unittest.TestCase):
    def test_one_point(self):
        """
        Test the transformation of one point in different views
        """
        coors = np.array([[1, 2, 3, 1]])
        dist = 0
        front_trans_res = trivs(coors, 'front profile', 0, 0, dist)
        npt.assert_array_equal(np.array([[1, 3]]), front_trans_res)

        top_trans_res = trivs(coors, 'top profile', 0, 0, dist)
        npt.assert_array_equal(np.array([[1, -2]]), top_trans_res)

        side_trans_res = trivs(coors, 'side profile', 0, 0, dist)
        npt.assert_array_equal(np.array([[-2, 3]]), side_trans_res)

        theta = math.radians(45)
        fi = math.radians(35.264389682)
        iso_trans_result = trivs(coors, 'isometric', theta, fi)
        expected = np.array([[np.cos(theta) - 2 * np.sin(theta),
                              -np.sin(theta) * np.sin(fi) - 2 * np.cos(theta) * np.sin(fi) + 3 * np.cos(fi)]])
        npt.assert_array_equal(expected, iso_trans_result)

    def test_drawer(self):
        coors = np.array([[0, 0],
                          [0, 1],
                          [1, 1],
                          [1, 0],
                          [0, 0]])
        drawer = Drawer()
        drawer.draw_connected_points(coors)
        plt.show()

    def test_three_view_fig(self):
        drawer = Drawer()
        coors = np.array([[0, 20, 15, 1],
                          [0, 20, 0, 1],
                          [30, 20, 0, 1],
                          [0, 20, 15, 1],
                          [0, 0, 15, 1],
                          [30, 0, 0, 1],
                          [30, 20, 0, 1]])
        drawer.draw_three_view_fig(coors)
        plt.show()

    def test_isometric_fig(self):
        drawer = Drawer()
        coors = np.array([[0, 20, 15, 1],
                          [0, 20, 0, 1],
                          [30, 20, 0, 1],
                          [0, 20, 15, 1],
                          [0, 0, 15, 1],
                          [30, 0, 0, 1],
                          [30, 20, 0, 1]])
        drawer.draw_isometric_fig(coors)
        plt.show()


class TestReadFile(unittest.TestCase):
    def test_read_file(self):
        expected_coors = np.array([[0, 20, 15, 1],
                                   [0, 20, 0, 1],
                                   [30, 20, 0, 1],
                                   [0, 20, 15, 1],
                                   [0, 0, 15, 1],
                                   [30, 0, 0, 1],
                                   [30, 20, 0, 1]])
        actual_coors = read_homogeneous_coor('../data/data1.csv', 3)
        npt.assert_array_equal(expected_coors, actual_coors)


if __name__ == '__main__':
    unittest.main()