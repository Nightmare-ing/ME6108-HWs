import math
import csv
import unittest

import matplotlib.pyplot as plt
import numpy as np
import numpy.testing as npt

from HW2.drawer import Drawer
from HW2.trivs import trivs
from utils import read_csv


class TestTrivs(unittest.TestCase):
    def test_one_point(self):
        """
        Test the transformation of one point in different views
        """
        coors = np.array([[1, 2, 3, 1]])
        dist = 0
        front_trans_res = trivs(coors, dist, 'front profile', 0, 0)
        npt.assert_array_equal(np.array([[1, 0, 3, 1]]), front_trans_res)

        top_trans_res = trivs(coors, dist, 'top profile', 0, 0)
        npt.assert_array_equal(np.array([[1, 0, -2, 1]]), top_trans_res)

        side_trans_res = trivs(coors, dist, 'side profile', 0, 0)
        npt.assert_array_equal(np.array([[-2, 0, 3, 1]]), side_trans_res)

        theta = math.radians(45)
        fi = math.radians(35.264389682)
        iso_trans_result = trivs(coors, dist, 'isometric', theta, fi)
        expected = np.array([[np.cos(theta) - 2 * np.sin(theta),
                              0,
                              -np.sin(theta) * np.sin(fi) - 2 * np.cos(theta) * np.sin(fi) + 3 * np.cos(fi),
                              1]])
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
        dist = 1
        front_trans_res = trivs(coors, dist, 'front profile', 0, 0)
        top_trans_res = trivs(coors, dist, 'top profile', 0, 0)
        side_trans_res = trivs(coors, dist, 'side profile', 0, 0)
        drawer.draw_connected_points(front_trans_res)
        drawer.draw_connected_points(top_trans_res)
        drawer.draw_connected_points(side_trans_res)
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
        dist = 1
        theta = math.radians(45)
        fi = math.radians(35.264389682)
        iso_trans_res = trivs(coors, dist, 'isometric', theta, fi)
        drawer.draw_connected_points(iso_trans_res)
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
        actual_coors = read_csv('../data/data1.csv', 3)
        npt.assert_array_equal(expected_coors, actual_coors)



if __name__ == '__main__':
    unittest.main()