import unittest

from package1.login import LoginTest
from package1.signup import SignUp

from package2.paymenttest import PaymentTest
from package2.paymwntreturn import PaymentReturn

tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SignUp)
tc3 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturn)

sanityTestSuites = unittest.TestSuite([tc1, tc2])
functionalityTestSuites = unittest.TestSuite([tc3, tc4])
masterTestSuites = unittest.TestSuite([tc1, tc2, tc3, tc4])
unittest.TextTestRunner().run(sanityTestSuites)
