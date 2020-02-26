import unittest


class AppTesting(unittest.TestCase):
    def test_Method(self):
        print("This is demo method")

    def test_name(self):
        print("This is remo")

    def test_gender(self):
        print("male")

    @unittest.skipIf(1 == 1, "City should be mumbai")
    def test_city(self):
        print("mumbai")

    @unittest.skip("State is not needed")
    def test_state(self):
        print("Maharastra")

    @unittest.skip
    def test_skip(self):
        print("This skip module")


if __name__ == "__main__":
    unittest.main()
