import unittest


class PaymentTest(unittest.TestCase):

    def test_paymentindollars(self):
        print("This is payment in dollars")
        self.assertTrue(True)

    def test_paymentinrupees(self):
        print("This is payment in rupees")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
