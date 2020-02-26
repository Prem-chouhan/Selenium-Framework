import unittest


class LoginTest(unittest.TestCase):

    def test_loginByemail(self):
        print("This is login by email")
        self.assertTrue(True)

    def test_loginByfacebook(self):
        print("This is login by facebook")
        self.assertTrue(True)

    def test_loginBytwitter(self):
        print("This is login by twitter")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
