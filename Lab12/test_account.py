from account import Account
import unittest

class test_account(unittest.TestCase):
    def test_init(self):
        self.assertEqual(Account('Bob'), 'Bob')

    def test_deposit(self):
        self.assertTrue(Account.deposit(10.20), True)
        self.assertFalse(Account.deposit('hello'), False)

    def test_withdraw(self):
        self.assertTrue(Account.withdraw(20.10), True)
        self.assertFalse(Account.withdraw('hey'), False)



