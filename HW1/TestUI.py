import unittest
from unittest.mock import patch

from HW1.UI import get_input


class MyTestCase(unittest.TestCase):
    @patch('builtins.input', side_effect=['(1, 2)', '(3, 4)'])
    def test_right_user_keyboard_input(self, mock_input):
        start, end = get_input()
        self.assertEqual(start, (1, 2))  # add assertion here
        self.assertEqual(end, (3, 4))

    @patch('builtins.input', side_effect=['1', '2'])
    def test_invalid_user_keyboard_input(self, mock_input):
        start, end = get_input()
        self.assertEqual(start, (1, 2))  # add assertion here
        self.assertEqual(end, (3, 4))


if __name__ == '__main__':
    unittest.main()
