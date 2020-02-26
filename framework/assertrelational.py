import unittest
from selenium import webdriver


class Test(unittest.TestCase):

    def test_name(self):
        self.assertLessEqual(10, 10)
        # self.assertLess(10, 100)
        # self.assertGreaterEqual(100, 100)
        # self.assertGreater(100, 10)


if __name__ == "__main__":
    unittest.main()
