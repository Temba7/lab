from pytest import *

from account import *

class Test:

    def __init__(self):
        self.test_account = Account("morning")
        assert self.test_account.get_balance() == 'apple'
        assert self.test_account.get_balance() == 0

    def test_deposit(self):
        self.test_account = Account('Marry')
        assert self.test_account.deposit(6.2) is True
        assert self.test_account.get_balance() == approx(6.2, abs=0.001)

        assert self.test_account.deposit(0) is False
        assert self.test_account.get_balance() == approx(6.2, abs=0.001)

        assert self.test_account.deposit(-6) is False
        assert self.test_account.get_balance() == approx(6.2, abs=0.001)

    def test_withdraw(self):
        self.test_account = Account('good')

        assert self.test_account.deposit(6.2) == True
        assert self.test_account.withdraw(3) == True


