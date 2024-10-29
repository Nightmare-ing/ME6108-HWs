import math
import unittest

import numpy as np
import numpy.testing as npt

from HW1.animation import theta
from HW2.trivs import trivs


class TestTrivs(unittest.TestCase):
    def test_one_point(self):
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
        iso_trans_result = trivs(coors, dist, 'isometric', np.pi/4, 0)
        expected = np.array([[np.cos(theta) - 2 * np.sin(theta),
                              0,
                              -np.sin(theta) * np.sin(fi) - 2 * np.cos(theta) * np.sin(fi) + 3 * np.cos(fi),
                              1]])
        npt.assert_array_equal(expected, iso_trans_result)
