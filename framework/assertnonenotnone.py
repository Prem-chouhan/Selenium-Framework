import unittest
from selenium import webdriver


class Test(unittest.TestCase):

    def test_name(self):
        # driver = webdriver.Firefox()
        driver = None
        # self.assertIsNone(driver)
        self.assertIsNotNone(driver)
        driver.close()


if __name__ == "__main__":
    unittest.main()
