import matplotlib.pyplot as plt
import unittest
from unittest.mock import patch
from io import StringIO


from HW1.scanning_algorithms import bresenham_line_optimized, bresenham_line_standard, bresenham_circle
from HW1.ui import get_input, line_drawer, circle_drawer


class TestInput(unittest.TestCase):
    @patch('builtins.input', side_effect=['(1, 2)', '(3, 4)'])
    def test_right_user_keyboard_input(self, mock_input):
        start, end = get_input()
        self.assertEqual(start, (1, 2))  # add assertion here
        self.assertEqual(end, (3, 4))

    @patch('builtins.input', side_effect=['1', '2', '(1, 2)', '(3, 4)'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_tried_again_user_keyboard_input(self, mock_stdout, mock_input):
        start, end = get_input()
        self.assertEqual(mock_stdout.getvalue().strip(), "Coordinates "
                                                         "entered is not "
                                                         "valid, please try again.")
        self.assertEqual(start, (1, 2))  # add assertion here
        self.assertEqual(end, (3, 4))

    @patch('builtins.input', side_effect=[1, 2])
    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_user_keyboard_input(self, mock_stdout, mock_input):
        get_input()
        self.assertEqual(mock_stdout.getvalue().strip(), "Invalid input type")


class TestLineDrawing(unittest.TestCase):
    def test_slope1(self):
        start = (-3, -3)
        end = (3, 3)
        x, y = bresenham_line_standard(start, end, 6)
        line_drawer(x, y)
        plt.show()

    def test_slope_less_1(self):
        start = (-3, -3)
        end = (3, -1)
        x, y = bresenham_line_standard(start, end, 6)
        line_drawer(x, y)
        plt.show()

    def test_slope_greater_1(self):
        start = (-3, -3)
        end = (-1, 3)
        x, y = bresenham_line_standard(start, end, 6)
        line_drawer(x, y)
        plt.show()

class TestCircleDrawing(unittest.TestCase):
    def test_origin(self):
        center = (0, 0)
        radius = 5
        x, y = bresenham_circle(center, radius, 10)
        circle_drawer(x, y, center, radius)
        plt.show()

    def test_not_origin(self):
        center = (3, 3)
        radius = 5
        x, y = bresenham_circle(center, radius, 10)
        circle_drawer(x, y, center, radius)
        plt.show()




if __name__ == '__main__':
    unittest.main()
