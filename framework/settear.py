import unittest


def setUpModule():
    print("Set Up Module")


def tearDownModule():
    print("Tear down for Module")


class AppTesting(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("This is set of class")

    @classmethod
    def tearDownClass(cls):
        print("This is Tear of Class")

    @classmethod
    def setUp(self):
        print("This is login")

    @classmethod
    def tearDown(self):
        print("This is logout")

    def test_method(self):
        print("This is just a test module")


if __name__ == "__main__":
    unittest.main()
