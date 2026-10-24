import unittest
import main


class MyTestCase(unittest.TestCase):
    def test_something(self, main):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
