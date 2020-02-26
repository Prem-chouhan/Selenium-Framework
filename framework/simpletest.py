import unittest
from selenium import webdriver


class SearchEngineTest(unittest.TestCase):
    def test_google(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.google.com/")
        print("Tittle of this page" + self.driver.title)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()