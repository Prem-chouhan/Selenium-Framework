import unittest
from selenium import webdriver


class Test(unittest.TestCase):

    def test_name(self):
        driver = webdriver.Firefox()
        driver.get("https://www.google.com/")
        tittle = driver.title
        # self.assertEqual("Google123", tittle, "If Equal Throws True")
        self.assertNotEqual("Google", tittle, "If Equal Throws True")
        driver.close()


if __name__ == "__main__":
    unittest.main()
