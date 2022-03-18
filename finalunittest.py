import signuptest
import logintest
import findhoteltest
import booktest
import unittest

signselurl = signuptest.selenium_url
logselurl = logintest.selenium_url
hotbookselurl = findhoteltest.selenium_url
payselurl = booktest.selenium_url

signtestword = 'signup'
logtestword = 'dashboard'
hotbooktestword = 'book'
paytestword = 'payment'


class finaltests(unittest.TestCase):

    def setUp(self):
        print('Test case started')

    def test_signup(self):
        selenium_version = signselurl
        self.assertIn(signtestword, selenium_version)

    def test_login(self):
        selenium_version = logselurl
        self.assertIn(logtestword, selenium_version)

    def test_hotel(self):
        selenium_version1 = hotbookselurl
        self.assertIn(hotbooktestword, selenium_version1)

    def test_payment(self):
        selenium_version = payselurl
        self.assertIn(paytestword, selenium_version)

    def tearDown(self):
        print("End of the test case")


if __name__ == '__main__':
    unittest.main()