import unittest
from selenium import webdriver


class Test(unittest.TestCase):

    def test_name(self):
        driver = webdriver.Firefox()
        driver.get("https://www.google.com/")
        tittle = driver.title
        # self.assertFalse(tittle == "Google123")
        self.assertTrue(tittle == "Google")
        driver.close()


if __name__ == "__main__":
    unittest.main()
