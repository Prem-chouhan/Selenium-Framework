import unittest
from selenium import webdriver


class Test(unittest.TestCase):

    def test_name(self):
        list = {"python", "selenium", "framework"}
        # self.assertIn("python", list)
        # self.assertNotIn("python", list)


if __name__ == "__main__":
    unittest.main()
