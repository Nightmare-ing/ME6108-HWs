import matplotlib.pyplot as plt
import unittest
from unittest.mock import patch
from io import StringIO


from HW1.scanning_algorithms import bresenham_line_optimized, bresenham_line_standard, bresenham_circle
from HW1.ui import Drawer, get_input_line, get_input_circle

# Create a drawer object for drawing test classes
_drawer = Drawer()


class TestInput(unittest.TestCase):
    @patch('builtins.input', side_effect=['(1, 2)', '(3, 4)'])
    def test_right_user_keyboard_input(self, mock_input):
        """
        Test the right user keyboard input
        :param mock_input: required for patching the input function
        """
        start, end = get_input_line()
        self.assertEqual(start, (1, 2))  # add assertion here
        self.assertEqual(end, (3, 4))

    @patch('builtins.input', side_effect=['1', '2', '(1, 2)', '(3, 4)'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_tried_again_user_keyboard_input(self, mock_stdout, mock_input):
        """
        Test the case when the user input is invalid and tried again
        :param mock_stdout: required for patching the stdout
        :param mock_input: required for patching the input function
        """
        start, end = get_input_line()
        self.assertEqual(mock_stdout.getvalue().strip(), "Coordinates "
                                                         "entered is not "
                                                         "valid, please try again.")
        self.assertEqual(start, (1, 2))  # add assertion here
        self.assertEqual(end, (3, 4))

    @patch('builtins.input', side_effect=[1, 2])
    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_user_keyboard_input(self, mock_stdout, mock_input):
        """
        Test the case when the user input is invalid.
        Maybe often for some irregular input
        :param mock_stdout: required for patching the stdout
        :param mock_input: required for patching the input function
        """
        get_input_line()
        self.assertEqual(mock_stdout.getvalue().strip(), "Invalid input type")

    @patch('builtins.input', side_effect=['(1, 2)', '3'])
    def test_valid_circle_keyboard_input(self, mock_input):
        """
        Test the case when the user input is valid for circle.
        The code is the same as the line input, so just test the valid input, I didn't optimize this because I'm lazy.
        Maybe update this later.
        :param mock_input: required for patching the input function
        """
        center, radius = get_input_circle()
        self.assertEqual(center, (1, 2))
        self.assertEqual(radius, 3)


class TestLineDrawing(unittest.TestCase):
    def test_slope1(self):
        """
        Draw the line to show the case when the slope is 1
        """
        start = (-3, -3)
        end = (3, 3)
        x, y = bresenham_line_standard(start, end, 6)
        _drawer.set_fig()
        _drawer.line_drawer(x, y)
        plt.show()

    def test_slope_less_1(self):
        """
        Draw the line to show the case when the slope is less than 1
        """
        start = (-3, -3)
        end = (3, -1)
        x, y = bresenham_line_standard(start, end, 6)
        _drawer.set_fig()
        _drawer.line_drawer(x, y)
        plt.show()

    def test_slope_greater_1(self):
        """
        Draw the line to show the case when the slope is greater than 1
        """
        start = (-3, -3)
        end = (-1, 3)
        x, y = bresenham_line_standard(start, end, 6)
        _drawer.set_fig()
        _drawer.line_drawer(x, y)
        plt.show()

class TestCircleDrawing(unittest.TestCase):
    def test_origin(self):
        """
        Draw the circle to show the case when the center is the origin
        """
        center = (0, 0)
        radius = 5
        x, y = bresenham_circle(center, radius, 10)
        _drawer.set_fig()
        _drawer.circle_drawer(x, y, center, radius)
        plt.show()

    def test_not_origin(self):
        """
        Draw the circle to show the case when the center is not the origin
        """
        center = (3, 3)
        radius = 5
        x, y = bresenham_circle(center, radius, 10)
        TestCircleDrawing.drawer.set_fig()
        TestCircleDrawing.drawer.circle_drawer(x, y, center, radius)
        plt.show()




if __name__ == '__main__':
    unittest.main()
