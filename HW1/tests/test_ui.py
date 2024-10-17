import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import matplotlib.patches as mpatches
import unittest
from unittest.mock import patch
from io import StringIO


from HW1.scanning_algorithms import bresenham_line_optimized, bresenham_line_standard, bresenham_circle
from HW1.ui import get_input


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
        draw_helper(x, y)

    def test_slope_less_1(self):
        start = (-3, -3)
        end = (3, -1)
        x, y = bresenham_line_standard(start, end, 6)
        draw_helper(x, y)

    def test_slope_greater_1(self):
        start = (-3, -3)
        end = (-1, 3)
        x, y = bresenham_line_standard(start, end, 6)
        draw_helper(x, y)

class TestCircleDrawing(unittest.TestCase):
    def test_origin(self):
        center = (0, 0)
        radius = 5
        x, y = bresenham_circle(center, radius, 100)
        circle_draw_helper(x, y, center, radius)


def draw_helper(x, y):
    fig, ax = plt.subplots()
    ax.set_xlim(-10, 10)
    ax.xaxis.set_major_locator(MultipleLocator(2))
    ax.xaxis.set_minor_locator(MultipleLocator(1))
    ax.set_ylim(-10, 10)
    ax.yaxis.set_major_locator(MultipleLocator(2))
    ax.yaxis.set_minor_locator(MultipleLocator(1))
    ax.grid(which='minor', linestyle=':', linewidth=0.5)
    ax.grid(True)
    ax.scatter(x, y)
    plt.show()


def circle_draw_helper(x, y, center, radius):
    fig, ax = plt.subplots()
    ax.set_xlim(-10, 10)
    ax.xaxis.set_major_locator(MultipleLocator(2))
    ax.xaxis.set_minor_locator(MultipleLocator(1))
    ax.set_ylim(-10, 10)
    ax.yaxis.set_major_locator(MultipleLocator(2))
    ax.yaxis.set_minor_locator(MultipleLocator(1))
    ax.set_aspect('equal')
    ax.grid(which='minor', linestyle=':', linewidth=0.5)
    ax.grid(True)
    ax.scatter(x, y)
    ax.add_patch(mpatches.Circle(center, radius, edgecolor='blue', facecolor='none', linewidth=1, linestyle=':'))
    plt.show()


if __name__ == '__main__':
    unittest.main()
