import unittest
import numpy.testing as npt
from HW1.scanning_algorithms import bresenham_line_standard, bresenham_line_optimized


class TestPixels(unittest.TestCase):
    def test_slope1(self):
        start = (-3, -3)
        end = (3, 3)
        expected_x, expected_y = bresenham_line_standard(start, end, 6)
        actual_x, actual_y = bresenham_line_optimized(start, end, 6)
        npt.assert_array_equal(expected_x, actual_x)
        npt.assert_array_equal(expected_y, actual_y)

    def test_slope_less_1(self):
        start = (-3, -3)
        end = (3, -1)
        expected_x, expected_y = bresenham_line_standard(start, end, 6)
        actual_x, actual_y = bresenham_line_optimized(start, end, 6)
        npt.assert_array_equal(expected_x, actual_x)
        npt.assert_array_equal(expected_y, actual_y)



if __name__ == '__main__':
    unittest.main()
