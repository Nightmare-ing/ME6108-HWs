import timeit
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

    def test_slope_greater_1_standard(self):
        start = (-3, -3)
        end = (-1, 3)
        expected_y, expected_x = bresenham_line_standard(start, (end[1], end[0]), 6)
        actual_x, actual_y = bresenham_line_standard(start, end, 6)
        npt.assert_array_equal(expected_x, actual_x)
        npt.assert_array_equal(expected_y, actual_y)

    def test_slope_greater_1(self):
        start = (-3, -3)
        end = (-1, 3)
        expected_x, expected_y = bresenham_line_standard(start, end, 6)
        actual_x, actual_y = bresenham_line_optimized(start, end, 6)
        npt.assert_array_equal(expected_x, actual_x)
        npt.assert_array_equal(expected_y, actual_y)

    def test_performance(self):
        start = (-10, -10)
        end = (10, 5)
        subdivisions = 100000
        elapsed_time_for_standard = timeit.timeit(lambda: bresenham_line_standard(start, end, subdivisions),
                                                  number=10)
        elapsed_time_for_opt = timeit.timeit(lambda: bresenham_line_optimized(start, end, subdivisions),
                                             number=10)
        print(f"Time used for standard scanning algorithm: {elapsed_time_for_standard:.4f} seconds")
        print(f"Time used for optimized parallel algorithm: {elapsed_time_for_opt:.4f} seconds")


if __name__ == '__main__':
    unittest.main()
