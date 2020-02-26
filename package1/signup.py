import unittest


class SignUp(unittest.TestCase):

    def test_signupByemail(self):
        print("This is signup by email")
        self.assertTrue(True)

    def test_signupByfacebook(self):
        print("This is signup by facebook")
        self.assertTrue(True)

    def test_signupBytwitter(self):
        print("This is signup by twitter")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
