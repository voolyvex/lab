from pytest import *
from account import *


class Test:
    def setup_method(self):
        self.a1 = Account('Checking')
        self.a2 = Account('Savings')

    
    def teardown_method(self):
        del self.a1
        del self.a2


    def test_init(self):
        assert self.a1.get_name() == 'Checking'
        assert self.a1.get_balance() == 0
        assert self.a2.get_name() == 'Savings'
        assert self.a2.get_balance() == 0


    def test_deposit(self):
        assert self.a1.deposit(5.01) is True
        assert self.a1.get_balance() == approx(5.01, abs=0.001)
        assert self.a2.deposit(0) is False
        assert self.a2.get_balance() == 0
       

    def test_withdraw(self):
        assert self.a1.withdraw(5) is False
        assert self.a1.get_balance() == 0
       
        assert self.a2.withdraw(-4.00) is False
        assert self.a2.get_balance() == 0
     
        self.a2.deposit(10)
        assert self.a2.withdraw(1.25) is True
        assert self.a2.get_balance() == approx(8.75, abs=0.001)
        
