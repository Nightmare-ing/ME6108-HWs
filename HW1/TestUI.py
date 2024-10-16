import unittest
from unittest.mock import patch
from io import StringIO

from HW1.UI import get_input


class MyTestCase(unittest.TestCase):
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




if __name__ == '__main__':
    unittest.main()
